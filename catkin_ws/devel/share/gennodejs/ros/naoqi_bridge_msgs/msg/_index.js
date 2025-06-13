
"use strict";

let FloatArrayStamped = require('./FloatArrayStamped.js');
let BoolStamped = require('./BoolStamped.js');
let MemoryPairFloat = require('./MemoryPairFloat.js');
let AudioBuffer = require('./AudioBuffer.js');
let JointAnglesWithSpeed = require('./JointAnglesWithSpeed.js');
let RobotInfo = require('./RobotInfo.js');
let IntArrayStamped = require('./IntArrayStamped.js');
let JointAngleTrajectory = require('./JointAngleTrajectory.js');
let HeadTouch = require('./HeadTouch.js');
let StringStamped = require('./StringStamped.js');
let EventStamped = require('./EventStamped.js');
let IntStamped = require('./IntStamped.js');
let Bumper = require('./Bumper.js');
let MemoryPairString = require('./MemoryPairString.js');
let WordRecognized = require('./WordRecognized.js');
let FaceROI = require('./FaceROI.js');
let PoseWithConfidenceStamped = require('./PoseWithConfidenceStamped.js');
let HandTouch = require('./HandTouch.js');
let StatusChangeStamped = require('./StatusChangeStamped.js');
let MemoryPairInt = require('./MemoryPairInt.js');
let FadeRGB = require('./FadeRGB.js');
let FloatStamped = require('./FloatStamped.js');
let StringArrayStamped = require('./StringArrayStamped.js');
let MemoryList = require('./MemoryList.js');
let SoundLocated = require('./SoundLocated.js');
let BodyROI = require('./BodyROI.js');
let SpeechWithFeedbackGoal = require('./SpeechWithFeedbackGoal.js');
let BlinkGoal = require('./BlinkGoal.js');
let JointTrajectoryActionResult = require('./JointTrajectoryActionResult.js');
let JointAnglesWithSpeedActionFeedback = require('./JointAnglesWithSpeedActionFeedback.js');
let SpeechWithFeedbackFeedback = require('./SpeechWithFeedbackFeedback.js');
let RunBehaviorAction = require('./RunBehaviorAction.js');
let BlinkResult = require('./BlinkResult.js');
let RunBehaviorActionGoal = require('./RunBehaviorActionGoal.js');
let JointAnglesWithSpeedAction = require('./JointAnglesWithSpeedAction.js');
let BlinkFeedback = require('./BlinkFeedback.js');
let BodyPoseWithSpeedResult = require('./BodyPoseWithSpeedResult.js');
let RunBehaviorActionFeedback = require('./RunBehaviorActionFeedback.js');
let SpeechWithFeedbackAction = require('./SpeechWithFeedbackAction.js');
let JointAnglesWithSpeedGoal = require('./JointAnglesWithSpeedGoal.js');
let JointTrajectoryFeedback = require('./JointTrajectoryFeedback.js');
let JointAnglesWithSpeedFeedback = require('./JointAnglesWithSpeedFeedback.js');
let FollowPathActionResult = require('./FollowPathActionResult.js');
let JointAnglesWithSpeedActionGoal = require('./JointAnglesWithSpeedActionGoal.js');
let BodyPoseWithSpeedAction = require('./BodyPoseWithSpeedAction.js');
let FollowPathResult = require('./FollowPathResult.js');
let BlinkActionResult = require('./BlinkActionResult.js');
let SpeechWithFeedbackResult = require('./SpeechWithFeedbackResult.js');
let BodyPoseAction = require('./BodyPoseAction.js');
let JointTrajectoryAction = require('./JointTrajectoryAction.js');
let JointTrajectoryActionFeedback = require('./JointTrajectoryActionFeedback.js');
let BodyPoseResult = require('./BodyPoseResult.js');
let JointTrajectoryResult = require('./JointTrajectoryResult.js');
let SetSpeechVocabularyActionGoal = require('./SetSpeechVocabularyActionGoal.js');
let BodyPoseGoal = require('./BodyPoseGoal.js');
let BodyPoseActionGoal = require('./BodyPoseActionGoal.js');
let FollowPathGoal = require('./FollowPathGoal.js');
let FollowPathAction = require('./FollowPathAction.js');
let BodyPoseWithSpeedActionResult = require('./BodyPoseWithSpeedActionResult.js');
let SetSpeechVocabularyResult = require('./SetSpeechVocabularyResult.js');
let JointTrajectoryActionGoal = require('./JointTrajectoryActionGoal.js');
let RunBehaviorResult = require('./RunBehaviorResult.js');
let FollowPathFeedback = require('./FollowPathFeedback.js');
let FollowPathActionFeedback = require('./FollowPathActionFeedback.js');
let BodyPoseWithSpeedFeedback = require('./BodyPoseWithSpeedFeedback.js');
let RunBehaviorGoal = require('./RunBehaviorGoal.js');
let BodyPoseActionFeedback = require('./BodyPoseActionFeedback.js');
let BlinkActionGoal = require('./BlinkActionGoal.js');
let BodyPoseActionResult = require('./BodyPoseActionResult.js');
let BodyPoseFeedback = require('./BodyPoseFeedback.js');
let SetSpeechVocabularyFeedback = require('./SetSpeechVocabularyFeedback.js');
let FollowPathActionGoal = require('./FollowPathActionGoal.js');
let JointAnglesWithSpeedActionResult = require('./JointAnglesWithSpeedActionResult.js');
let SetSpeechVocabularyAction = require('./SetSpeechVocabularyAction.js');
let SpeechWithFeedbackActionResult = require('./SpeechWithFeedbackActionResult.js');
let SpeechWithFeedbackActionFeedback = require('./SpeechWithFeedbackActionFeedback.js');
let SetSpeechVocabularyActionResult = require('./SetSpeechVocabularyActionResult.js');
let BlinkAction = require('./BlinkAction.js');
let JointAnglesWithSpeedResult = require('./JointAnglesWithSpeedResult.js');
let BodyPoseWithSpeedActionFeedback = require('./BodyPoseWithSpeedActionFeedback.js');
let RunBehaviorActionResult = require('./RunBehaviorActionResult.js');
let BodyPoseWithSpeedGoal = require('./BodyPoseWithSpeedGoal.js');
let SetSpeechVocabularyActionFeedback = require('./SetSpeechVocabularyActionFeedback.js');
let SpeechWithFeedbackActionGoal = require('./SpeechWithFeedbackActionGoal.js');
let SetSpeechVocabularyGoal = require('./SetSpeechVocabularyGoal.js');
let JointTrajectoryGoal = require('./JointTrajectoryGoal.js');
let BodyPoseWithSpeedActionGoal = require('./BodyPoseWithSpeedActionGoal.js');
let BlinkActionFeedback = require('./BlinkActionFeedback.js');
let RunBehaviorFeedback = require('./RunBehaviorFeedback.js');

module.exports = {
  FloatArrayStamped: FloatArrayStamped,
  BoolStamped: BoolStamped,
  MemoryPairFloat: MemoryPairFloat,
  AudioBuffer: AudioBuffer,
  JointAnglesWithSpeed: JointAnglesWithSpeed,
  RobotInfo: RobotInfo,
  IntArrayStamped: IntArrayStamped,
  JointAngleTrajectory: JointAngleTrajectory,
  HeadTouch: HeadTouch,
  StringStamped: StringStamped,
  EventStamped: EventStamped,
  IntStamped: IntStamped,
  Bumper: Bumper,
  MemoryPairString: MemoryPairString,
  WordRecognized: WordRecognized,
  FaceROI: FaceROI,
  PoseWithConfidenceStamped: PoseWithConfidenceStamped,
  HandTouch: HandTouch,
  StatusChangeStamped: StatusChangeStamped,
  MemoryPairInt: MemoryPairInt,
  FadeRGB: FadeRGB,
  FloatStamped: FloatStamped,
  StringArrayStamped: StringArrayStamped,
  MemoryList: MemoryList,
  SoundLocated: SoundLocated,
  BodyROI: BodyROI,
  SpeechWithFeedbackGoal: SpeechWithFeedbackGoal,
  BlinkGoal: BlinkGoal,
  JointTrajectoryActionResult: JointTrajectoryActionResult,
  JointAnglesWithSpeedActionFeedback: JointAnglesWithSpeedActionFeedback,
  SpeechWithFeedbackFeedback: SpeechWithFeedbackFeedback,
  RunBehaviorAction: RunBehaviorAction,
  BlinkResult: BlinkResult,
  RunBehaviorActionGoal: RunBehaviorActionGoal,
  JointAnglesWithSpeedAction: JointAnglesWithSpeedAction,
  BlinkFeedback: BlinkFeedback,
  BodyPoseWithSpeedResult: BodyPoseWithSpeedResult,
  RunBehaviorActionFeedback: RunBehaviorActionFeedback,
  SpeechWithFeedbackAction: SpeechWithFeedbackAction,
  JointAnglesWithSpeedGoal: JointAnglesWithSpeedGoal,
  JointTrajectoryFeedback: JointTrajectoryFeedback,
  JointAnglesWithSpeedFeedback: JointAnglesWithSpeedFeedback,
  FollowPathActionResult: FollowPathActionResult,
  JointAnglesWithSpeedActionGoal: JointAnglesWithSpeedActionGoal,
  BodyPoseWithSpeedAction: BodyPoseWithSpeedAction,
  FollowPathResult: FollowPathResult,
  BlinkActionResult: BlinkActionResult,
  SpeechWithFeedbackResult: SpeechWithFeedbackResult,
  BodyPoseAction: BodyPoseAction,
  JointTrajectoryAction: JointTrajectoryAction,
  JointTrajectoryActionFeedback: JointTrajectoryActionFeedback,
  BodyPoseResult: BodyPoseResult,
  JointTrajectoryResult: JointTrajectoryResult,
  SetSpeechVocabularyActionGoal: SetSpeechVocabularyActionGoal,
  BodyPoseGoal: BodyPoseGoal,
  BodyPoseActionGoal: BodyPoseActionGoal,
  FollowPathGoal: FollowPathGoal,
  FollowPathAction: FollowPathAction,
  BodyPoseWithSpeedActionResult: BodyPoseWithSpeedActionResult,
  SetSpeechVocabularyResult: SetSpeechVocabularyResult,
  JointTrajectoryActionGoal: JointTrajectoryActionGoal,
  RunBehaviorResult: RunBehaviorResult,
  FollowPathFeedback: FollowPathFeedback,
  FollowPathActionFeedback: FollowPathActionFeedback,
  BodyPoseWithSpeedFeedback: BodyPoseWithSpeedFeedback,
  RunBehaviorGoal: RunBehaviorGoal,
  BodyPoseActionFeedback: BodyPoseActionFeedback,
  BlinkActionGoal: BlinkActionGoal,
  BodyPoseActionResult: BodyPoseActionResult,
  BodyPoseFeedback: BodyPoseFeedback,
  SetSpeechVocabularyFeedback: SetSpeechVocabularyFeedback,
  FollowPathActionGoal: FollowPathActionGoal,
  JointAnglesWithSpeedActionResult: JointAnglesWithSpeedActionResult,
  SetSpeechVocabularyAction: SetSpeechVocabularyAction,
  SpeechWithFeedbackActionResult: SpeechWithFeedbackActionResult,
  SpeechWithFeedbackActionFeedback: SpeechWithFeedbackActionFeedback,
  SetSpeechVocabularyActionResult: SetSpeechVocabularyActionResult,
  BlinkAction: BlinkAction,
  JointAnglesWithSpeedResult: JointAnglesWithSpeedResult,
  BodyPoseWithSpeedActionFeedback: BodyPoseWithSpeedActionFeedback,
  RunBehaviorActionResult: RunBehaviorActionResult,
  BodyPoseWithSpeedGoal: BodyPoseWithSpeedGoal,
  SetSpeechVocabularyActionFeedback: SetSpeechVocabularyActionFeedback,
  SpeechWithFeedbackActionGoal: SpeechWithFeedbackActionGoal,
  SetSpeechVocabularyGoal: SetSpeechVocabularyGoal,
  JointTrajectoryGoal: JointTrajectoryGoal,
  BodyPoseWithSpeedActionGoal: BodyPoseWithSpeedActionGoal,
  BlinkActionFeedback: BlinkActionFeedback,
  RunBehaviorFeedback: RunBehaviorFeedback,
};
