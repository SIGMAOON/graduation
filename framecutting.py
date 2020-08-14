import cv2
import os

# x가 등장하는 프레임의 넘버를 받아 앞 뒤 다섯 프레임을 이미지로 저장함
def framecutting(framenumber = 20):
    # 지정한 디렉토리 경로
    path = 'C:\Users\gwon8\Desktop\졸업프로젝트'
    for i in range(framenumber-5,framenumber+5):
        cv2.imwrite(os.path.join(path , "%d" + '.jpg'),%i)