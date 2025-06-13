
(cl:in-package :asdf)

(defsystem "testpython-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AddTwoInts" :depends-on ("_package_AddTwoInts"))
    (:file "_package_AddTwoInts" :depends-on ("_package"))
    (:file "Goto" :depends-on ("_package_Goto"))
    (:file "_package_Goto" :depends-on ("_package"))
    (:file "Home" :depends-on ("_package_Home"))
    (:file "_package_Home" :depends-on ("_package"))
  ))