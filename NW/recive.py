import cv2 as cv
import numpy as np
import threading
import os
import time
import datetime
#import torch 
from upload import s3
import firebase_admin
from firebase_admin import credentials, db
import multiprocessing as mp
from multiprocessing import shared_memory

cred = credentials.Certificate("C:/Users/sjmama/ai-smartsafetysystem-firebase-adminsdk-5doyf-30cbb7476f.json")
firebase_admin.initialize_app(cred,
                              {'databaseURL' : 'https://ai-smartsafetysystem-default-rtdb.firebaseio.com'})
datapath='video'
ref=db.reference(datapath)
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
        time.sleep(5)
        event_flag=1
        time.sleep(2)
        event_flag=2
        time.sleep(2)

def showNsave(cam_no):
    global cap
    sdata=Sdata(cam_no)
    ret, frame = cap.read()
    innerflag=0
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    frameshm=shared_memory.SharedMemory(create=True, size=frame.nbytes)
    print(frameshm.name)
    out = cv.VideoWriter(dst, fourcc, fps, (frame.shape[1], frame.shape[0]))
    while cap.isOpened():
        ret, frame = cap.read()
        sharedframe=np.ndarray(frame.shape, dtype=frame.dtype, buffer=frameshm.buf)
        sharedframe[:]=frame[:]
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        #cv.imshow('frame', frame)
        queue.append(frame)
        if len(queue) > queue_size:
            queue.pop(0)
        if innerflag==0 and event_flag!=0:#여기는 위험 신호 감지해서 저장하게 해야하고
            print('1')
            ref=db.reference('flag')
            ref.set(event_flag)
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
            ref=db.reference('flag')
            ref.set(event_flag)
        elif innerflag!=0 and event_flag==0:
            print('0')
            ref=db.reference('flag')
            ref.set(event_flag)
            innerflag=event_flag
            out.release()
            os.rename("test.mp4", new_filename)
            s3.upload_file(new_filename,"sjmama1",new_filename)
            print('s3 upload!')
            sdata.link_storage='https://sjmama1.s3.ap-northeast-2.amazonaws.com/'+new_filename
            sdata_dict=sdata.__dict__
            print(sdata_dict)
            ref=db.reference('video')#저장한 파일은 삭제
            ref.push(sdata_dict)
            print('firebase push!')
            os.remove(new_filename)
            out = cv.VideoWriter(dst, fourcc, fps, (frame.shape[1], frame.shape[0]))
        if (cv.waitKey(1)==27):
            break
    out.release()
    cap.release()


fctl=threading.Thread(target=flagcontrol, args=())
fctl.daemon=True
def main():
    global cap
    cam_no='0000'
    cap = cv.VideoCapture('rtmp://3.38.100.84:1935/live/'+cam_no)
    S_S=threading.Thread(target=showNsave, args=(cam_no,))#show and save
    fctl.start()
    if os.path.exists(dst):
        os.remove(dst)
    S_S.start()
    S_S.join()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()