# RPIVideoStream
OpenCV video receiving stream using a GStreamer backend pipeline. 


Command Line Code on RPI:



raspivid -n -t 0 -w 1920 -h 1080 -fps 30 -b 6000000 -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host=(HOST IP) port=5001


After you run the videos stream on the RPI, run the python code on your computer to open the capture of the stream.

When you run the python code, you will be prompted the video length you wish to save.
