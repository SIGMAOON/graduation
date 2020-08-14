
import pickle
import cv2
import numpy as np
from PIL import Image
import os
import fnmatch


# 파일 이름 추출
def filename():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.mp4'):
            return file
        elif fnmatch.fnmatch(file, '*.avi'):
            return file

def framecutting(framenumber = 20):
    # 지정한 디렉토리 경로
    path = 'C:\Users\gwon8\Desktop\졸업프로젝트'
    for i in range(framenumber-5,framenumber+5):
        cv2.imwrite(os.path.join(path , '오버워치.jpg')


#특정좌표에서 아군과 적군색상 rgb추출후 색상이름 리스트를 받환
def Position(frame):
    # # 화면 : frame
    #height = frame.shape[1]
    #print(height)
    # #FRAME TO IMAGE
    rgb_frame = Image.fromarray(frame.astype('uint8'), 'RGB')
    # index : height=1280, width=720
    # 좌표 위치 2개 설정 (아군색, 적군색 추출용)
    taps = [(1279 ,719), (640, 360)]
    # 추출한 색상값 return 할 list 변수 추가
    rgb = []
    for tap in taps:
        # 빨간색, 황갈색, 주황색, 황금색, 노란색, 연두색, 녹색, 네온파란색, 파란색, 보라색, 남색, 심홍색, 핑크색
        if (202, 0, 20) == rgb_frame.getpixel(tap):  # 해당 좌표의 rgb색상이 202, 0, 20이라면
            rgb.append('red') #rgb list에 색상이름 red를 추가
        elif (212, 88, 0) == rgb_frame.getpixel(tap):
            rgb.append('yellowish_brown')
        elif (213, 122, 0) == rgb_frame.getpixel(tap):
            rgb.append('orange')
        elif (255, 125, 0) == rgb_frame.getpixel(tap):
            rgb.append('gold')
        elif (255, 255, 0) == rgb_frame.getpixel(tap):
            rgb.append('yellow')
        elif (203, 254, 0) == rgb_frame.getpixel(tap):
            rgb.append('light_green')
        elif (0, 172, 130) == rgb_frame.getpixel(tap):
            rgb.append('green')
        elif (0, 251, 251) == rgb_frame.getpixel(tap):
            rgb.append('neon_blue')
        elif (41, 169, 226) == rgb_frame.getpixel(tap):
            rgb.append('blue')
        elif (127, 0, 127) == rgb_frame.getpixel(tap):
            rgb.append('violet')
        elif (81, 60, 253) == rgb_frame.getpixel(tap):
            rgb.append('bluish_violet')
        elif (254, 0, 254) == rgb_frame.getpixel(tap):
            rgb.append('magenta')
        elif (245, 105, 191) == rgb_frame.getpixel(tap):
            rgb.append('pink')
        else:
            rgb.append('x')
    return rgb #아군색상과 적군색상 이름


def tracking():
    # 영상 불러오기
    try:
        print('영상을 불러옵니다.')
        name = filename()
        cap = cv2.VideoCapture(name)
        #cap = cv2.VideoCapture('1.mp4')
    except FileNotFoundError:
        print('불러오기 실패')
        return
    #원하는 위치로 영상 이동
    sec =13
    cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    ret, screen = cap.read()
    framecutting(20)
    #색상추출
    rgb = Position(screen)
    #print(rgb) #['white', 'white']로 나옴
    # 정확한 좌표를 못찾아서 일단 하드코딩
    rgb = ['x','blue']
    #print(rgb)

    # hsv_color.pickle 파일 불러온 후 변수 data에 저장
    f = open("hsv_colors.pkl", "rb")
    data = pickle.load(f)
    #x 색상 hsv범위#
    data['x'] = [115,0,180],[145,20,235]
    #rgb를 hsv로 바꾸기
    for rgbs in data.keys():
        # 우리팀 색깔 hsv가져오기
        if rgbs == rgb[0]:
            hsv2 = data[rgbs]
        # 상대팀 색깔 hsv가져오기
        # if rgbs == rgb[1]:
    #upper와 lower설정

    lower = np.array(hsv2[0])
    upper = np.array(hsv2[1])

    #다시 0초부터 video 재생
    cap.set(cv2.CAP_PROP_POS_MSEC, 0)
    while 1:
        # 재생되는 비디오를 한프레임씩 읽고, 정상적으로 읽으면 ret이 true
        # ret 값을 체크해서 비디오 프레임을 제대로 읽엇는지 확인 가능
        ret, frame = cap.read()
        if ret:
            # # BGR을 HSV모드로 전환
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # mask와 나머지 설정
            mask = cv2.inRange(hsv, lower, upper)
            #mask2 = cv2.inRange(hsv, lower_white, upper_white)
            rest = cv2.bitwise_and(frame, frame, mask=mask)
            #cv2.imshow('original',frame)
            #cv2.imshow('my new video', rest)
            #width :  1920, height :  1080
            #dst = frame.copy()
            middle = rest[300:400, 600:700]
            #dst[0:100, 0:100] = middle
            #rest2 = cv2.bitwise_and(middle, middle, mask=mask)
            cv2.imshow('middle', middle)

            k=cv2.waitKey(1)
            if k == 27 :
                break
            """k = 27
            if k == cv2.waitKey(1) & 0xFF == ord('q'):
                break"""
        # frame 읽기에 문제가 발생하면
        else:
            break
    #memory release
    cap.release()
    cv2.destroyAllWindows()
    f.close()

# main 코드
tracking()
