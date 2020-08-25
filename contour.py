import cv2
import numpy as np


def Contour():
    #cv2.namedWindow("noise removal")
    img = cv2.imread("jpg/overwatch275.jpg", cv2.IMREAD_COLOR)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 잡음 제거
    img_hsv = cv2.fastNlMeansDenoisingColored(img_hsv, None, 10, 10, 7, 21)
    lower = np.array([167, 30, 30], dtype="uint8")
    upper = np.array([187, 255, 255], dtype="uint8")
    img_cont = cv2.inRange(img_hsv, lower, upper)
    #cv2.imshow('img',img_cont)
    contours, hierarchy = cv2.findContours(img_cont, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# 가장 큰 영역 찾기
    max = 0
    maxcnt = None
    for cnt in contours :
        area = cv2.contourArea(cnt)
        if(max < area) :
            max = area
            maxcnt = cnt
    # maxcontours의 각 꼭지점 다각선 만들기
    #hull = cv2.convexHull(maxcnt)
    # img 다 0으로 만들기?
    mask = np.zeros(img.shape).astype(img.dtype)
    color = [255, 255, 255]

    # 경계선 내부 255로 채우기
    cv2.fillPoly(mask, [maxcnt], color)
    img_hand = cv2.bitwise_and(img, mask)

    #cv2.drawContours(img_hand, [maxcnt], 0, (255, 0, 0), 3)
    #cv2.drawContours(img_hand, [hull], 0, (0, 255, 0), 3)

    # 이미지 보여주기
    cv2.imshow('image', img_hand)
    while True:
        if cv2.waitKey(0) == 27:
            cv2.destroyWindow('image')
            break
    return

Contour()