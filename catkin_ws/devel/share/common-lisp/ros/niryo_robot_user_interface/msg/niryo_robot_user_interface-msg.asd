
(cl:in-package :asdf)

(defsystem "niryo_robot_user_interface-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ConnectionState" :depends-on ("_package_ConnectionState"))
    (:file "_package_ConnectionState" :depends-on ("_package"))
  ))