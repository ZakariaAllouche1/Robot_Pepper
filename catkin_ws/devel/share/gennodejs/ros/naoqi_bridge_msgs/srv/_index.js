
"use strict";

let GetBodyROI = require('./GetBodyROI.js')
let GetTruepose = require('./GetTruepose.js')
let GetFacesROI = require('./GetFacesROI.js')
let TangentialSecurityDistance = require('./TangentialSecurityDistance.js')
let GetString = require('./GetString.js')
let GetFloat = require('./GetFloat.js')
let GetInstalledBehaviors = require('./GetInstalledBehaviors.js')
let SetTransform = require('./SetTransform.js')
let SetFloat = require('./SetFloat.js')
let CmdPoseService = require('./CmdPoseService.js')
let OrthogonalSecurityDistance = require('./OrthogonalSecurityDistance.js')
let CmdVelService = require('./CmdVelService.js')
let SetArmsEnabled = require('./SetArmsEnabled.js')
let GetRobotInfo = require('./GetRobotInfo.js')
let SetString = require('./SetString.js')

module.exports = {
  GetBodyROI: GetBodyROI,
  GetTruepose: GetTruepose,
  GetFacesROI: GetFacesROI,
  TangentialSecurityDistance: TangentialSecurityDistance,
  GetString: GetString,
  GetFloat: GetFloat,
  GetInstalledBehaviors: GetInstalledBehaviors,
  SetTransform: SetTransform,
  SetFloat: SetFloat,
  CmdPoseService: CmdPoseService,
  OrthogonalSecurityDistance: OrthogonalSecurityDistance,
  CmdVelService: CmdVelService,
  SetArmsEnabled: SetArmsEnabled,
  GetRobotInfo: GetRobotInfo,
  SetString: SetString,
};
