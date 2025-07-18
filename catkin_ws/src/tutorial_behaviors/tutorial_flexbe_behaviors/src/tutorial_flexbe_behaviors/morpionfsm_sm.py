#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.decision_state import DecisionState
from flexbe_states.publisher_string_state import PublisherStringState
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jul 09 2025
@author: Zakaria
'''
class MorpionFSMSM(Behavior):
	'''
	machine a etat morpion
	'''


	def __init__(self):
		super(MorpionFSMSM, self).__init__()
		self.name = 'MorpionFSM'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:987 y:285, x:976 y:360
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.grid = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:214 y:46
			OperatableStateMachine.add('WAIT_BOARD',
										SubscriberState(topic='/board_homography', blocking=True, clear=False),
										transitions={'received': 'READY', 'unavailable': 'ERROR_RECOVERY'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:713 y:33
			OperatableStateMachine.add('DECIDE_TURN',
										DecisionState(outcomes=["robot","human"], conditions={   "robot": lambda g: g.count("yellow") == g.count("blue"),   "human": lambda g: g.count("yellow")  > g.count("blue") }),
										transitions={'robot': 'COMPUTE_MOVE', 'human': 'READY'},
										autonomy={'robot': Autonomy.Off, 'human': Autonomy.Off},
										remapping={'input_value': 'grid'})

			# x:222 y:220
			OperatableStateMachine.add('ERROR_RECOVERY',
										PublisherStringState(topic='/speech'),
										transitions={'done': 'WAIT_BOARD'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'grid'})

			# x:418 y:52
			OperatableStateMachine.add('READY',
										SubscriberState(topic='/tic_tac_state', blocking=True, clear=False),
										transitions={'received': 'DECIDE_TURN', 'unavailable': 'ERROR_RECOVERY'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'grid'})

			# x:25 y:305
			OperatableStateMachine.add('RESET',
										WaitState(wait_time=5.0),
										transitions={'done': 'WAIT_BOARD'},
										autonomy={'done': Autonomy.Off})

			# x:708 y:379
			OperatableStateMachine.add('Wait_MOVE',
										SubscriberState(topic='/move_done', blocking=True, clear=False),
										transitions={'received': 'RESET', 'unavailable': 'ERROR_RECOVERY'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:700 y:148
			OperatableStateMachine.add('COMPUTE_MOVE',
										SubscriberState(topic='/reponse_case_morpion', blocking=True, clear=False),
										transitions={'received': 'Wait_MOVE', 'unavailable': 'ERROR_RECOVERY'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'move'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
