import pickle
import cv2
import numpy as np
from PIL import Image
import os
import fnmatch

def filename():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.mp4'):
            return file
        elif fnmatch.fnmatch(file, '*.avi'):
            return file

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

    while 1:
        # 재생되는 비디오를 한프레임씩 읽고, 정상적으로 읽으면 ret이 true
        # ret 값을 체크해서 비디오 프레임을 제대로 읽엇는지 확인 가능
        ret, frame = cap.read()
        if ret:
            # # BGR을 HSV모드로 전환
            #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.cvtColor(gray, (3,3),0)
            canny = cv2.cvtColor(blur, 100, 200)
            middle = canny[300:400, 600:700]
            cv2.imshow('middle', middle)


            k=cv2.waitKey(1)
            if k == 27 :
                break
        else:
            break
    #memory release
    cap.release()
    cv2.destroyAllWindows()

# main 코드
tracking()