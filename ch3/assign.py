import cv2 as cv
import numpy as np

# 이미지 로드
image = cv.imread('img_1.png')

skin_imageY = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
skin_imageH = cv.cvtColor(image, cv.COLOR_BGR2HSV)

while True:
    cv.imshow('Img', image)
    key = cv.waitKey(1) & 0xFF

    if key == ord('y'):
        lower_range = np.array([0, 133, 77])
        upper_range = np.array([255, 173, 127])

        skin_mask = cv.inRange(skin_imageY, lower_range, upper_range)
        result = cv.bitwise_and(image, image, mask=skin_mask)
        cv.imshow('Skin Detection Y', result)

    elif key == ord('h'):
        lower_range = np.array([0, 70, 50])
        upper_range = np.array([50, 150, 255])

        skin_mask = cv.inRange(skin_imageH, lower_range, upper_range)
        result = cv.bitwise_and(image, image, mask=skin_mask)
        cv.imshow('Skin Detection HSV', result)

    elif key == ord('q'):
        break

cv.destroyAllWindows()

