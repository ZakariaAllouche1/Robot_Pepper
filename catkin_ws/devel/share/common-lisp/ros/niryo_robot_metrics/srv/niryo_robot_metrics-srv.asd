
(cl:in-package :asdf)

(defsystem "niryo_robot_metrics-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :niryo_robot_metrics-msg
)
  :components ((:file "_package")
    (:file "GetMetric" :depends-on ("_package_GetMetric"))
    (:file "_package_GetMetric" :depends-on ("_package"))
  ))