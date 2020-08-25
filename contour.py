import cv2
import numpy as np
#가우시안 블러 + 캐니 디텍션 적용


def Gray():
    img = cv2.imread("jpg/overwatch275.jpg", cv2.IMREAD_COLOR)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #빨강색 outline 검출
    lower = np.array([170, 30, 30], dtype="uint8")
    upper = np.array([178, 255, 255], dtype="uint8")
    mask = cv2.inRange(img_hsv, lower, upper)
    img_color = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)
    # hsv to gray
    img_rgb = cv2.cvtColor(img_color, cv2.COLOR_HSV2BGR)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # 가우시안 블러, noise제거, threshold
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_dn = cv2.fastNlMeansDenoising(img_blur, 10, 10, 7, 21)
    ret3, img_th = cv2.threshold(img_dn, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # contour, canny edge
    canny = cv2.Canny(img_th, 70, 30)
    #sobelx = cv2.Sobel(canny, cv2.CV_64F, 1, 0, ksize=3)
    #sobely = cv2.Sobel(, cv2.CV_64F, 0, 1, ksize=3)
    #laplacian = cv2.Laplacian(img, cv2.CV_8U)

    contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        hull =cv2.convexHull(cnt)
        img_hull = cv2.drawContours(canny, [hull], 0, (255,0,255),5)

    contours, hierarchy = cv2.findContours(img_hull, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    max = 0
    maxcnt = None
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (max < area):
            max = area
            maxcnt = cnt
    mask = np.zeros(img_hull.shape).astype(img_hull.dtype)
    color = [255, 255, 255]
    cv2.fillPoly(mask, [maxcnt], color)
    img_hand = cv2.bitwise_and(img_hull, mask)
    cv2.imshow('image', img_hand)

    while True:
        if cv2.waitKey(0) == 27:
            cv2.destroyWindow('image')
            break
    return

Gray()

def Contour():
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

#Contour()