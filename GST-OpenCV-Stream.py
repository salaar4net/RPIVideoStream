import cv2
import time

#Standard Input

inp = input("Video Length: ")
seconds = int(inp)
gstreamer_str = "udpsrc port=5001 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! video/x-h264, width=1920, height=1080, framerate=30/1 ! avdec_h264 ! videoconvert ! appsink"
# Video Capture

cap = cv2.VideoCapture(gstreamer_str, cv2.CAP_GSTREAMER)

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
# Print to check resolution and fps
print('Src opened, %dx%d @ %d fps' % (w, h, fps))

# Video Save Output
out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc(*'h264'), 30.0, (1920,1080)) 

# Writing and opening frame captures
fWrite = False
end_time = time.time() + 1000000000
while(cap.isOpened() and time.time() < end_time):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Input via Gstreamer", frame)
        out.write(frame)
        if (fWrite == False):
            end_time = time.time() + seconds
            fWrite = True
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        else:
            pass
    else:
        break
cap.release() 
out.release()
cv2.destroyAllWindows()
