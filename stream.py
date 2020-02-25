import cv2 as cv
import matplotlib.pyplot as plt
import time
import datetime


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


def save_file_locally(frame):
    # Saves images.
    name = f"/home/paul/Desktop/images/{index}.jpg"
    print('Creating...' + name)
    cv.imwrite(name, frame)


def sift():
    img1 = cv.imread('box.png', cv.IMREAD_GRAYSCALE)  # queryImage
    img2 = cv.imread('box_in_scene.png', cv.IMREAD_GRAYSCALE)  # trainImage
    # Initiate SIFT detector
    sift = cv.xfeatures2d.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)  # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    # Need to draw only good matches, so create a mask
    matchesMask = [[0, 0] for i in range(len(matches))]
    # ratio test as per Lowe's paper
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7 * n.distance:
            matchesMask[i] = [1, 0]
    draw_params = dict(matchColor=(0, 255, 0),
                       singlePointColor=(255, 0, 0),
                       matchesMask=matchesMask,
                       flags=cv.DrawMatchesFlags_DEFAULT)
    img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
    plt.imshow(img3, ), plt.show()


index = 0
# Set video file path of input video with name and extension.
vid = cv.VideoCapture(0)
while True:
    ret, frame = vid.read()
    save_file_locally(frame) if ret else 0
    index += 1
