
(cl:in-package :asdf)

(defsystem "maquette_arduino-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Serv_ard" :depends-on ("_package_Serv_ard"))
    (:file "_package_Serv_ard" :depends-on ("_package"))
    (:file "Serv_str" :depends-on ("_package_Serv_str"))
    (:file "_package_Serv_str" :depends-on ("_package"))
  ))