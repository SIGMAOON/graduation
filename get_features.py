import numpy as np
import cv2
# import argparse

from math import sqrt

""" calculate distance """
def cal_dist(output_name, center_x, center_y):
    # load size of image
    # img = cv2.imread('data/overwatch/frame00000.jpg')
    # height, width, color = img.shape
    #
    # # location of center
    # center_x, center_y = width / 2, height / 2

    # open output.txt
    f = open(f'output/{output_name}.txt', 'r')

    count = 0   # count of images
    labels = []; label = []; first = True
    features = np.empty((0, 10), float)   # numpy array of features
    for line in f.readlines():
        if line[0] == 'I':
            if first: label = []; first = False
            else:
                labels.append(label); label = []
                count += 1
        else:
            tmp = list(line.split())
            if tmp[1] == 'kill':
                feature = np.full(10, -1.0)  # feature of each kills

                # minimum distance of before frame
                before_label = labels[count - 1]

                # if label is empty
                if len(before_label) == 0:
                    pass
                else:
                    sorted_dist = sorted(before_label, key=lambda x: x[1])
                    tracking_obj = sorted_dist[0][0]
                    feature[0] = sorted_dist[0][1]

                    # before 9 frames
                    index_feature = 1
                    while index_feature < 10:
                        tmp = labels[count - index_feature - 1]
                        for l in tmp:
                            if l[0] == tracking_obj:
                                feature[index_feature] = l[1]
                        index_feature += 1

                    features = np.append(features, np.array([feature]), axis=0)

            else:
                dist = sqrt((center_x - float(tmp[3]))**2 + (center_y - float(tmp[5]))**2)
                label.append((tmp[1], dist))

    f.close()

    print(features)
    np.save(f'output/{output_name}_features', features)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--output_name", type=str, default='output', help='name of output test file')
    # parser.add_argument("--center_x", type=float, default=960.0, help='center of x')
    # parser.add_argument("--center_y", type=float, default=540.0, help='center of y')
    # opt = parser.parse_args()

    # cal_dist(opt.output_name, opt.center_x, opt.center_y)

    cal_dist("output", 960.0, 540.0)