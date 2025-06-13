
(cl:in-package :asdf)

(defsystem "bras_redondant-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "Serv_position" :depends-on ("_package_Serv_position"))
    (:file "_package_Serv_position" :depends-on ("_package"))
  ))