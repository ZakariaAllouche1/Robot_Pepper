; Auto-generated. Do not edit!


(cl:in-package testpython-srv)


;//! \htmlinclude Goto-request.msg.html

(cl:defclass <Goto-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0))
)

(cl:defclass Goto-request (<Goto-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Goto-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Goto-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name testpython-srv:<Goto-request> is deprecated: use testpython-srv:Goto-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <Goto-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader testpython-srv:x-val is deprecated.  Use testpython-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <Goto-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader testpython-srv:y-val is deprecated.  Use testpython-srv:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Goto-request>) ostream)
  "Serializes a message object of type '<Goto-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Goto-request>) istream)
  "Deserializes a message object of type '<Goto-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Goto-request>)))
  "Returns string type for a service object of type '<Goto-request>"
  "testpython/GotoRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Goto-request)))
  "Returns string type for a service object of type 'Goto-request"
  "testpython/GotoRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Goto-request>)))
  "Returns md5sum for a message object of type '<Goto-request>"
  "363aeec325ec01e00bcc24a96476d819")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Goto-request)))
  "Returns md5sum for a message object of type 'Goto-request"
  "363aeec325ec01e00bcc24a96476d819")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Goto-request>)))
  "Returns full string definition for message of type '<Goto-request>"
  (cl:format cl:nil "float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Goto-request)))
  "Returns full string definition for message of type 'Goto-request"
  (cl:format cl:nil "float64 x~%float64 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Goto-request>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Goto-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Goto-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))
;//! \htmlinclude Goto-response.msg.html

(cl:defclass <Goto-response> (roslisp-msg-protocol:ros-message)
  ((res
    :reader res
    :initarg :res
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Goto-response (<Goto-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Goto-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Goto-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name testpython-srv:<Goto-response> is deprecated: use testpython-srv:Goto-response instead.")))

(cl:ensure-generic-function 'res-val :lambda-list '(m))
(cl:defmethod res-val ((m <Goto-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader testpython-srv:res-val is deprecated.  Use testpython-srv:res instead.")
  (res m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Goto-response>) ostream)
  "Serializes a message object of type '<Goto-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'res) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Goto-response>) istream)
  "Deserializes a message object of type '<Goto-response>"
    (cl:setf (cl:slot-value msg 'res) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Goto-response>)))
  "Returns string type for a service object of type '<Goto-response>"
  "testpython/GotoResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Goto-response)))
  "Returns string type for a service object of type 'Goto-response"
  "testpython/GotoResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Goto-response>)))
  "Returns md5sum for a message object of type '<Goto-response>"
  "363aeec325ec01e00bcc24a96476d819")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Goto-response)))
  "Returns md5sum for a message object of type 'Goto-response"
  "363aeec325ec01e00bcc24a96476d819")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Goto-response>)))
  "Returns full string definition for message of type '<Goto-response>"
  (cl:format cl:nil "bool res~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Goto-response)))
  "Returns full string definition for message of type 'Goto-response"
  (cl:format cl:nil "bool res~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Goto-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Goto-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Goto-response
    (cl:cons ':res (res msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Goto)))
  'Goto-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Goto)))
  'Goto-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Goto)))
  "Returns string type for a service object of type '<Goto>"
  "testpython/Goto")