
(cl:in-package :asdf)

(defsystem "snpi5_doosan-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Goto" :depends-on ("_package_Goto"))
    (:file "_package_Goto" :depends-on ("_package"))
    (:file "Home" :depends-on ("_package_Home"))
    (:file "_package_Home" :depends-on ("_package"))
    (:file "Prise" :depends-on ("_package_Prise"))
    (:file "_package_Prise" :depends-on ("_package"))
    (:file "Repos" :depends-on ("_package_Repos"))
    (:file "_package_Repos" :depends-on ("_package"))
  ))