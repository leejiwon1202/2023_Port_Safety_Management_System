import cv2 as cv
import numpy as np
import threading
import os
import time
#import torch 

fps= 30
dst='test.mp4'    #저장 위치

event_flag=0

save_second=3   #몇초 저장할건지

queue_size = save_second*30
queue = []

#model=model()
#model.load_state_dict(torch.load(./aaaa))
def flagcontrol():
    global event_flag
    while True:
        event_flag=0
        time.sleep(5)
        event_flag=1
        time.sleep(5)
        

def showNsave():
    cap = cv.VideoCapture('rtmp://3.35.25.173:1935/live/0000')
    ret, frame = cap.read()
    innerflag=0
    print(type(frame))
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(dst, fourcc, fps, (frame.shape[1], frame.shape[0]))
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
        if cv.waitKey(1) == ord('q'):#여기는 시그널 처리 해줘야함
            break
        if innerflag==0 and event_flag==1:#여기는 위험 신호 감지해서 저장하게 해야하고
            innerflag=event_flag
            for f in queue:
                out.write(f)
        elif innerflag==1 and event_flag==1:
            out.write(frame)
        elif innerflag==1 and event_flag==0:
            innerflag=event_flag
        print(event_flag)
    out.release()
    cap.release()

S_S=threading.Thread(target=showNsave, args=())#show and save
fctl=threading.Thread(target=flagcontrol, args=())
fctl.daemon=True
def main():
    fctl.start()
    if os.path.exists(dst):
        os.remove(dst)
    S_S.start()
    
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()