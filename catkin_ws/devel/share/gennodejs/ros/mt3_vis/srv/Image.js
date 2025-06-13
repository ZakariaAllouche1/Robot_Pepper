// Auto-generated. Do not edit!

// (in-package mt3_vis.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class ImageRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ImageRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ImageRequest
    let len;
    let data = new ImageRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'mt3_vis/ImageRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ImageRequest(null);
    return resolved;
    }
};

class ImageResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.nTarget_1 = null;
      this.pointTarget_1 = null;
      this.nTarget_2 = null;
      this.pointTarget_2 = null;
    }
    else {
      if (initObj.hasOwnProperty('nTarget_1')) {
        this.nTarget_1 = initObj.nTarget_1
      }
      else {
        this.nTarget_1 = 0;
      }
      if (initObj.hasOwnProperty('pointTarget_1')) {
        this.pointTarget_1 = initObj.pointTarget_1
      }
      else {
        this.pointTarget_1 = [];
      }
      if (initObj.hasOwnProperty('nTarget_2')) {
        this.nTarget_2 = initObj.nTarget_2
      }
      else {
        this.nTarget_2 = 0;
      }
      if (initObj.hasOwnProperty('pointTarget_2')) {
        this.pointTarget_2 = initObj.pointTarget_2
      }
      else {
        this.pointTarget_2 = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ImageResponse
    // Serialize message field [nTarget_1]
    bufferOffset = _serializer.uint32(obj.nTarget_1, buffer, bufferOffset);
    // Serialize message field [pointTarget_1]
    // Serialize the length for message field [pointTarget_1]
    bufferOffset = _serializer.uint32(obj.pointTarget_1.length, buffer, bufferOffset);
    obj.pointTarget_1.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [nTarget_2]
    bufferOffset = _serializer.uint32(obj.nTarget_2, buffer, bufferOffset);
    // Serialize message field [pointTarget_2]
    // Serialize the length for message field [pointTarget_2]
    bufferOffset = _serializer.uint32(obj.pointTarget_2.length, buffer, bufferOffset);
    obj.pointTarget_2.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ImageResponse
    let len;
    let data = new ImageResponse(null);
    // Deserialize message field [nTarget_1]
    data.nTarget_1 = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [pointTarget_1]
    // Deserialize array length for message field [pointTarget_1]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.pointTarget_1 = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.pointTarget_1[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [nTarget_2]
    data.nTarget_2 = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [pointTarget_2]
    // Deserialize array length for message field [pointTarget_2]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.pointTarget_2 = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.pointTarget_2[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 24 * object.pointTarget_1.length;
    length += 24 * object.pointTarget_2.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'mt3_vis/ImageResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f544d014c0d8841005a7554d29acdf3b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ImageResponse(null);
    if (msg.nTarget_1 !== undefined) {
      resolved.nTarget_1 = msg.nTarget_1;
    }
    else {
      resolved.nTarget_1 = 0
    }

    if (msg.pointTarget_1 !== undefined) {
      resolved.pointTarget_1 = new Array(msg.pointTarget_1.length);
      for (let i = 0; i < resolved.pointTarget_1.length; ++i) {
        resolved.pointTarget_1[i] = geometry_msgs.msg.Point.Resolve(msg.pointTarget_1[i]);
      }
    }
    else {
      resolved.pointTarget_1 = []
    }

    if (msg.nTarget_2 !== undefined) {
      resolved.nTarget_2 = msg.nTarget_2;
    }
    else {
      resolved.nTarget_2 = 0
    }

    if (msg.pointTarget_2 !== undefined) {
      resolved.pointTarget_2 = new Array(msg.pointTarget_2.length);
      for (let i = 0; i < resolved.pointTarget_2.length; ++i) {
        resolved.pointTarget_2[i] = geometry_msgs.msg.Point.Resolve(msg.pointTarget_2[i]);
      }
    }
    else {
      resolved.pointTarget_2 = []
    }

    return resolved;
    }
};

module.exports = {
  Request: ImageRequest,
  Response: ImageResponse,
  md5sum() { return 'f544d014c0d8841005a7554d29acdf3b'; },
  datatype() { return 'mt3_vis/Image'; }
};
