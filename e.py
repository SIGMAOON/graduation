import cv2
import numpy as np
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


def get_Distance(screen):
    #frame을 하나 가져와서 캐릭터와 에임사이의 픽셀거리를 알아냄
    #여기에 지원이 코드 삽입해줘
    #캐릭터와 에임사이 거리 알아내는 므찐 코드
    distance = 10
    return distance


def framecutting(framenumber):
    ad = [None] *11 # 에임사이의 거리 11개를 저장할 리스트 (aim distance)
    # 지정한 디렉토리 경로
    path = 'jpg'
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
            distance = get_Distance(screen)
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


def find_FrameNum():
    # 영상 불러오기
    try:
        print('영상을 불러옵니다.')
        name = filename()
        cap = cv2.VideoCapture(name)
    except FileNotFoundError:
        print('불러오기 실패')
        return
    fl = [] # x가 발견되는 framenumber list
    x = s = 0 #헤드샷 비율 count용 int
    while 1:
        # 재생되는 비디오를 한프레임씩 읽고, 정상적으로 읽으면 ret이 true
        # ret 값을 체크해서 비디오 프레임을 제대로 읽엇는지 확인 가능
        ret, frame = cap.read()
        if ret:
            framenumber = cap.get(cv2.CAP_PROP_POS_FRAMES)
            # x표시나 해골표시가 match되면 fl list에 현재 framenumber추가
            if contour.skullMatch(frame):
                s = s+1
                fl.append(framenumber)
            elif contour.xMatch(frame):
                x = x+1
                fl.append(framenumber)
        # frame 읽기에 문제가 발생하면
        else:
            break
    print(fl)
    print(s,x)

    # memory release
    cap.release()
    cv2.destroyAllWindows()
    return fl,x,s

def main():
    #distance = []
    #x또는 해골표시가 나타난 framenumber list
    framelist,x,s = find_FrameNum()

    #distance feature를 받을 2차원 배열
    distance = [[0 for col in range(11)] for row in range(len(framelist))]
    j=0
    #각각 framenumber에 대해 앞뒤 10개를 돌려서 distance를 받음
    for i in framelist:
        distance[j]= framecutting(i)
        j =j+1
    #feature 값 distance와 헤드샷 비율 반환
    # ratio = s/(x+s)
    return distance  #, ratio


main()
