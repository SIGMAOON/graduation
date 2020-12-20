import os
import cv2

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
    print("-- Write name of video: data/video/", end='')
    path = input()

    # load_video(opt.video_path)
    load_video(path)
    for file in os.scandir('output/overwatch/'):
        os.remove(file.path)
    print("-----------------------------------------------------------------------------------")\