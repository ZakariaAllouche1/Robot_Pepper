
(cl:in-package :asdf)

(defsystem "snpi5-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "Image" :depends-on ("_package_Image"))
    (:file "_package_Image" :depends-on ("_package"))
  ))