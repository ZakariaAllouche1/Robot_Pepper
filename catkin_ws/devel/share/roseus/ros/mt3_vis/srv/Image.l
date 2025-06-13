;; Auto-generated. Do not edit!


(when (boundp 'mt3_vis::Image)
  (if (not (find-package "MT3_VIS"))
    (make-package "MT3_VIS"))
  (shadow 'Image (find-package "MT3_VIS")))
(unless (find-package "MT3_VIS::IMAGE")
  (make-package "MT3_VIS::IMAGE"))
(unless (find-package "MT3_VIS::IMAGEREQUEST")
  (make-package "MT3_VIS::IMAGEREQUEST"))
(unless (find-package "MT3_VIS::IMAGERESPONSE")
  (make-package "MT3_VIS::IMAGERESPONSE"))

(in-package "ROS")



(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass mt3_vis::ImageRequest
  :super ros::object
  :slots ())

(defmethod mt3_vis::ImageRequest
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

(defclass mt3_vis::ImageResponse
  :super ros::object
  :slots (_nTarget_1 _pointTarget_1 _nTarget_2 _pointTarget_2 ))

(defmethod mt3_vis::ImageResponse
  (:init
   (&key
    ((:nTarget_1 __nTarget_1) 0)
    ((:pointTarget_1 __pointTarget_1) ())
    ((:nTarget_2 __nTarget_2) 0)
    ((:pointTarget_2 __pointTarget_2) ())
    )
   (send-super :init)
   (setq _nTarget_1 (round __nTarget_1))
   (setq _pointTarget_1 __pointTarget_1)
   (setq _nTarget_2 (round __nTarget_2))
   (setq _pointTarget_2 __pointTarget_2)
   self)
  (:nTarget_1
   (&optional __nTarget_1)
   (if __nTarget_1 (setq _nTarget_1 __nTarget_1)) _nTarget_1)
  (:pointTarget_1
   (&rest __pointTarget_1)
   (if (keywordp (car __pointTarget_1))
       (send* _pointTarget_1 __pointTarget_1)
     (progn
       (if __pointTarget_1 (setq _pointTarget_1 (car __pointTarget_1)))
       _pointTarget_1)))
  (:nTarget_2
   (&optional __nTarget_2)
   (if __nTarget_2 (setq _nTarget_2 __nTarget_2)) _nTarget_2)
  (:pointTarget_2
   (&rest __pointTarget_2)
   (if (keywordp (car __pointTarget_2))
       (send* _pointTarget_2 __pointTarget_2)
     (progn
       (if __pointTarget_2 (setq _pointTarget_2 (car __pointTarget_2)))
       _pointTarget_2)))
  (:serialization-length
   ()
   (+
    ;; uint32 _nTarget_1
    4
    ;; geometry_msgs/Point[] _pointTarget_1
    (apply #'+ (send-all _pointTarget_1 :serialization-length)) 4
    ;; uint32 _nTarget_2
    4
    ;; geometry_msgs/Point[] _pointTarget_2
    (apply #'+ (send-all _pointTarget_2 :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _nTarget_1
       (write-long _nTarget_1 s)
     ;; geometry_msgs/Point[] _pointTarget_1
     (write-long (length _pointTarget_1) s)
     (dolist (elem _pointTarget_1)
       (send elem :serialize s)
       )
     ;; uint32 _nTarget_2
       (write-long _nTarget_2 s)
     ;; geometry_msgs/Point[] _pointTarget_2
     (write-long (length _pointTarget_2) s)
     (dolist (elem _pointTarget_2)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _nTarget_1
     (setq _nTarget_1 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; geometry_msgs/Point[] _pointTarget_1
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pointTarget_1 (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _pointTarget_1)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; uint32 _nTarget_2
     (setq _nTarget_2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; geometry_msgs/Point[] _pointTarget_2
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pointTarget_2 (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _pointTarget_2)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(defclass mt3_vis::Image
  :super ros::object
  :slots ())

(setf (get mt3_vis::Image :md5sum-) "f544d014c0d8841005a7554d29acdf3b")
(setf (get mt3_vis::Image :datatype-) "mt3_vis/Image")
(setf (get mt3_vis::Image :request) mt3_vis::ImageRequest)
(setf (get mt3_vis::Image :response) mt3_vis::ImageResponse)

(defmethod mt3_vis::ImageRequest
  (:response () (instance mt3_vis::ImageResponse :init)))

(setf (get mt3_vis::ImageRequest :md5sum-) "f544d014c0d8841005a7554d29acdf3b")
(setf (get mt3_vis::ImageRequest :datatype-) "mt3_vis/ImageRequest")
(setf (get mt3_vis::ImageRequest :definition-)
      "---
uint32 nTarget_1
geometry_msgs/Point[] pointTarget_1
uint32 nTarget_2
geometry_msgs/Point[] pointTarget_2


================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
")

(setf (get mt3_vis::ImageResponse :md5sum-) "f544d014c0d8841005a7554d29acdf3b")
(setf (get mt3_vis::ImageResponse :datatype-) "mt3_vis/ImageResponse")
(setf (get mt3_vis::ImageResponse :definition-)
      "---
uint32 nTarget_1
geometry_msgs/Point[] pointTarget_1
uint32 nTarget_2
geometry_msgs/Point[] pointTarget_2


================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
")



(provide :mt3_vis/Image "f544d014c0d8841005a7554d29acdf3b")


