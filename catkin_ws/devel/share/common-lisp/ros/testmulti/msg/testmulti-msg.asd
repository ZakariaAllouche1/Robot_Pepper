
(cl:in-package :asdf)

(defsystem "testmulti-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "my_msg" :depends-on ("_package_my_msg"))
    (:file "_package_my_msg" :depends-on ("_package"))
  ))