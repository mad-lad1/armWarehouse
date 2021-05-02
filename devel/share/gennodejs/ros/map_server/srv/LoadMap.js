// Auto-generated. Do not edit!

// (in-package map_server.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class LoadMapRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.map_path = null;
    }
    else {
      if (initObj.hasOwnProperty('map_path')) {
        this.map_path = initObj.map_path
      }
      else {
        this.map_path = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LoadMapRequest
    // Serialize message field [map_path]
    bufferOffset = _serializer.string(obj.map_path, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LoadMapRequest
    let len;
    let data = new LoadMapRequest(null);
    // Deserialize message field [map_path]
    data.map_path = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.map_path.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'map_server/LoadMapRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '87ded74cc4428020b667445286a08b63';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string map_path
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LoadMapRequest(null);
    if (msg.map_path !== undefined) {
      resolved.map_path = msg.map_path;
    }
    else {
      resolved.map_path = ''
    }

    return resolved;
    }
};

class LoadMapResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LoadMapResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LoadMapResponse
    let len;
    let data = new LoadMapResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'map_server/LoadMapResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LoadMapResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: LoadMapRequest,
  Response: LoadMapResponse,
  md5sum() { return '186a7ab57c33a3cd9a96fa8a2a713c2b'; },
  datatype() { return 'map_server/LoadMap'; }
};
