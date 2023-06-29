import cv2 as cv
#import torch 
""" import datetime """

cap = cv.VideoCapture('rtmp://34.216.5.166:1935/live/0000')
fourcc = cv.VideoWriter_fourcc(*'mp4v')
w=round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h=round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps= 30
out = cv.VideoWriter('output.mp4', fourcc, fps, (w,h))
queue_size = 90
queue = []

#model=model()
#model.load_state_dict(torch.load(./aaaa))
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
    if cv.waitKey(1) == ord('s'):
        for f in queue:
            out.write(f)
    print(len(queue))

""" current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d/%H:%M")
 """
out.release()
cap.release()
cv.destroyAllWindows()