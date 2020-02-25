import datetime
import time
import cv2 as cv
import threading


# Decorator.
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


def crop_image(index, crop_start, crop_finish):
    cropped = image[0:height, crop_start:crop_finish]
    cv.imwrite(f"/home/paul/Desktop/images/cropped_{index}.jpeg", cropped)


@timeit
def main():
    crop_start = 0
    crop_finish = width // 4
    for _ in range(1, 5):
        crop_image(_, crop_start, crop_finish)
        crop_start += width // 4
        crop_finish += width // 4


image = cv.imread("/home/paul/video/imageCompareEngine/poza.JPEG")
height = image.shape[0] // 2
width = image.shape[1]

while True:
    main()
