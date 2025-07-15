#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROS 2 node : Unbeatable Tic‑Tac‑Toe agent (Pepper joue **O**)
===========================================================
* Bleu  → **X** (1) — joueur humain
* Jaune → **O** (0) — le robot

Améliorations 2025‑07‑15
-----------------------
• Minimax ► Alpha‑β pruning + mémoïsation + score dépendant de la profondeur (gagne vite, perd tard).
• Premier coup déterministe : centre si libre, sinon angle.
• Cache remis à zéro à la fin de chaque partie pour éviter la croissance mémoire.
"""

from __future__ import annotations

import json
import random
import re
import requests
from typing import List, Optional, Tuple, Dict

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

MODEL: str = "mistral:7b"
OLLAMA_URL: str = "http://localhost:11434/api/generate"
MAX_TOKENS: int = 12
TIMEOUT: int = 120  # seconds
INF: int = 10  # borne pour le score


class MistralMinimaxPrompt(Node):
    """ROS 2 node that queries a local Mistral LLM to play unbeatable O."""

    rows: List[str] = ["A", "B", "C"]

    # ---- Phrases variées ----
    move_phrases = [
        "I play {cell}.",
        "Here is my move: {cell}.",
        "Let's try {cell}.",
        "I'm placing my cup on {cell}.",
        "My choice is {cell}!"
    ]
    turn_phrases = [
        "Your turn!",
        "It's up to you!",
        "Go ahead!",
        "Now, it's your move!",
        "I'm waiting for your move."
    ]
    win_phrases = [
        "Yeah, I won!",
        "Victory for me!",
        "I did it!",
        "Good game, I win!",
        "I'm the champion!"
    ]
    lose_phrases = [
        "Oh no, I lost…",
        "You win, well played!",
        "You got me this time!",
        "Congrats, you beat me!",
        "Impressive, you win!"
    ]
    draw_phrases = [
        "It's a draw!",
        "No winner this time.",
        "It's a tie!",
        "Neither of us wins.",
        "Stalemate, well played!"
    ]
    correct_phrases = [
        "I was about to play {wrong}, but I think {right} is better!",
        "Let me change my mind. {right} is a stronger move.",
        "Actually, {right} is the optimal move.",
        "I'm going to play {right} instead, that's a smarter choice!"
    ]

    def __init__(self) -> None:
        super().__init__("mistral_minimax_ai")

        # --- Communication ROS -------------
        self.sub_state = self.create_subscription(
            String, "/tic_tac_state", self.state_cb, 10
        )
        self.pub_move = self.create_publisher(String, "/reponse_case_morpion", 10)

        speech_topic = self.declare_parameter("speech_topic", "/speech").value
        self.pub_speech = self.create_publisher(String, speech_topic, 10)

        # --- États internes ----------------
        self.msg_out = String()
        self.prev_x: int = 0
        self.prev_o: int = 0
        self.expecting_opponent: bool = False

        self.cases_deja_jouees: set[str] = set()
        self.saved_board: List[List[str]] = [["" for _ in range(3)] for _ in range(3)]
        self._cache: Dict[Tuple[Tuple[int, ...], int], int] = {}

        # --- Logs + warm‑up ----------------
        self.get_logger().info(
            "MistralMinimaxPrompt ready — X: blue, O: yellow (robot)"
        )
        self._warmup_llm()

    # ------------------------------------------------------------------
    # Utilitaires plateau
    # ------------------------------------------------------------------
    @staticmethod
    def _flatten(board: List[List[str]]) -> Tuple[int, ...]:
        mapping = {"yellow": 0, "cup_yellow": 0, "blue": 1, "cup_blue": 1}
        return tuple(mapping.get(cell, -1) for row in board for cell in row)

    @staticmethod
    def _winner(flat: Tuple[int, ...]) -> Optional[int]:
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6),            # diagonals
        ]
        for a, b, c in lines:
            if flat[a] == flat[b] == flat[c] != -1:
                return flat[a]
        return None

    def _empty_cells(self, flat: Tuple[int, ...]) -> List[str]:
        return [
            self.rows[i] + str(j + 1)
            for i in range(3)
            for j in range(3)
            if flat[3 * i + j] == -1 and (self.rows[i] + str(j + 1)) not in self.cases_deja_jouees
        ]

    def _cell_occupied(self, cell: str, flat: Tuple[int, ...]) -> bool:
        try:
            idx = self.rows.index(cell[0].upper()) * 3 + int(cell[1]) - 1
            return flat[idx] != -1
        except (ValueError, IndexError):
            return True

    # ------------------------------------------------------------------
    # Minimax avec alpha‑β + mémoïsation
    # ------------------------------------------------------------------
    def _minimax(self, flat: Tuple[int, ...], player: int, depth: int = 0,
                 alpha: int = -INF, beta: int = INF) -> int:
        key = (flat, player)
        if key in self._cache:
            return self._cache[key]

        winner = self._winner(flat)
        if winner is not None:
            score = (INF - depth) if winner == 0 else (depth - INF)
        elif -1 not in flat:  # draw
            score = 0
        else:
            best = -INF if player == 0 else INF
            for idx in range(9):
                if flat[idx] != -1:
                    continue
                # jouer
                new_flat = list(flat)
                new_flat[idx] = player
                new_flat_t = tuple(new_flat)
                val = self._minimax(new_flat_t, 1 - player, depth + 1, alpha, beta)
                if player == 0:  # maximiser
                    best = max(best, val)
                    alpha = max(alpha, best)
                else:           # minimiser
                    best = min(best, val)
                    beta = min(beta, best)
                if beta <= alpha:
                    break  # coupure alpha‑β
            score = best

        self._cache[key] = score
        return score

    def best_move(self, flat: Tuple[int, ...]) -> int:
        best_score = -INF
        move: Optional[int] = None
        for idx in range(9):
            if flat[idx] != -1:
                continue
            new_flat = list(flat)
            new_flat[idx] = 0  # robot joue O
            score = self._minimax(tuple(new_flat), 1, 1)  # humain joue après
            if score > best_score:
                best_score = score
                move = idx
        assert move is not None  # il doit toujours y avoir un coup
        return move

    # ------------------------------------------------------------------
    # ROS callback principal
    # ------------------------------------------------------------------
    def state_cb(self, msg: String) -> None:
        # Parse JSON
        try:
            board = json.loads(msg.data)["board"]
            if len(board) != 3 or any(len(r) != 3 for r in board):
                raise ValueError
        except Exception:
            self.get_logger().warning("/tic_tac_state mal formé — ignoré")
            return

        # Fusion vision ↔ mémoire
        for i in range(3):
            for j in range(3):
                current = board[i][j]
                prev = self.saved_board[i][j]
                if current in ["", None, -1] and prev not in ["", None, -1]:
                    board[i][j] = prev
                elif current not in ["", None, -1]:
                    board[i][j] = current
                self.saved_board[i][j] = board[i][j]

        flat = self._flatten(board)
        winner = self._winner(flat)
        if winner is not None or -1 not in flat:  # fin de partie
            status = "draw" if winner is None else ("X wins" if winner == 1 else "O wins")
            self.get_logger().info(f"Game over ({status}) — no move sent")
            phrase_list = self.draw_phrases if winner is None else (self.win_phrases if winner == 0 else self.lose_phrases)
            self._say(random.choice(phrase_list))
            self._reset_game()
            return

        n_x, n_o = flat.count(1), flat.count(0)

        # Synchronisation tour humain
        if self.expecting_opponent:
            if n_x == self.prev_x:
                return  # on attend encore le mouvement adverse
            self.expecting_opponent = False
            self._say(random.choice(self.turn_phrases))

        if n_x != n_o + 1:  # état incohérent : on attend
            self.prev_x, self.prev_o = n_x, n_o
            return

        # --- Choix du coup robot ---
        empty_cells = self._empty_cells(flat)

        # 1. Premier coup robot : stratégie fixe (centre → angle)
        if n_x == 1 and n_o == 0:
            if flat[4] == -1:
                move = "B2"
            else:
                move = next((c for c in ("A1", "A3", "C1", "C3") if c in empty_cells), random.choice(empty_cells))
            self._say_move(move)
            self._publish(move, n_x, n_o)
            return

        # 2. Proposition du LLM validée par Minimax
        mistral_move = self._choose_move(flat)
        valid = (
            mistral_move and
            not self._cell_occupied(mistral_move, flat) and
            mistral_move in empty_cells
        )
        idx_llm: Optional[int] = None
        if valid:
            idx_llm = self.rows.index(mistral_move[0].upper()) * 3 + int(mistral_move[1]) - 1

        best_idx = self.best_move(flat)
        i, j = divmod(best_idx, 3)
        best_move_str = self.rows[i] + str(j + 1)

        if valid and idx_llm == best_idx:  # le LLM est optimal
            self._say_move(mistral_move)
            self._publish(mistral_move, n_x, n_o)
        else:
            if valid:  # correction verbale
                correction_phrase = random.choice(self.correct_phrases).format(
                    wrong=mistral_move, right=best_move_str
                )
                self._say(correction_phrase)
            else:
                self._say_move(best_move_str)
            self._publish(best_move_str, n_x, n_o)

    # ------------------------------------------------------------------
    # Helpers divers
    # ------------------------------------------------------------------
    def _say_move(self, cell: str) -> None:
        self._say(random.choice(self.move_phrases).format(cell=cell))
        self._say(random.choice(self.turn_phrases))

    def _build_prompt(self, flat: Tuple[int, ...]) -> str:
        board_str = "\n".join(
            f"{self.rows[i]}  [ " + ", ".join(
                "X" if flat[3 * i + j] == 1 else "O" if flat[3 * i + j] == 0 else "_"
                for j in range(3)
            ) + " ]" for i in range(3)
        )
        empties = ", ".join(self._empty_cells(flat))
        return (
            "You are Player 2 (O, yellow). Player 1 is X (blue).\n"
            f"Choose ONE empty cell among: {empties}\n"
            "Reply ONLY with that cell (e.g. B2).\n\nCurrent board:\n" + board_str + "\n"
        )

    def _choose_move(self, flat: Tuple[int, ...]) -> Optional[str]:
        prompt = self._build_prompt(flat)
        payload = {
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"num_predict": MAX_TOKENS},
        }
        try:
            response = requests.post(OLLAMA_URL, json=payload, timeout=TIMEOUT)
            text = response.json().get("response", "")
            match = re.search(r"([ABCabc][123])", text)
            return match.group(1).upper() if match else None
        except Exception as exc:
            self.get_logger().error(f"LLM request error: {exc}")
            return None

    def _publish(self, cell: str, n_x: int, n_o: int) -> None:
        self.msg_out.data = cell
        self.pub_move.publish(self.msg_out)
        self.get_logger().info(f"AI plays: {cell}")
        self.cases_deja_jouees.add(cell)
        self.prev_x, self.prev_o = n_x, n_o + 1
        self.expecting_opponent = True

    def _say(self, text: str) -> None:
        if self.pub_speech.get_subscription_count() > 0:
            self.pub_speech.publish(String(data=text))

    def _reset_game(self) -> None:
        """Nettoie l'état interne à la fin d'une partie."""
        self.cases_deja_jouees.clear()
        self.saved_board = [["" for _ in range(3)] for _ in range(3)]
        self._cache.clear()
        self.prev_x = self.prev_o = 0
        self.expecting_opponent = False

    # ------------------------------------------------------------------
    # Initialisation LLM (warm‑up)
    # ------------------------------------------------------------------
    def _warmup_llm(self) -> None:
        try:
            requests.post(
                OLLAMA_URL,
                json={"model": MODEL, "prompt": "warm‑up", "stream": False},
                timeout=TIMEOUT,
            )
        except Exception:
            pass


def main(args=None):
    rclpy.init(args=args)
    node = MistralMinimaxPrompt()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()