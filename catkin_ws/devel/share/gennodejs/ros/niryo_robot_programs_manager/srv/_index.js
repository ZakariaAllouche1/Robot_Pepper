
"use strict";

let GetProgramList = require('./GetProgramList.js')
let ExecuteProgram = require('./ExecuteProgram.js')
let SetProgramAutorun = require('./SetProgramAutorun.js')
let GetProgramAutorunInfos = require('./GetProgramAutorunInfos.js')
let GetProgram = require('./GetProgram.js')
let ManageProgram = require('./ManageProgram.js')

module.exports = {
  GetProgramList: GetProgramList,
  ExecuteProgram: ExecuteProgram,
  SetProgramAutorun: SetProgramAutorun,
  GetProgramAutorunInfos: GetProgramAutorunInfos,
  GetProgram: GetProgram,
  ManageProgram: ManageProgram,
};
