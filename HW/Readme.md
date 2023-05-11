라즈베리파이 초기 설정
Raspberry pi imager 프로그램을 설치 후 OS64bit, storage sd카드 선택
설정 -> enable SSH -> use passward authenitication -> ID/ 와이파이password 설정, locale로
다 끝났으면 write를 이용해 sd카드에 쓰기

SSH 활성화 << imager 1.7.1 이상에선 필요한 작업이 아님 혹시 몰라 작업
PC에서 간단하게 활성화 하기 
boot 드라이브 -> cmdline, config 파일 확장명 보이게
새로운 ssh.txt 파일 만든 후 usb 다시 꽂아 확인.

라즈베리파이 사용법
1. 모니터, 키보드, 마우스를 연결하여 컴퓨터처럼 사용
2. 컴퓨터에서 라즈베리파이에 SSH터미널 혹은 VNC 접속하여 사용

디스플레이를 이용한 wifi 설정
라즈베리파이 창에서 오른쪽 위에 wifi 클릭 후
SSID -> 와이파이 apply 후 국가 US로 설정

원격으로 라즈베리파이 다루기
ifconfig -> inet 주소가 파이의 ip주소
configuration -> interfaces - ssh Enable로 바꾸기
같은 와이파이로 연결된 컴퓨터에서 putty 실행 후 ip주소 입력 후 open -> 접속됨
pi / 비밀번호 입력 후 엔터 -> 라즈베리파이에 연결됨
sudo apt-get install xrdp << xrdp 원격 접속 프로그램

중복로그인 푸는 법
sudo nano /boot/config.txt
중간의 hdmi_force_hotplug=1의 앞에 #을 없애줌 << 모니터가 꽂혀있지 않아도 라즈베리파이에 원격으로 이용가능
sudo raspi-config -> system options -> boot/auto login -> desktop << 자동 로그인 취소를 통해 원격 로그인 가능
finish를 하여 끝

원격 데스크톱 연결 -> 라즈베리파이IP:3389를 통해 원격 연결
username : pi / password : ~~
cmd에서 기본 게이트웨이 주소를 찾은 후
라즈베리파이를 고정 내부 ip로 등록 함
포트포워딩으로 외부 10000번대에서 아무거나 내부 3389

카메라 연결 및 사진 찍기
라즈베리파이 터미널
sudo raspi-config 입력 -> interfacing option -> camera -> yes -> reboot
~$ raspistill -o test.jpg 명령어 입력 이때 test.jpg의 이름을 바꾸지 않으면 같은 파일에 덮어 쓰기 됨
~ $ raspistill -vf -o test.jpg -t 10000 << t명령어는 ms뒤에 찍는다 -vf상하반전 / -hf 좌우반전

동영상 찍기
~ $ raspivid -o vid.h264 << 확장자가 mp4가 아님 따라서 바꿔주기
~$ sudo apt-get install -y gpac <<< 모든 질문에 yes로 답하기
~$ MP4Box -add vid3.h264 vid3.mp4 <<명령어로 mp4로 인코딩

파이썬을 이용한 동영상 찍기
~$ sudo nano camera.py 편집기를 이용하여 py코드로 접속
////////////////////////////////////
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.rotation = 180 #180도 회전
camera.capture('/home/pi/capture.jpg')
camera.start_recording(/home/pi/vid.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
///////////////////////////////////////
필요한 코드 갖다 쓰기
~$ sudo python camera.py로 파이썬으로 짠 코드 실행

한글포트 설치 방법
sudo apt install fonts-unfonts-core  (관리자권한 다운명령어 설치 무엇을설치할건지)
configuration -> locale -> setlocale -> Ko -> UTF-8로 설정
Timezone -> Asia -> Seoul
sudo apt remove ibus ibus-hangul 기존 입출력 삭제
sudo apt install fcitx fcitx-hangul 한글 입출력 설치
sudo nano /etc/default/im-config -> auto를 fcitx로 한글 입력기 설정
nano <- 파일 고치기

