import os
import cv2
import detect, get_features, linear_regression

""" load video and save frame """
def load_video(video):
    print("-- Loading Video ...")

    # remove all files in overwatch directory
    for file in os.scandir('data/overwatch/'):
        os.remove(file.path)

    # save frames
    vidcap = cv2.VideoCapture(video)

    count = 0
    while(vidcap.isOpened()):
        ret, image = vidcap.read()

        if ret:
            cv2.imwrite('data/overwatch/frame%05d.jpg' % count, image)
            print('saved data/overwatch/frame%05d.jpg' % count)
            count += 1
        else:
            print("-- Save Frame Complete!")
            break

    vidcap.release()

""" run detect.py """
def run():
    os.system('python detect.py')

if __name__ == '__main__':
    # load video and get frames
    print("-- Write name of video: data/video/", end='')
    video = input()
    video_path = f"data/video/{video}"

    # load_video(opt.video_path)
    load_video(video_path)
    for file in os.scandir('output/overwatch/'):
        os.remove(file.path)
    print("-- Complete get frames")
    print("-----------------------------------------------------------------------------------")


    # run YOLO
    print("\n-- Write name of weights file: weights/", end='')
    file = input()
    file_path = f"weights/{file}"

    detect.run(file_path)
    os.system(f"python detect.py --weights_path {file_path}")
    print("-----------------------------------------------------------------------------------")


    # get features
    print("\n-- Getting features ...")
    get_features.cal_dist("output", 960.0, 540.0)
    print("-- Complete get features")
    print("-----------------------------------------------------------------------------------")


    # classify
    print("\n-- Classifying ...")
    linear_regression.run()