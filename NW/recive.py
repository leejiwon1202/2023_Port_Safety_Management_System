import cv2 as cv
import numpy as np
import threading
import os
import time
import datetime
#import torch 

fps= 30
dst='test.mp4'    #저장 위치

event_flag=0
save_second=3   #몇초 저장할건지

queue_size = save_second*30
queue = []
class Sdata:
    def __init__(self, cam_no):
        self.cam_no=cam_no
        self.event_type=0
        self.link_storage=''
        self.date=''
        self.time=''
        
        
#model=model()
#model.load_state_dict(torch.load(./aaaa))
def flagcontrol():
    global event_flag
    while True:
        event_flag=0
        time.sleep(10)
        event_flag=1
        time.sleep(15)

def showNsave(cam_no):
    global cap
    sdata=Sdata(0)
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
        if innerflag==0 and event_flag!=0:#여기는 위험 신호 감지해서 저장하게 해야하고
            sdata.cam_no=cam_no
            sdata.event_type=event_flag
            innerflag=event_flag
            now = datetime.datetime.now()
            sdata.date=now.strftime("%Y-%m-%d")
            sdata.time=now.strftime("%Hh%Mm%Ss")
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%Hh%Mm%Ss")
            new_filename = f"{date}#{time}.mp4"
            for f in queue:
                out.write(f)
        elif innerflag!=0 and event_flag!=0:
            out.write(frame)
        elif innerflag!=0 and event_flag==0:
            innerflag=event_flag
            out.release()
            os.rename("test.mp4", new_filename)
            #s3 여기서 저장
            #여기서 linkstate넣어주고
            #pymysql로 여기서 저장 하면됨
            out = cv.VideoWriter(dst, fourcc, fps, (frame.shape[1], frame.shape[0]))
            
        print(event_flag)
        if (cv.waitKey(1)==27):
            break
    out.release()
    cap.release()
    os.rename("test.mp4", new_filename)


fctl=threading.Thread(target=flagcontrol, args=())
fctl.daemon=True
def main():
    global cap
    cam_no='0000'
    cap = cv.VideoCapture('rtmp://3.37.194.115:1935/live/'+cam_no)
    S_S=threading.Thread(target=showNsave, args=(cam_no))#show and save
    fctl.start()
    if os.path.exists(dst):
        os.remove(dst)
    S_S.start()
    
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()