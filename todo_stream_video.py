# import cv2
# import gi
# import numpy as np

# gi.require_version("Gst", "1.0")
# gi.require_version("GstRtspServer", "1.0")
# from gi.repository import Gst, GstRtspServer, GObject

# class VideoAppSrc(GstRtspServer.RTSPMediaFactory):
#     def __init__(self, **properties):
#         super(VideoAppSrc, self).__init__(**properties)
#         # self.cap = 
#         self.cap = ""
#         self.number_frames = 0
#         # self.duration = 1.0 / self.cap.get(cv2.CAP_PROP_FPS) * Gst.SECOND
#         self.duration = 1.0
#         self.launch_string = (
#             "appsrc name=source is-live=true format=GST_FORMAT_TIME "
#             "caps=video/x-raw,width=640,height=480,framerate=30/1 ! "
#             "videoconvert ! video/x-raw,format=I420 ! x264enc tune=zerolatency speed-preset=superfast ! "
#             "rtph264pay config-interval=1 pt=96 ! "
#             "udpsink host=127.0.0.1 port=5000"
#         )

#     def on_need_data(self, src, length):
#         # ret, frame = self.cap.read()
#         frame = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)
#         # if not ret:
#         #     return

#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         frame = cv2.resize(frame, (640, 480))
#         data = frame.tostring()

#         buf = Gst.Buffer.new_allocate(None, len(data), None)
#         buf.fill(0, data)

#         buf.duration = self.duration
#         timestamp = self.number_frames * self.duration
#         buf.pts = buf.dts = int(timestamp)
#         buf.offset = timestamp

#         self.number_frames += 1
#         retval = src.emit("push-buffer", buf)

#         if retval != Gst.FlowReturn.OK:
#             print("Push buffer error")

#     def do_create_element(self, url):
#         return Gst.parse_launch(self.launch_string)

#     def do_configure(self, rtsp_media):
#         self.number_frames = 0
#         appsrc = rtsp_media.get_element().get_child_by_name("source")
#         appsrc.connect("need-data", self.on_need_data)


# class GstreamerRtspServer(GstRtspServer.RTSPServer):
#     def __init__(self, **properties):
#         super(GstreamerRtspServer, self).__init__(**properties)
#         self.factory = VideoAppSrc()
#         self.factory.set_shared(True)
#         self.get_mount_points().add_factory("/stream", self.factory)
#         self.attach(None)


# Gst.init(None)

# server = GstreamerRtspServer()

# loop = GObject.MainLoop()
# loop.run()
