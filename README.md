# Guide utilisateur Morpion – Robot Pepper

**Auteur** : Zakaria ALLOUCHE
**Affiliation** : ISIR, Sorbonne Université
**Date** : 18 juillet 2025

---

## Introduction

Ce document présente les étapes nécessaires pour lancer et utiliser le code ROS du jeu de Morpion développé durant mon stage à l’ISIR.

---

## Pré-requis

Assurez-vous d’avoir les pré-requis suivants :

* Ubuntu 20.04
* ROS 1 Noetic
* NAOqi driver
* ROS 2 Foxy
* Workspace ROS 1 configuré avec les packages suivants :
  `naoqi_driver`, `testpython`, `translator`, `flexbe_app`, `flexbe_behavior_engine`
* Workspace ROS 2 configuré avec le package `Morpion`

---

## Compilation des Workspaces

### 1. Workspace ROS 1

```bash
use_ros1
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

### 2. Workspace ROS 2

```bash
use_ros2
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

---

## Étapes de lancement

### Lancement du robot Pepper

```bash
use_ros1
cd ~/catkin_ws
source devel/setup.bash
roslaunch testpython pepper_init.launch
```

### Lancement du bridge ROS 1 / ROS 2

Ouvrez un nouveau terminal :

```bash
use_ros1
use_ros2
ros2 run ros1_bridge dynamic_bridge --bridge-all-topics
```

### Lancement de la machine à états FlexBe

```bash
use_ros1
cd ~/catkin_ws
source devel/setup.bash
roslaunch flexbe_app flexbe_full.launch
```

> Après le lancement de FlexBe, sélectionnez **Load Behavior**, choisissez **MorpionFSM**, puis cliquez sur **Runtime Control** et **Start Execution**.

### Lancement des noeuds du morpion ROS 2

```bash
use_ros2
ros2 launch morpion morpion_launch.py
```
### Changement de résolution de la caméra

Pour modifier la résolution de la caméra du robot Pepper, éditez le fichier `boot_config.json` :

```bash
cd ~/catkin_ws/src/naoqi_driver/share
gedit boot_config.json
```

---

## Conclusion

Ce guide présente les commandes essentielles pour l’utilisation du code ROS du Morpion avec le robot Pepper.
Pour toute question complémentaire, n’hésitez pas à me contacter :

* [zakaria.allouche@etu.sorbonne-universite.fr](mailto:zakaria.allouche@etu.sorbonne-universite.fr)
* [zakaria.allouche@isir.upmc.fr](mailto:zakaria.allouche@isir.upmc.fr)

