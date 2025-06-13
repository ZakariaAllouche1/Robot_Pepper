
(cl:in-package :asdf)

(defsystem "niryo_robot_metrics-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Metric" :depends-on ("_package_Metric"))
    (:file "_package_Metric" :depends-on ("_package"))
  ))