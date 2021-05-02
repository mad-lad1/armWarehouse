// Generated by gencpp from file map_server/LoadMap.msg
// DO NOT EDIT!


#ifndef MAP_SERVER_MESSAGE_LOADMAP_H
#define MAP_SERVER_MESSAGE_LOADMAP_H

#include <ros/service_traits.h>


#include <map_server/LoadMapRequest.h>
#include <map_server/LoadMapResponse.h>


namespace map_server
{

struct LoadMap
{

typedef LoadMapRequest Request;
typedef LoadMapResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct LoadMap
} // namespace map_server


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::map_server::LoadMap > {
  static const char* value()
  {
    return "186a7ab57c33a3cd9a96fa8a2a713c2b";
  }

  static const char* value(const ::map_server::LoadMap&) { return value(); }
};

template<>
struct DataType< ::map_server::LoadMap > {
  static const char* value()
  {
    return "map_server/LoadMap";
  }

  static const char* value(const ::map_server::LoadMap&) { return value(); }
};


// service_traits::MD5Sum< ::map_server::LoadMapRequest> should match 
// service_traits::MD5Sum< ::map_server::LoadMap > 
template<>
struct MD5Sum< ::map_server::LoadMapRequest>
{
  static const char* value()
  {
    return MD5Sum< ::map_server::LoadMap >::value();
  }
  static const char* value(const ::map_server::LoadMapRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::map_server::LoadMapRequest> should match 
// service_traits::DataType< ::map_server::LoadMap > 
template<>
struct DataType< ::map_server::LoadMapRequest>
{
  static const char* value()
  {
    return DataType< ::map_server::LoadMap >::value();
  }
  static const char* value(const ::map_server::LoadMapRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::map_server::LoadMapResponse> should match 
// service_traits::MD5Sum< ::map_server::LoadMap > 
template<>
struct MD5Sum< ::map_server::LoadMapResponse>
{
  static const char* value()
  {
    return MD5Sum< ::map_server::LoadMap >::value();
  }
  static const char* value(const ::map_server::LoadMapResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::map_server::LoadMapResponse> should match 
// service_traits::DataType< ::map_server::LoadMap > 
template<>
struct DataType< ::map_server::LoadMapResponse>
{
  static const char* value()
  {
    return DataType< ::map_server::LoadMap >::value();
  }
  static const char* value(const ::map_server::LoadMapResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MAP_SERVER_MESSAGE_LOADMAP_H