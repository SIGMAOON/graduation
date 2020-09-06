import cv2
import numpy as np
import os

# x인식1 -outline따기
def x_Outline():
    img = cv2.imread("jpg/overwatch297.jpg", cv2.IMREAD_COLOR)
    outline = cv2.Canny(img, 390, 430)
    #middle = outline[330:390, 610:670]
    cv2.imshow('canny', outline)
    path = 'C:/Users/k96422/PycharmProjects/graduation/jpg'
    #h = cv2.imwrite(os.path.join(path , 'x2.jpg'), middle)

    while True:
        if cv2.waitKey(0) == 27:
            cv2.destroyWindow('image')
            break
    return
#x_Outline()


# x인식2 - outline인식하기
def xMatch(img):
    #img = cv2.imread("jpg/overwatch281.jpg", cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    outline = cv2.Canny(img_gray, 390, 430)
    """img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0,0,255], dtype="uint8")
    upper = np.array([145, 255, 255], dtype="uint8")
    mask = cv2.inRange(img, lower, upper)
    outline = cv2.bitwise_and(img, img, mask=mask)"""

    """outline = cv2.cvtColor(outline, cv2.COLOR_HSV2BGR)
    outline = cv2.cvtColor(outline, cv2.COLOR_BGR2GRAY)"""

    #outline = img_gray[330:390, 610:670]
    template = cv2.imread("jpg/xxx1.jpg", 0)
    #print(template.shape)
    #template = cv2.Canny(template,390,420)
    #resize_template = template.resize((int(template.size[0] / 4), int(template.size[1] / 4)), 0)
    #resize_template = cv2.resize(template,(40,50))
    """cv2.imshow("outline", template)
    while True:
        if cv2.waitKey(0) == 27:
            cv2.destroyWindow('image')
            break
    #return"""
    res = cv2.matchTemplate(outline, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where(res >= threshold)
    # 유사도가 0.5이상이면 true를 return
    for pt in zip(*loc[::-1]):
        return True
    return False
#print(xMatch())


def skull_Outline():
    img = cv2.imread("jpg/overwatch304.jpg", cv2.IMREAD_COLOR)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 빨강색 outline 검출
    lower = np.array([160, 30, 30], dtype="uint8")
    upper = np.array([200, 255, 255], dtype="uint8")
    mask = cv2.inRange(img_hsv, lower, upper)
    img_color = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)
    img_rgb = cv2.cvtColor(img_color, cv2.COLOR_HSV2BGR)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    #middle = img_gray[310:400, 590:690]
    middle = img_gray[330:380, 610:670]
    cv2.imshow('skull', middle)
    path = 'C:/Users/k96422/PycharmProjects/graduation/jpg'
    h = cv2.imwrite(os.path.join(path, 'skull2.jpg'), middle)
    while True:
        if cv2.waitKey(0) == 27:
            cv2.destroyWindow('image')
            break
    return


def skullMatch(img):
    #img = cv2.imread("jpg/overwatch304.jpg", cv2.IMREAD_COLOR)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 빨강색 outline 검출
    lower = np.array([160, 30, 30], dtype="uint8")
    upper = np.array([200, 255, 255], dtype="uint8")
    mask = cv2.inRange(img_hsv, lower, upper)
    img_color = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)
    img_rgb = cv2.cvtColor(img_color, cv2.COLOR_HSV2BGR)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    outline = img_gray[310:400, 590:690]

    template = cv2.imread("jpg/skull.jpg", 0)

    res = cv2.matchTemplate(outline, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where(res >= threshold)
    # 유사도가 0.5이상이면 true를 return
    for pt in zip(*loc[::-1]):
        return True
    return False

#print(skullMatch())
#print(Match())

"""
def Gray():
    img = cv2.imread("jpg/overwatch283.jpg", cv2.IMREAD_COLOR)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #빨강색 outline 검출
    lower = np.array([170, 30, 30], dtype="uint8")
    upper = np.array([180, 255, 255], dtype="uint8")
    mask = cv2.inRange(img_hsv, lower, upper)
    img_color = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)
    # hsv to gray
    img_rgb = cv2.cvtColor(img_color, cv2.COLOR_HSV2BGR)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # 가우시안 블러, noise제거, threshold
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
    #img_dn = cv2.fastNlMeansDenoising(img_blur, 10, 10, 7, 21)
    #ret3, img_th = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # contour, canny edge
    laplacian = cv2.Laplacian(img_blur, cv2.CV_8U)
    #가장 큰 크기의 area찾기
    contours, hierarchy = cv2.findContours(laplacian, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    max = 0
    maxcnt = None
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (max < area):
            max = area
            maxcnt = cnt
    #색깔 채우기
    mask = np.zeros(laplacian.shape).astype(laplacian.dtype)
    color = [255, 255, 255]
    cv2.fillPoly(mask, [maxcnt], color)
    img_final = cv2.bitwise_and(laplacian, mask)

    # 각 area마다 네모로 감싸기
    contours, hierarchy = cv2.findContours(img_final, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        hull = cv2.convexHull(cnt)
        cv2.drawContours(img_final, [hull], 0, (255, 255, 255), 3)

    cv2.imshow('image', img_final)
    while True:
        if cv2.waitKey(0) == 27:
            cv2.destroyWindow('image')
            break
    return
"""
#Gray()


"""
def Contour():
    img = cv2.imread("jpg/overwatch275.jpg", cv2.IMREAD_COLOR)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 잡음 제거
    img_hsv = cv2.fastNlMeansDenoisingColored(img_hsv, None, 10, 10, 7, 21)
   lower = np.array([167, 30, 30], dtype="uint8")
    upper = np.array([187, 255, 255], dtype="uint8")
   #lower = np.array([115, 30, 30], dtype = "uint8")
    #upper = np.array([145, 255, 255], dtype = "uint8")
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


def test():
    distance = [[0 for col in range(5)] for row in range(3)]
    #3*5행렬?
    j = 0
    for i in range(3,9,3):
        distance[j]= [10,10,10,10,10]
        j =j+1
    print(distance)
#test()
"""