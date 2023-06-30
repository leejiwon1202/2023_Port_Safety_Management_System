import cv2 as cv
import numpy as np
import threading
#import torch 


fps= 30
dst='./test.mp4'    #저장 위치

save_second=3   #몇초 저장할건지

queue_size = save_second*30
queue = []

#model=model()
#model.load_state_dict(torch.load(./aaaa))
def imagemodel(model, cap):
    result=model(cap)

def showNsave():
    print("11111")
    cap = cv.VideoCapture('rtmp://34.216.5.166:1935/live/0000')
    ret, frame = cap.read()
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(dst, fourcc, fps, (frame.shape[0], frame.shape[1]))
    print("22222")
    while cap.isOpened():
        print("3333")
        ret, frame = cap.read()
        print('4444')
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow('frame', frame)
        print("5555")
        queue.append(frame)
        print(type(frame))
        if len(queue) > queue_size:
            queue.pop(0)
            
        if cv.waitKey(1) == ord('q'):
            break
        if cv.waitKey(1) == ord('s'):
            for f in queue:
                out.write(f)
        print(len(queue))
    out.release()
    cap.release()

S_S=threading.Thread(target=showNsave, args=())#show and save

def main():
    S_S.start()
    
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()