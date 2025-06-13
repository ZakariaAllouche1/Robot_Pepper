
(cl:in-package :asdf)

(defsystem "bras-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Trajectoire" :depends-on ("_package_Trajectoire"))
    (:file "_package_Trajectoire" :depends-on ("_package"))
  ))