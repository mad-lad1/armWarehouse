# Install script for directory: /home/user/catkin_ws/src/aws-robomaker-small-warehouse-world

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/user/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/user/catkin_ws/build/aws-robomaker-small-warehouse-world/catkin_generated/installspace/aws_robomaker_small_warehouse_world.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/aws_robomaker_small_warehouse_world/cmake" TYPE FILE FILES
    "/home/user/catkin_ws/build/aws-robomaker-small-warehouse-world/catkin_generated/installspace/aws_robomaker_small_warehouse_worldConfig.cmake"
    "/home/user/catkin_ws/build/aws-robomaker-small-warehouse-world/catkin_generated/installspace/aws_robomaker_small_warehouse_worldConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/aws_robomaker_small_warehouse_world" TYPE FILE FILES "/home/user/catkin_ws/src/aws-robomaker-small-warehouse-world/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/aws_robomaker_small_warehouse_world" TYPE DIRECTORY FILES
    "/home/user/catkin_ws/src/aws-robomaker-small-warehouse-world/launch"
    "/home/user/catkin_ws/src/aws-robomaker-small-warehouse-world/models"
    "/home/user/catkin_ws/src/aws-robomaker-small-warehouse-world/worlds"
    "/home/user/catkin_ws/src/aws-robomaker-small-warehouse-world/maps"
    "/home/user/catkin_ws/src/aws-robomaker-small-warehouse-world/rviz"
    )
endif()

