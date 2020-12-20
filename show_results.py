import cv2
import numpy as np
import glob

if __name__ == "__main__":
    # img_array = []
    # for filename in glob.glob('output/overwatch/*.png'):
    #     img = cv2.imread(filename)
    #     height, width, layers = img.shape
    #     size = (width, height)
    #     img_array.append(img)
    #
    # out = cv2.VideoWriter('no_hack.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
    # for i in range(len(img_array)):
    #     out.write(img_array[i])
    #
    # out.release()

    for file in glob.glob('output/overwatch/*.png'):
        img = cv2.imread(file)
        img = cv2.resize(img, dsize=(0, 0), fx=1.5, fy=1.5)

        cv2.imshow('no_hack', img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()