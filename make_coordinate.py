import numpy as np
import cv2
import math

drawing = False
ix, iy = -1, -1

x_up, x_down, y_up, y_down = 0, 0, 0, 0

def onMoush(event, x, y, flags, param):
    global ix, iy, drawing, x_up, x_down, y_up, y_down

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        x_up, y_up = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(param, (ix, iy), (x, y), (0, 0, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(param, (ix, iy), (x, y), (0, 0, 0), -1)
        x_down, y_down = x, y

def moushBrush(img_path):
    img = cv2.imread(img_path)
    cv2.namedWindow('draw_box')
    cv2.setMouseCallback('draw_box', onMoush, param=img)

    while True:
        cv2.imshow('draw_box', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    moushBrush('data/overwatch/frame00617.jpg')
    print("(%f, %f), (%f, %f)" % (x_up, y_up, x_down, y_down))
    print("X %.2f Y %.2f" % ((x_up + x_down) / 2, (y_up + y_down) / 2))