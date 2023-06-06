import cv2 as cv
import numpy as np

cap = cv.VideoCapture('rtmp://34.216.5.166:1935/live/0000')
fourcc = cv.VideoWriter_fourcc(*'mp4v')
w=round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h=round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps= 30
out = cv.VideoWriter('/Users/yundong-geun/project/smart/'+
                     '2023_Port_Safety_Management_System/NW/test.mp4'
                     , fourcc, fps, (w,h))
queue_size = 90
queue = []
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('frame', frame)
    queue.append(frame)
    if len(queue) > queue_size:
        queue.pop(0)
    if cv.waitKey(1) == ord('q'):
        break
    print(len(queue))

out.release()
cap.release()
cv.destroyAllWindows()