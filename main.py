from cv2 import VideoCapture, imwrite


cam = VideoCapture(0)

ret, frame = cam.read()

if ret:
  imwrite("frame.png", frame)


cam.release()