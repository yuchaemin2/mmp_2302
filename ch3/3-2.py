import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('soccer.jpg') 
h=cv.calcHist([img],[2],None,[256],[0,256]) # 2�? 채널?�� R 채널?��?�� ?��?��?��그램 구함
plt.plot(h,color='r',linewidth=1)

plt.show()