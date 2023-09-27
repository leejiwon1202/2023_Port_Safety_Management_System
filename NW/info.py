import sys
import os
import cv2 as cv
import numpy as np
from multiprocessing import shared_memory

cap = cv.VideoCapture('rtmp://3.38.100.84:1935/live/0000')
ret,frame=cap.read()
if not ret:
    print('not')
else:
    os.system('echo '+str(frame.shape).replace(' ', '')+' > info.txt')
    flag=np.array([0])
    flagshm=shared_memory.SharedMemory(create=True, size=flag.nbytes)
    os.system('echo '+flagshm.name+' >> info.txt')
    frameshm=shared_memory.SharedMemory(create=True, size=frame.nbytes)
    os.system('echo '+frameshm.name+' >> info.txt')
    while True:
        frame=frame
