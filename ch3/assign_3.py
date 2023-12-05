import cv2 as cv
import numpy as np

img = cv.imread('img_1.png')

rows, cols = img.shape[:2]

current_rotation = 0  # 현재 회전 각도

def rotate_image(clockwise):
    global img, current_rotation

    if clockwise:
        current_rotation += 90
    else:
        current_rotation -= 90

    current_rotation %= 360

    if current_rotation == 90:
        src_points = np.float32([[0,0], [0, rows-1], [cols-1,0]])
        dst_points = np.float32([[0, cols-1], [rows-1, cols-1], [0, 0]])
    elif current_rotation == 180:
        src_points = np.float32([[0,0], [0, rows-1], [cols-1,0]])
        dst_points = np.float32([[cols-1, rows-1], [cols-1, 0], [0, rows-1]])
    elif current_rotation == 270:
        src_points = np.float32([[0,0], [0, rows-1], [cols-1,0]])
        dst_points = np.float32([[rows-1, 0], [0, 0], [rows-1, cols-1]])
    else:  # 0도 회전
        return

    affine_matrix = cv.getAffineTransform(src_points, dst_points)
    img_rotated = cv.warpAffine(img, affine_matrix, (rows, cols))

    cv.imshow('Rotated Image', img_rotated)

def mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        rotate_image(False)  # 시계 반대 방향으로 90도 회전
    elif event == cv.EVENT_RBUTTONDOWN:
        rotate_image(True)   # 시계 방향으로 90도 회전

cv.imshow('Original', img)
cv.setMouseCallback('Original', mouse_callback)

cv.waitKey()
cv.destroyAllWindows()
