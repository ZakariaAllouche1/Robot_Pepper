;; Auto-generated. Do not edit!


(when (boundp 'testpython::Home)
  (if (not (find-package "TESTPYTHON"))
    (make-package "TESTPYTHON"))
  (shadow 'Home (find-package "TESTPYTHON")))
(unless (find-package "TESTPYTHON::HOME")
  (make-package "TESTPYTHON::HOME"))
(unless (find-package "TESTPYTHON::HOMEREQUEST")
  (make-package "TESTPYTHON::HOMEREQUEST"))
(unless (find-package "TESTPYTHON::HOMERESPONSE")
  (make-package "TESTPYTHON::HOMERESPONSE"))

(in-package "ROS")





(defclass testpython::HomeRequest
  :super ros::object
  :slots ())

(defmethod testpython::HomeRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass testpython::HomeResponse
  :super ros::object
  :slots (_res ))

(defmethod testpython::HomeResponse
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

(defclass testpython::Home
  :super ros::object
  :slots ())

(setf (get testpython::Home :md5sum-) "e27848a10f8e7e4030443887dfea101b")
(setf (get testpython::Home :datatype-) "testpython/Home")
(setf (get testpython::Home :request) testpython::HomeRequest)
(setf (get testpython::Home :response) testpython::HomeResponse)

(defmethod testpython::HomeRequest
  (:response () (instance testpython::HomeResponse :init)))

(setf (get testpython::HomeRequest :md5sum-) "e27848a10f8e7e4030443887dfea101b")
(setf (get testpython::HomeRequest :datatype-) "testpython/HomeRequest")
(setf (get testpython::HomeRequest :definition-)
      "---
bool res

")

(setf (get testpython::HomeResponse :md5sum-) "e27848a10f8e7e4030443887dfea101b")
(setf (get testpython::HomeResponse :datatype-) "testpython/HomeResponse")
(setf (get testpython::HomeResponse :definition-)
      "---
bool res

")



(provide :testpython/Home "e27848a10f8e7e4030443887dfea101b")


