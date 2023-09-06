import cv2 as cv
import numpy as np
import multiprocessing as mp
from multiprocessing import shared_memory

cap = cv.VideoCapture('./2023-09-05#17h42m12s.mp4')
ret, frame = cap.read() #동영상 정보 읽어오기 -read
frameshm= shared_memory.SharedMemory(name= 'wnsm_2e5ebdd5')
# while 1:
#     ret, frame=cap.read()
#     
#     x=np.ndarray(frame.shape, dtype=frame.dtype, buffer=frameshm.buf)
#     cv.imshow('frame', frame)
    
    #동영상 출력 - 실행시 큰 창으로 출력 
while(cap.isOpened()):
    x=np.ndarray(frame.shape, dtype=frame.dtype, buffer=frameshm.buf)
    if ret:
    #frame은 이미지 정보이므로 imshow 로 읽어들일 수 있음
        cv.imshow('frame', x)  
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv.destroyAllWindows()