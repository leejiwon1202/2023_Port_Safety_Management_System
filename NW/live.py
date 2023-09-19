import cv2
import mediapipe as mp
import numpy as np
import torch.nn as nn
import torch
from multiprocessing import shared_memory
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

flag=np.array([0])
flagshm= shared_memory.SharedMemory(name= 'wnsm_9400e8a0')#flag 주소
flag = np.ndarray(flag.shape, dtype=flag.dtype, buffer=flagshm.buf)

frameshm= shared_memory.SharedMemory(name= 'wnsm_97d54b24')#frame주소
cap = cv2.VideoCapture('./2023-09-05#17h42m12s.mp4')
ret, frame = cap.read() #동영상 정보 읽어오기 -read
frame = np.ndarray((800, 1280, 3), dtype=frame.dtype, buffer=frameshm.buf)
class GRU(nn.Module):
    def __init__(self, input_size, hidden_size, sequence_length, num_layers, device):
        super(GRU, self).__init__()
        self.device = device
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size*sequence_length, 1)
        
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(self.device)
        out, _ = self.gru(x, h0)
        out = out.reshape(out.shape[0], -1)
        out = self.fc(out)
        return out


sequence_length = 90
input_size = 132
num_layers = 2
hidden_size = 8
model = GRU(input_size = input_size, hidden_size = hidden_size, sequence_length = sequence_length, num_layers = num_layers, device = device).to(device)
model.load_state_dict(torch.load(f=r'C:\Users\mkjsy\Desktop\YM\Source Code\VSCode\SHM\My\savepoint1238.pth'))

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode = True, min_detection_confidence = 0.1, model_complexity = 2)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
cap = cv2.VideoCapture(0)

queue_size = 90
queue = []

while True:
    #image.flags.writeable = False
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(image)

    x = []
    try:
        for k in range(33):
            x.append(result.pose_landmarks.landmark[k].x)
            x.append(result.pose_landmarks.landmark[k].y)
            x.append(result.pose_landmarks.landmark[k].z)
            x.append(result.pose_landmarks.landmark[k].visibility)
    except AttributeError:
        x = np.zeros(132)
    queue.append(x)
    
    #image.flags.writeable = True
    cv2.imshow('Webcam', cv2.flip(image, 1))

    if len(queue) == queue_size:
        input = torch.FloatTensor(queue).to(device)
        input = input.unsqueeze(0)
        out = model(input)
        if out > 2.5:
            if (flag[0]/10)==1:
                flag[0] = flag[0]
            else:
                flag[0]=flag[0]+10
        else:
            if (flag[0]/10)==1:
                flag[0] = flag[0]-10
            else:
                flag[0]=flag[0]
        print(flag)
        queue.pop(0)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
