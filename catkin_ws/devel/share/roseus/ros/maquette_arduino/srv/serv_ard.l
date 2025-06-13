;; Auto-generated. Do not edit!


(when (boundp 'maquette_arduino::serv_ard)
  (if (not (find-package "MAQUETTE_ARDUINO"))
    (make-package "MAQUETTE_ARDUINO"))
  (shadow 'serv_ard (find-package "MAQUETTE_ARDUINO")))
(unless (find-package "MAQUETTE_ARDUINO::SERV_ARD")
  (make-package "MAQUETTE_ARDUINO::SERV_ARD"))
(unless (find-package "MAQUETTE_ARDUINO::SERV_ARDREQUEST")
  (make-package "MAQUETTE_ARDUINO::SERV_ARDREQUEST"))
(unless (find-package "MAQUETTE_ARDUINO::SERV_ARDRESPONSE")
  (make-package "MAQUETTE_ARDUINO::SERV_ARDRESPONSE"))

(in-package "ROS")





(defclass maquette_arduino::serv_ardRequest
  :super ros::object
  :slots (_pos ))

(defmethod maquette_arduino::serv_ardRequest
  (:init
   (&key
    ((:pos __pos) 0)
    )
   (send-super :init)
   (setq _pos (round __pos))
   self)
  (:pos
   (&optional __pos)
   (if __pos (setq _pos __pos)) _pos)
  (:serialization-length
   ()
   (+
    ;; int16 _pos
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _pos
       (write-word _pos s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _pos
     (setq _pos (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(defclass maquette_arduino::serv_ardResponse
  :super ros::object
  :slots (_res ))

(defmethod maquette_arduino::serv_ardResponse
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

(defclass maquette_arduino::serv_ard
  :super ros::object
  :slots ())

(setf (get maquette_arduino::serv_ard :md5sum-) "25fc7c55b8d1a528cd733083f4c845ff")
(setf (get maquette_arduino::serv_ard :datatype-) "maquette_arduino/serv_ard")
(setf (get maquette_arduino::serv_ard :request) maquette_arduino::serv_ardRequest)
(setf (get maquette_arduino::serv_ard :response) maquette_arduino::serv_ardResponse)

(defmethod maquette_arduino::serv_ardRequest
  (:response () (instance maquette_arduino::serv_ardResponse :init)))

(setf (get maquette_arduino::serv_ardRequest :md5sum-) "25fc7c55b8d1a528cd733083f4c845ff")
(setf (get maquette_arduino::serv_ardRequest :datatype-) "maquette_arduino/serv_ardRequest")
(setf (get maquette_arduino::serv_ardRequest :definition-)
      "int16 pos
---
bool res

")

(setf (get maquette_arduino::serv_ardResponse :md5sum-) "25fc7c55b8d1a528cd733083f4c845ff")
(setf (get maquette_arduino::serv_ardResponse :datatype-) "maquette_arduino/serv_ardResponse")
(setf (get maquette_arduino::serv_ardResponse :definition-)
      "int16 pos
---
bool res

")



(provide :maquette_arduino/serv_ard "25fc7c55b8d1a528cd733083f4c845ff")


