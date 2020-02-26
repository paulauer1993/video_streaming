import datetime
import time
import cv2 as cv
import threading
import re
import subprocess

location = f"/home/paul/Desktop/images/da.jpg"
original_screen = "path"
current_screen = "path2"


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


# HLK
def go_route(route):
    if route == 1:
        pass
    elif route == 2:
        pass
    else:
        pass
    return route


def start_stop_video_capture(trigger=True):
    index = 0
    vid = cv.VideoCapture(0)
    while trigger:
        ret, frame = vid.read()
        cv.imwrite(location, frame) if ret else None
        index += 1
    vid.release()


def crop_image(path, route):
    image = cv.imread(f"{location}")
    if route == 1:
        height = image.shape[0] // 2
        width = image.shape[1]
    elif route == 2:
        pass
    else:
        pass
    crop_start = 0
    crop_finish = width // 4
    for _ in range(1, 5):
        cropped_image = image[0:height, crop_start:crop_finish]
        cv.imwrite(f"{path}/cropped_{_}.jpeg", cropped_image)


def timer(t0, t1):
    lst = []
    lst.append(t0 - t1)


def start_threads():
    p1 = threading.Thread(target=go_route)
    while compare_screens("", "") < 85:
        p2 = threading.Thread(target=start_stop_video_capture)
        p3 = threading.Thread(target=crop_image)
        p4 = threading.Thread(target=compare_screens)
    p5 = threading.Thread(target=timer)


def compare_screens(original_screen, current_screen):
    output = subprocess.getoutput(f"/home/paul/video/imageCompareEngine/build/imageCompare {original_screen} {current_screen}").split()
    similarity = re.findall(r"\d+", output[1])
    return int(similarity[0])


# HLK
def calculate_average(lst):
    return sum(lst) / len(lst)

# ./imageCompare ../sample.jpg ../sample.jpg
