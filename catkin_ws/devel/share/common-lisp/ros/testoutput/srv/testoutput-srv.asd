
(cl:in-package :asdf)

(defsystem "testoutput-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Pince" :depends-on ("_package_Pince"))
    (:file "_package_Pince" :depends-on ("_package"))
  ))