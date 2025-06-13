
(cl:in-package :asdf)

(defsystem "dsr_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "JogMultiAxis" :depends-on ("_package_JogMultiAxis"))
    (:file "_package_JogMultiAxis" :depends-on ("_package"))
    (:file "LogAlarm" :depends-on ("_package_LogAlarm"))
    (:file "_package_LogAlarm" :depends-on ("_package"))
    (:file "ModbusState" :depends-on ("_package_ModbusState"))
    (:file "_package_ModbusState" :depends-on ("_package"))
    (:file "RobotError" :depends-on ("_package_RobotError"))
    (:file "_package_RobotError" :depends-on ("_package"))
    (:file "RobotState" :depends-on ("_package_RobotState"))
    (:file "_package_RobotState" :depends-on ("_package"))
    (:file "RobotStop" :depends-on ("_package_RobotStop"))
    (:file "_package_RobotStop" :depends-on ("_package"))
  ))