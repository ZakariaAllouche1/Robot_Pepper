
(cl:in-package :asdf)

(defsystem "dsr_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Robotiq2FClose" :depends-on ("_package_Robotiq2FClose"))
    (:file "_package_Robotiq2FClose" :depends-on ("_package"))
    (:file "Robotiq2FMove" :depends-on ("_package_Robotiq2FMove"))
    (:file "_package_Robotiq2FMove" :depends-on ("_package"))
    (:file "Robotiq2FOpen" :depends-on ("_package_Robotiq2FOpen"))
    (:file "_package_Robotiq2FOpen" :depends-on ("_package"))
    (:file "SerialSendData" :depends-on ("_package_SerialSendData"))
    (:file "_package_SerialSendData" :depends-on ("_package"))
  ))