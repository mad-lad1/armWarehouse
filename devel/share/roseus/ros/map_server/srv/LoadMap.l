;; Auto-generated. Do not edit!


(when (boundp 'map_server::LoadMap)
  (if (not (find-package "MAP_SERVER"))
    (make-package "MAP_SERVER"))
  (shadow 'LoadMap (find-package "MAP_SERVER")))
(unless (find-package "MAP_SERVER::LOADMAP")
  (make-package "MAP_SERVER::LOADMAP"))
(unless (find-package "MAP_SERVER::LOADMAPREQUEST")
  (make-package "MAP_SERVER::LOADMAPREQUEST"))
(unless (find-package "MAP_SERVER::LOADMAPRESPONSE")
  (make-package "MAP_SERVER::LOADMAPRESPONSE"))

(in-package "ROS")





(defclass map_server::LoadMapRequest
  :super ros::object
  :slots (_map_path ))

(defmethod map_server::LoadMapRequest
  (:init
   (&key
    ((:map_path __map_path) "")
    )
   (send-super :init)
   (setq _map_path (string __map_path))
   self)
  (:map_path
   (&optional __map_path)
   (if __map_path (setq _map_path __map_path)) _map_path)
  (:serialization-length
   ()
   (+
    ;; string _map_path
    4 (length _map_path)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _map_path
       (write-long (length _map_path) s) (princ _map_path s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _map_path
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _map_path (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass map_server::LoadMapResponse
  :super ros::object
  :slots (_success ))

(defmethod map_server::LoadMapResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass map_server::LoadMap
  :super ros::object
  :slots ())

(setf (get map_server::LoadMap :md5sum-) "186a7ab57c33a3cd9a96fa8a2a713c2b")
(setf (get map_server::LoadMap :datatype-) "map_server/LoadMap")
(setf (get map_server::LoadMap :request) map_server::LoadMapRequest)
(setf (get map_server::LoadMap :response) map_server::LoadMapResponse)

(defmethod map_server::LoadMapRequest
  (:response () (instance map_server::LoadMapResponse :init)))

(setf (get map_server::LoadMapRequest :md5sum-) "186a7ab57c33a3cd9a96fa8a2a713c2b")
(setf (get map_server::LoadMapRequest :datatype-) "map_server/LoadMapRequest")
(setf (get map_server::LoadMapRequest :definition-)
      "string map_path
---
bool success
")

(setf (get map_server::LoadMapResponse :md5sum-) "186a7ab57c33a3cd9a96fa8a2a713c2b")
(setf (get map_server::LoadMapResponse :datatype-) "map_server/LoadMapResponse")
(setf (get map_server::LoadMapResponse :definition-)
      "string map_path
---
bool success
")



(provide :map_server/LoadMap "186a7ab57c33a3cd9a96fa8a2a713c2b")


