import cv2 as cv
import numpy as np
import math

# 초기 설정
drawing = True  # 그림 그리기 모드
ix, iy = -1, -1  # 시작점 좌표

# 색상 정의
white = (255, 255, 255)
green = (0,255,0)
blue = (255, 0, 0)
red = (0, 0, 255)
BrushSiz=5					# 붓의 크기
LColor,RColor=(255,0,0),(0,0,255)		# 파란색과 빨간색

# 이미지 생성
img = np.ones((600, 900, 3), dtype=np.uint8) * 255  # 흰색 이미지

def draw_shape(event, x, y, flags, param):
    global ix, iy

    if flags & cv.EVENT_FLAG_SHIFTKEY:
        if event==cv.EVENT_LBUTTONDOWN:	
            ix,iy=x,y
        elif event==cv.EVENT_LBUTTONUP:	
            cv.line(img,(ix,iy),(x,y),green,2)

    elif flags & cv.EVENT_FLAG_ALTKEY:
        if event==cv.EVENT_LBUTTONDOWN:	
            ix,iy=x,y
        elif event==cv.EVENT_LBUTTONUP:	
            cv.rectangle(img,(ix,iy),(x,y),red,2)
        elif event==cv.EVENT_RBUTTONDOWN:
            ix,iy=x,y
        elif event==cv.EVENT_RBUTTONUP: #직사각형 채우기
            cv.rectangle(img,(ix,iy),(x,y),blue,-1) 

    elif flags & cv.EVENT_FLAG_CTRLKEY:
        if event==cv.EVENT_LBUTTONDOWN:	
            ix,iy=x,y
        elif event==cv.EVENT_LBUTTONUP:	
            cv.circle(img,(ix, iy), pd(ix,iy,x,y), blue, 2)
        elif event==cv.EVENT_RBUTTONDOWN:
            ix,iy=x,y
        elif event==cv.EVENT_RBUTTONUP: #원 채우기
            cv.circle(img,(ix,iy), pd(ix,iy,x,y), red, -1) 

    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),BrushSiz,LColor,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),BrushSiz,RColor,-1)
    

def pd(ix,iy, x,y):
    a = x - ix
    b = y - iy
    c = math.sqrt((a*a)+(b*b))
    return int(c)


# OpenCV 창 생성 및 마우스 콜백 함수 설정
cv.namedWindow('Drawing')
cv.setMouseCallback('Drawing', draw_shape)

while True:
    cv.imshow('Drawing', img)
    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('b'):
        img[:] = 255  # 이미지 초기화

cv.destroyAllWindows()
