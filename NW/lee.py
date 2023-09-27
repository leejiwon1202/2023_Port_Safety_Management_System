from ultralytics import YOLO
import cv2
import numpy as np
from multiprocessing import shared_memory
import sys
flag=np.array([0])
# flagshm= shared_memory.SharedMemory(name= 'wnsm_202710aa')#flag 주소
flagshm= shared_memory.SharedMemory(name= sys.argv[3])#flag 주소
flag = np.ndarray(flag.shape, dtype=flag.dtype, buffer=flagshm.buf)

#frameshm= shared_memory.SharedMemory(name= 'wnsm_8721aa3b')#frame주소
frameshm= shared_memory.SharedMemory(name= sys.argv[5])
cap = cv2.VideoCapture('./2023-09-05#17h42m12s.mp4')
ret, frame = cap.read() #동영상 정보 읽어오기 -read
numbers = sys.argv[1].strip('()').split(',')
shape = tuple(int(num) for num in numbers)
frame = np.ndarray(shape, dtype=frame.dtype, buffer=frameshm.buf)

def getIntersectionArea(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    return (xB - xA + 1) * (yB - yA + 1)

coord_list = []

person_model = YOLO("./weights/person.pt")
door_model = YOLO("./weights/door.pt")

while True:
    #ret, frame = cap.read() # 여기서 프레임을 받아옴
    fakeflag=0
    if ret:
        coord_list = []
        for coord in person_model.predict(frame)[0].boxes:
            x, y, w, h = coord.xywh[0][:]
            xmin, ymin, xmax, ymax = int(x-w/2), int(y-h/2), int(x+w/2), int(y+h/2)
            cv2.rectangle(frame, (xmin, ymin, xmax, ymax), (0, 0, 255), 4) # 삭제해도 됨
            coord_list.append([xmin, ymin, xmax, ymax])
            break
            
        for coord in door_model.predict(frame)[0].boxes:
            x, y, w, h = coord.xywh[0][:]
            xmin, ymin, xmax, ymax = int(x-w/2), int(y-h/2), int(x+w/2), int(y+h/2)
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (255, 0, 0), 4) # 삭제해도 됨
            coord_list.append([xmin, ymin, xmax, ymax])
        
        area = 0
        distance = 0
        #for i in range(len(coord_list) - 1): 
        for i in range(len(coord_list)): 
            for j in range(i+1, len(coord_list)):
                area = getIntersectionArea(coord_list[i], coord_list[j])
            if area > 0:
                # 여기서 신호 보내면 됨
                fakeflag=2
                cv2.putText(frame, "WARNING!!", (50, 100), 1, 3, (0, 0, 255), 5, cv2.LINE_AA) # 삭제해도 됨
                break
            else:
                fakeflag=0
        flag[0]=fakeflag
        cv2.imshow("frame", frame) # 삭제해도 됨

        if cv2.waitKey(10) == 27: # 삭제해도 됨
            break # 삭제해도 됨
    
cap.release() # 삭제해도 됨
cv2.destroyAllWindows() # 삭제해도 됨