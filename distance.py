import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('d.png')
imgray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thr = cv2.threshold(imgray, 127,255,cv2.THRESH_BINARY)[1]

contours,_ = cv2.findContours(thr,2,1)

cnt = contours[-1]
# cnt


hull = cv2.convexHull(cnt)
cv2.drawContours(img, [hull],0, (0,0,255),2)

hull = cv2.convexHull(cnt,returnPoints=False)
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start =tuple(cnt[s][0])
    end =tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 255, 0], 4)
    cv2.circle(img, far, 5, [255, 0, 0], 10)
plt.imshow(img)
plt.axis('off')
plt.show()

dist = cv2.pointPolygonTest(cnt, (500,250), True) # contour된 물체와 지정한 점 사이의 거리, 추후에 에임의 위치로 좌표를 지정
cv2.circle(img, (50,50),3, (255,0,0), 10)
plt.imshow(img)
plt.show()

print("Contour와 점의 거리 : {0:.2f}".format(dist))
