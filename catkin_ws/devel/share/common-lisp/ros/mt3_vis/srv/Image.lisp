; Auto-generated. Do not edit!


(cl:in-package mt3_vis-srv)


;//! \htmlinclude Image-request.msg.html

(cl:defclass <Image-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Image-request (<Image-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Image-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Image-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mt3_vis-srv:<Image-request> is deprecated: use mt3_vis-srv:Image-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Image-request>) ostream)
  "Serializes a message object of type '<Image-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Image-request>) istream)
  "Deserializes a message object of type '<Image-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Image-request>)))
  "Returns string type for a service object of type '<Image-request>"
  "mt3_vis/ImageRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Image-request)))
  "Returns string type for a service object of type 'Image-request"
  "mt3_vis/ImageRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Image-request>)))
  "Returns md5sum for a message object of type '<Image-request>"
  "f544d014c0d8841005a7554d29acdf3b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Image-request)))
  "Returns md5sum for a message object of type 'Image-request"
  "f544d014c0d8841005a7554d29acdf3b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Image-request>)))
  "Returns full string definition for message of type '<Image-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Image-request)))
  "Returns full string definition for message of type 'Image-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Image-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Image-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Image-request
))
;//! \htmlinclude Image-response.msg.html

(cl:defclass <Image-response> (roslisp-msg-protocol:ros-message)
  ((nTarget_1
    :reader nTarget_1
    :initarg :nTarget_1
    :type cl:integer
    :initform 0)
   (pointTarget_1
    :reader pointTarget_1
    :initarg :pointTarget_1
    :type (cl:vector geometry_msgs-msg:Point)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Point :initial-element (cl:make-instance 'geometry_msgs-msg:Point)))
   (nTarget_2
    :reader nTarget_2
    :initarg :nTarget_2
    :type cl:integer
    :initform 0)
   (pointTarget_2
    :reader pointTarget_2
    :initarg :pointTarget_2
    :type (cl:vector geometry_msgs-msg:Point)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Point :initial-element (cl:make-instance 'geometry_msgs-msg:Point))))
)

(cl:defclass Image-response (<Image-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Image-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Image-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mt3_vis-srv:<Image-response> is deprecated: use mt3_vis-srv:Image-response instead.")))

(cl:ensure-generic-function 'nTarget_1-val :lambda-list '(m))
(cl:defmethod nTarget_1-val ((m <Image-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mt3_vis-srv:nTarget_1-val is deprecated.  Use mt3_vis-srv:nTarget_1 instead.")
  (nTarget_1 m))

(cl:ensure-generic-function 'pointTarget_1-val :lambda-list '(m))
(cl:defmethod pointTarget_1-val ((m <Image-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mt3_vis-srv:pointTarget_1-val is deprecated.  Use mt3_vis-srv:pointTarget_1 instead.")
  (pointTarget_1 m))

(cl:ensure-generic-function 'nTarget_2-val :lambda-list '(m))
(cl:defmethod nTarget_2-val ((m <Image-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mt3_vis-srv:nTarget_2-val is deprecated.  Use mt3_vis-srv:nTarget_2 instead.")
  (nTarget_2 m))

(cl:ensure-generic-function 'pointTarget_2-val :lambda-list '(m))
(cl:defmethod pointTarget_2-val ((m <Image-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mt3_vis-srv:pointTarget_2-val is deprecated.  Use mt3_vis-srv:pointTarget_2 instead.")
  (pointTarget_2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Image-response>) ostream)
  "Serializes a message object of type '<Image-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'nTarget_1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'nTarget_1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'nTarget_1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'nTarget_1)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'pointTarget_1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'pointTarget_1))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'nTarget_2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'nTarget_2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'nTarget_2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'nTarget_2)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'pointTarget_2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'pointTarget_2))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Image-response>) istream)
  "Deserializes a message object of type '<Image-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'nTarget_1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'nTarget_1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'nTarget_1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'nTarget_1)) (cl:read-byte istream))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'pointTarget_1) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'pointTarget_1)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Point))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'nTarget_2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'nTarget_2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'nTarget_2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'nTarget_2)) (cl:read-byte istream))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'pointTarget_2) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'pointTarget_2)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Point))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Image-response>)))
  "Returns string type for a service object of type '<Image-response>"
  "mt3_vis/ImageResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Image-response)))
  "Returns string type for a service object of type 'Image-response"
  "mt3_vis/ImageResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Image-response>)))
  "Returns md5sum for a message object of type '<Image-response>"
  "f544d014c0d8841005a7554d29acdf3b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Image-response)))
  "Returns md5sum for a message object of type 'Image-response"
  "f544d014c0d8841005a7554d29acdf3b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Image-response>)))
  "Returns full string definition for message of type '<Image-response>"
  (cl:format cl:nil "uint32 nTarget_1~%geometry_msgs/Point[] pointTarget_1~%uint32 nTarget_2~%geometry_msgs/Point[] pointTarget_2~%~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Image-response)))
  "Returns full string definition for message of type 'Image-response"
  (cl:format cl:nil "uint32 nTarget_1~%geometry_msgs/Point[] pointTarget_1~%uint32 nTarget_2~%geometry_msgs/Point[] pointTarget_2~%~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Image-response>))
  (cl:+ 0
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'pointTarget_1) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'pointTarget_2) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Image-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Image-response
    (cl:cons ':nTarget_1 (nTarget_1 msg))
    (cl:cons ':pointTarget_1 (pointTarget_1 msg))
    (cl:cons ':nTarget_2 (nTarget_2 msg))
    (cl:cons ':pointTarget_2 (pointTarget_2 msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Image)))
  'Image-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Image)))
  'Image-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Image)))
  "Returns string type for a service object of type '<Image>"
  "mt3_vis/Image")