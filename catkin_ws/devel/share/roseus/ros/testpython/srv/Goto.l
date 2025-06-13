;; Auto-generated. Do not edit!


(when (boundp 'testpython::Goto)
  (if (not (find-package "TESTPYTHON"))
    (make-package "TESTPYTHON"))
  (shadow 'Goto (find-package "TESTPYTHON")))
(unless (find-package "TESTPYTHON::GOTO")
  (make-package "TESTPYTHON::GOTO"))
(unless (find-package "TESTPYTHON::GOTOREQUEST")
  (make-package "TESTPYTHON::GOTOREQUEST"))
(unless (find-package "TESTPYTHON::GOTORESPONSE")
  (make-package "TESTPYTHON::GOTORESPONSE"))

(in-package "ROS")





(defclass testpython::GotoRequest
  :super ros::object
  :slots (_x _y ))

(defmethod testpython::GotoRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass testpython::GotoResponse
  :super ros::object
  :slots (_res ))

(defmethod testpython::GotoResponse
  (:init
   (&key
    ((:res __res) nil)
    )
   (send-super :init)
   (setq _res __res)
   self)
  (:res
   (&optional (__res :null))
   (if (not (eq __res :null)) (setq _res __res)) _res)
  (:serialization-length
   ()
   (+
    ;; bool _res
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _res
       (if _res (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _res
     (setq _res (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass testpython::Goto
  :super ros::object
  :slots ())

(setf (get testpython::Goto :md5sum-) "363aeec325ec01e00bcc24a96476d819")
(setf (get testpython::Goto :datatype-) "testpython/Goto")
(setf (get testpython::Goto :request) testpython::GotoRequest)
(setf (get testpython::Goto :response) testpython::GotoResponse)

(defmethod testpython::GotoRequest
  (:response () (instance testpython::GotoResponse :init)))

(setf (get testpython::GotoRequest :md5sum-) "363aeec325ec01e00bcc24a96476d819")
(setf (get testpython::GotoRequest :datatype-) "testpython/GotoRequest")
(setf (get testpython::GotoRequest :definition-)
      "float64 x
float64 y
---
bool res

")

(setf (get testpython::GotoResponse :md5sum-) "363aeec325ec01e00bcc24a96476d819")
(setf (get testpython::GotoResponse :datatype-) "testpython/GotoResponse")
(setf (get testpython::GotoResponse :definition-)
      "float64 x
float64 y
---
bool res

")



(provide :testpython/Goto "363aeec325ec01e00bcc24a96476d819")


