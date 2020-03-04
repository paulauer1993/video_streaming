import datetime
import time
import cv2 as cv
from threading import Thread
import re
import subprocess


def get_l():
    image = cv.imread("/home/paul/Desktop/images/0.jpeg")
    height = int(image.shape[1])
    width = int(image.shape[0])
    return height, width


# Decorator
def timeit(method):
    def timed(*args, **kw):
        ts = datetime.datetime.now().strftime("%H:%M:%S:%f")
        print(f'> > >Thread {method.__name__} started running: {ts}')
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print(f'> > >Thread {method.__name__} took {te-ts} seconds to complete')
        return result
    return timed


def start_video_capture():
    vid = cv.VideoCapture(0)
    return vid


def video_capture(vid):
    ret, frame = vid.read()
    cv.imwrite("/home/paul/Desktop/images/0.jpeg", frame) if ret else None


def stop_video_capture(vid):
    vid.release()


def start_processes():
    a = 0.0
    height, width = get_l()
    vid = start_video_capture()
    while a < 85.0:
        video_capture(vid)
        a = crop_and_compare_images(height, width)
    stop_video_capture(vid)
    print(a)


def compare_screens(original_screen, current_screen):
    output = subprocess.getoutput(f"/home/paul/video/imageCompareEngine/build/imageCompare {original_screen} {current_screen}")
    print(float(output))
    return float(output)


def calculate_average(lst):
    return sum(lst) / len(lst)


@timeit
def crop_and_compare_images(height, width):
    image = cv.imread("/home/paul/Desktop/images/0.jpeg")
    t1 = Thread(target=cv.imwrite, args=("/home/paul/Desktop/cropped_new/cropped_1.jpeg", image[0: width // 2, 0: height // 2])).start()
    t2 = Thread(target=cv.imwrite, args=("/home/paul/Desktop/cropped_new/cropped_1.jpeg", image[width // 2: width, height // 2: height])).start()
    t3 = Thread(target=cv.imwrite, args=("/home/paul/Desktop/cropped_new/cropped_1.jpeg", image[0: width // 2, 0: height // 2])).start()
    s1 = compare_screens("/home/paul/Desktop/cropped/cropped_1.jpeg", "/home/paul/Desktop/cropped_new/cropped_1.jpeg")
    s2 = compare_screens("/home/paul/Desktop/cropped/cropped_2.jpeg", "/home/paul/Desktop/cropped_new/cropped_2.jpeg")
    s3 = compare_screens("/home/paul/Desktop/cropped/cropped_3.jpeg", "/home/paul/Desktop/cropped_new/cropped_3.jpeg")
    t1.join(), t2.join(), t3.join()
    print((s1 + s2 + s3) // 3)
    return (s1 + s2 + s3) // 3


start_processes()
