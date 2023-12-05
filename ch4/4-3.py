import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg')	 # 영상 읽기
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


# canny=cv.Canny(gray,100,200) # 에지 이미지, 캐니를 구하기 위해서는 그레이로 컨벌트 시켜야 함

t, bin_gray=cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU) # 이진 영상
contour,hierarchy=cv.findContours(bin_gray,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

lcontour=[]
for i in range(len(contour)):
    if contour[i].shape[0]>80:	# 길이가 100보다 크면(숫자 조정해서 내가 원하는 컨타워 찾기)
        lcontour.append(contour[i])
    
cv.drawContours(img,lcontour,-1,(0,255,0),3)
# cv.drawContours(img, contour, -1, (0, 255, 0), 3) # 100보다 짧은 것도 다 표시

cv.imshow('Original with contours',img)    
# cv.imshow('Canny',canny)
cv.imshow('Binary', bin_gray)

cv.waitKey()
cv.destroyAllWindows()