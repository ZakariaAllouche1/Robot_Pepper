; Auto-generated. Do not edit!


(cl:in-package maquette_arduino-srv)


;//! \htmlinclude serv_ard-request.msg.html

(cl:defclass <serv_ard-request> (roslisp-msg-protocol:ros-message)
  ((pos
    :reader pos
    :initarg :pos
    :type cl:fixnum
    :initform 0))
)

(cl:defclass serv_ard-request (<serv_ard-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <serv_ard-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'serv_ard-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name maquette_arduino-srv:<serv_ard-request> is deprecated: use maquette_arduino-srv:serv_ard-request instead.")))

(cl:ensure-generic-function 'pos-val :lambda-list '(m))
(cl:defmethod pos-val ((m <serv_ard-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader maquette_arduino-srv:pos-val is deprecated.  Use maquette_arduino-srv:pos instead.")
  (pos m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <serv_ard-request>) ostream)
  "Serializes a message object of type '<serv_ard-request>"
  (cl:let* ((signed (cl:slot-value msg 'pos)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <serv_ard-request>) istream)
  "Deserializes a message object of type '<serv_ard-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pos) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<serv_ard-request>)))
  "Returns string type for a service object of type '<serv_ard-request>"
  "maquette_arduino/serv_ardRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'serv_ard-request)))
  "Returns string type for a service object of type 'serv_ard-request"
  "maquette_arduino/serv_ardRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<serv_ard-request>)))
  "Returns md5sum for a message object of type '<serv_ard-request>"
  "25fc7c55b8d1a528cd733083f4c845ff")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'serv_ard-request)))
  "Returns md5sum for a message object of type 'serv_ard-request"
  "25fc7c55b8d1a528cd733083f4c845ff")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<serv_ard-request>)))
  "Returns full string definition for message of type '<serv_ard-request>"
  (cl:format cl:nil "int16 pos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'serv_ard-request)))
  "Returns full string definition for message of type 'serv_ard-request"
  (cl:format cl:nil "int16 pos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <serv_ard-request>))
  (cl:+ 0
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <serv_ard-request>))
  "Converts a ROS message object to a list"
  (cl:list 'serv_ard-request
    (cl:cons ':pos (pos msg))
))
;//! \htmlinclude serv_ard-response.msg.html

(cl:defclass <serv_ard-response> (roslisp-msg-protocol:ros-message)
  ((res
    :reader res
    :initarg :res
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass serv_ard-response (<serv_ard-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <serv_ard-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'serv_ard-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name maquette_arduino-srv:<serv_ard-response> is deprecated: use maquette_arduino-srv:serv_ard-response instead.")))

(cl:ensure-generic-function 'res-val :lambda-list '(m))
(cl:defmethod res-val ((m <serv_ard-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader maquette_arduino-srv:res-val is deprecated.  Use maquette_arduino-srv:res instead.")
  (res m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <serv_ard-response>) ostream)
  "Serializes a message object of type '<serv_ard-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'res) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <serv_ard-response>) istream)
  "Deserializes a message object of type '<serv_ard-response>"
    (cl:setf (cl:slot-value msg 'res) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<serv_ard-response>)))
  "Returns string type for a service object of type '<serv_ard-response>"
  "maquette_arduino/serv_ardResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'serv_ard-response)))
  "Returns string type for a service object of type 'serv_ard-response"
  "maquette_arduino/serv_ardResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<serv_ard-response>)))
  "Returns md5sum for a message object of type '<serv_ard-response>"
  "25fc7c55b8d1a528cd733083f4c845ff")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'serv_ard-response)))
  "Returns md5sum for a message object of type 'serv_ard-response"
  "25fc7c55b8d1a528cd733083f4c845ff")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<serv_ard-response>)))
  "Returns full string definition for message of type '<serv_ard-response>"
  (cl:format cl:nil "bool res~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'serv_ard-response)))
  "Returns full string definition for message of type 'serv_ard-response"
  (cl:format cl:nil "bool res~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <serv_ard-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <serv_ard-response>))
  "Converts a ROS message object to a list"
  (cl:list 'serv_ard-response
    (cl:cons ':res (res msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'serv_ard)))
  'serv_ard-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'serv_ard)))
  'serv_ard-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'serv_ard)))
  "Returns string type for a service object of type '<serv_ard>"
  "maquette_arduino/serv_ard")