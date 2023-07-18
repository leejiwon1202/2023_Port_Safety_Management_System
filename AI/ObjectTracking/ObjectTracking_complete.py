# 0단계 - 필요한 라이브러리 임포트
import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from ultralytics import YOLO


# 1단계 - 칼만 필터 계산 & 필요 함수 작성
def kalman_filter(z_meas, x_esti, P):
    # (1) Prediction.
    x_pred = A @ x_esti
    P_pred = A @ P @ A.T + Q

    # (2) Kalman Gain.
    K = P_pred @ H.T @ inv(H @ P_pred @ H.T + R)

    # (3) Estimation.
    x_esti = x_pred + K @ (z_meas - H @ x_pred)

    # (4) Error Covariance.
    P = P_pred - K @ H @ P_pred

    return x_esti, P

def getPoint(model_result):
  point = model_result.boxes.xyxy[0]
  c_x = ((point[0] + point[2]) / 2).item()
  c_y = ((point[1] + point[3]) / 2).item()
  return [c_x, c_y]


# 2단계 - 공통 상수 선언
dt = 0.02
A = np.array([[ 1, dt,  0,  0],
              [ 0,  1,  0,  0],
              [ 0,  0,  1, dt],
              [ 0,  0,  0,  1]])
H = np.array([[ 1,  0,  0,  0],
              [ 0,  0,  1,  0]])
Q = 14.0 * np.eye(4)
R = np.array([[50,  0],
              [ 0, 50]])

x_0 = np.array([0, 0, 0, 0]) 
P_0 = 100 * np.eye(4)


# 3단계 - 객체별 변수 선언
p_esti, p_P = x_0, P_0
c_esti, c_P = x_0, P_0


# 4단계 - pretrained 모델 불러오기
model_person = YOLO('/home/jiwon/Harbor/person.pt')
model_container = YOLO('/home/jiwon/Harbor/OD_Person/SaveModel/weights/best.pt')


# 5단계 - 서버에서 받아오는 이미지를 이용하여 객체를 추적 -> 근접 시에 경보
cap = cv2.videocapture(0)
while True:
  _, frame = cap.read()

  res_p = model_person.predict(frame)
  res_c = model_container.predict(frame)

  # 1) 두 객체 모두 존재
  if len(res_p) != 0 and len(res_c) != 0:
    p_esti, p_P = kalman_filter(getPoint(res_p[0]), p_esti, p_P)
    c_esti, c_P = kalman_filter(getPoint(res_c[0]), c_esti, c_P)

    distance = ((p_esti[0] - c_esti[0]) ** 2 + (p_esti[1] - c_esti[1]) ** 2) ** 0.5

    if distance <= 100:
      print("위험 상황 발생!") # 이 부분을 서버로 신호 보내는 코드로 변경.

  # 2) 컨테이너만 존재 -> 사람 좌표 초기화
  elif len(res_c) != 0:
    p_esti, p_P = x_0, P_0
    c_esti, c_P = kalman_filter(getPoint(res_c[0]), c_esti, c_P)

  # 3) 사람만 존재 -> 컨테이너 좌표 초기화
  elif len(res_p) != 0:
    p_esti, p_P = kalman_filter(getPoint(res_p[0]), p_esti, p_P)
    c_esti, c_P = x_0, P_0
cap.release()