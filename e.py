### 구조물에 가려진 캐릭터도 식별
# 캐릭터 위에 x자 표시되면 헤드샷임.
# 닉네임도 킬로그상에서 확인.(누가 죽였는지 누가 죽었는지)
# 프로그램이 색상을 자동선택하도록 수정 (김희선)
# 비디오에서 색상을 hsv를 이용해 추출 (지승연)
# 비디오를 넣는 과정 수정 (문지원)

import pickle
import cv2
import numpy as np
from PIL import Image

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
            rgb.append('white')
    return rgb #아군색상과 적군색상 이름


"""안쓰는 함수 comment화
# RGB값을 HSV값으로 변형하기 위한 함수
def HSV(r, g, b):
    color = np.uint8([[[b, g, r]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    print('HSV for COLOR: ', hsv_color)
"""


def tracking():
    # 영상 불러오기
    try:
        print('영상을 불러옵니다.')
        cap = cv2.VideoCapture('1.mp4')
    except FileNotFoundError:
        print('불러오기 실패')
        return
    #원하는 위치로 영상 이동
    sec =13
    cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    ret, screen = cap.read()
    #색상추출
    rgb = Position(screen)
    #print(rgb) #['white', 'white']로 나옴
    # 정확한 좌표를 못찾아서 일단 하드코딩
    rgb = ['blue','blue']
    #print(rgb)

    # hsv_color.pickle 파일 불러온 후 변수 data에 저장
    f = open("hsv_colors.pkl", "rb")
    data = pickle.load(f)

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
            rest = cv2.bitwise_and(frame, frame, mask=mask)
            """
            # HSV에서 BGR로 가정할 범위를 정의함
             lower_blue = np.array([110, 100, 100])
             upper_blue = np.array([130, 255, 255])
            
             lower_green = np.array([50, 100, 100])
             upper_green = np.array([70, 255, 255])
            
             lower_red = np.array([-10, 100, 100])
             upper_red = np.array([10, 255, 255])
            
             # HSV 이미지에서 청색만, 또는 초록색만 또는 빨간색만 추출하기 위한 임계값
             mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
             mask_green = cv2.inRange(hsv, lower_green, upper_green)
             mask_red = cv2.inRange(hsv, lower_red, upper_red)

            # hsv의 모든 값을 lower_blue, upper_blue로 지정한 범위에 있는지 체크 후
            # 범위에 해당하면 그 값 그대로, 아니면 0으로 채워서 반환

            # mask와 원본 이미지를 비트 연산
             res1 = cv2.bitwise_and(frame, frame, mask=mask_blue)
             res2 = cv2.bitwise_and(frame, frame, mask=mask_green)
             res3 = cv2.bitwise_and(frame, frame, mask=mask_red)
            cv2.imshow('original', frame)
             cv2.imshow('BLUE', res1)
             cv2.imshow('GREEN', res2)
             cv2.imshow('RED', res3)

            lower_my = np.array([20, 100, 100])
            upper_my = np.array([40, 255, 255])
            mask_my = cv2.inRange(hsv, lower_my, upper_my)
            res4 = cv2.bitwise_and(frame, frame, mask=mask_my)
            """
            cv2.imshow('my new video', rest)

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
"""
# hsv(255, 110, 199)
# 색 후보: 169 104 20
# 169 79 20
# 255 110 199: 내 색(핑크) RGB -> 162 145 255
# 252 252 0: 상대 색(노랑) RGB -> 30 255 252

# x = tap[0]
# y = tap[1]
# b = frame[x, y, 0]  # B Channel Value
# g = frame[x, y, 1]  # G Channel Value
# r = frame[x, y, 2]  # R Channel Value
"""