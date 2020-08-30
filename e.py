import pickle
import cv2
import numpy as np
from PIL import Image
import os
import fnmatch
import contour


# 파일 이름 추출
# **파일이 디렉토리내에 두개있으면 어떤걸 선택??????????
def filename():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.mp4'):
            return file
        elif fnmatch.fnmatch(file, '*.avi'):
            return file


def dis(screen):
    #frame을 하나 가져와서 캐릭터와 에임사이의 픽셀거리를 알아냄
    #여기에 지원이 코드 삽입해줘
    #캐릭터와 에임사이 거리 알아내는 므찐 코드
    distance = 10
    return distance


def framecutting(framenumber):
    ad = [None] *11 # 에임사이의 거리 11개를 저장할 리스트 (aim distance)
    # 지정한 디렉토리 경로
    path = 'C:/Users/k96422/PycharmProjects/graduation/jpg'
    try:
        #print('영상을 불러옵니다.')
        name = filename()
        cap = cv2.VideoCapture(name)
    except FileNotFoundError:
        print('불러오기 실패')
        return
    cap.set(cv2.CAP_PROP_POS_FRAMES, framenumber)
    j = 0
    for i in range(int(framenumber-5),int(framenumber+6)):
        ret, screen = cap.read()
        if ret:
            # 저장되는지 확인 : 저장됨
            #h = cv2.imwrite(os.path.join(path , 'overwatch'+str(i)+'.jpg'), screen)
            # 여기서 캐릭터와 에임사이의 거리를 뽑아내서 리스트에 저장?
            # 아니면 저장된 image를 하나씩 불러와서 확인?
            distance = dis(screen)
            ad[j] = distance
            j = j+1
            k = cv2.waitKey(1)
            if k == 27:
                break
        else:
            print('error')
    cap.release()
    #print(ad)
    return ad # 캐릭터와 에임사이의 거리를 저장한 리스트를 반환


# 특정좌표에서 아군과 적군색상 rgb추출후 색상이름 리스트를 받환
def Position(frame):
    # # 화면 : frame
    # height = frame.shape[1]
    # print(height)
    # # FRAME TO IMAGE
    rgb_frame = Image.fromarray(frame.astype('uint8'), 'RGB')
    # index : height=1280, width=720
    # 좌표 위치 2개 설정 (아군색, 적군색 추출용)
    taps = [(1279 ,719), (640, 360)]
    # 추출한 색상값 return 할 list 변수 추가
    rgb = []
    for tap in taps:
        # 빨간색, 황갈색, 주황색, 황금색, 노란색, 연두색, 녹색, 네온파란색, 파란색, 보라색, 남색, 심홍색, 핑크색
        if (202, 0, 20) == rgb_frame.getpixel(tap):  # 해당 좌표의 rgb색상이 202, 0, 20이라면
            rgb.append('red') # rgb list에 색상이름 red를 추가
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
    return rgb # 아군색상과 적군색상 이름


def tracking():
    # 영상 불러오기
    try:
        print('영상을 불러옵니다.')
        name = filename()
        cap = cv2.VideoCapture(name)
        # cap = cv2.VideoCapture('1.mp4')
    except FileNotFoundError:
        print('불러오기 실패')
        return
    # 원하는 위치로 영상 이동
    sec =13
    cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    ret, screen = cap.read()
    # framecutting(20)
    # 색상추출
    rgb = Position(screen)
    # print(rgb)
    # 정확한 좌표를 못찾아서 일단 하드코딩
    rgb = ['red','blue']

    # hsv_color.pickle 파일 불러온 후 변수 data에 저장
    f = open("hsv_colors.pkl", "rb")
    data = pickle.load(f)
    # x 색상 hsv범위 #
    #data['x'] = [115,0,180],[145,20,235]
    # rgb를 hsv로 바꾸기
    for rgbs in data.keys():
        # 우리팀 색깔 hsv가져오기
        if rgbs == rgb[0]:
            hsv2 = data[rgbs]
        # 상대팀 색깔 hsv가져오기 - 일단 패스
        # if rgbs == rgb[1]:

    # upper와 lower설정
    lower = np.array(hsv2[0])
    upper = np.array(hsv2[1])

    # 다시 0초부터 video 재생
    cap.set(cv2.CAP_PROP_POS_MSEC, 0)
    fl = [] # x가 발견되는 framenumber list
    x = s = 0 #헤드샷 비율 count용 int
    while 1:
        # 재생되는 비디오를 한프레임씩 읽고, 정상적으로 읽으면 ret이 true
        # ret 값을 체크해서 비디오 프레임을 제대로 읽엇는지 확인 가능
        ret, frame = cap.read()
        if ret:
            framenumber=cap.get(cv2.CAP_PROP_POS_FRAMES)
            # # BGR을 HSV모드로 전환
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # x표시나 해골표시가 match되면 fl list에 현재 framenumber추가
            if contour.skullMatch(frame):
                s = s+1
                fl.append(framenumber)
            elif contour.xMatch(frame):
                x = x+1
                fl.append(framenumber)

            # mask와 나머지 설정
            mask = cv2.inRange(hsv, lower, upper)
            rest = cv2.bitwise_and(frame, frame, mask=mask)
            # cv2.imshow('original',frame)
            #cv2.imshow('my new video', rest)
            # width :  1920, height :  1080 #frame.shape로 알아낸 것
            # dst = frame.copy()
            #middle = rest[340:380, 620:670] #x위치를 framecut한것
            # dst[0:100, 0:100] = middle #왼쪽위에 imshow하고 싶을때 이거
            # rest2 = cv2.bitwise_and(middle, middle, mask=mask)
            #cv2.imshow('middle', middle)
            """k=cv2.waitKey(1)
            if k == 27 :
                break"""

        # frame 읽기에 문제가 발생하면
        else:
            break
    # memory release
    print(fl)
    print(s,x)
    cap.release()
    cv2.destroyAllWindows()
    f.close()

    #ratio = s/(x+s)
    return fl
        #, ratio


def main():
    # main 코드
    #distance = []
    #x또는 해골표시가 나타난 framenumber list
    #framenumber, ratio=tracking()
    framelist = tracking()
    #distance feature를 받을 2차원 배열
    distance = [[0 for col in range(11)] for row in range(len(framelist))]
    j=0
    #각각 framenumber에 대해 앞뒤 10개를 돌려서 distance를 받음
    for i in framelist:
        distance[j]= framecutting(i)
        j =j+1
    #feature 값 distance와 헤드샷 비율 반환
    return distance
        #, ratio

main()
#tracking()
