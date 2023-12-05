import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('soccer.jpg') 
h=cv.calcHist([img],[2],None,[256],[0,256]) # 2Î≤? Ï±ÑÎÑê?ù∏ R Ï±ÑÎÑê?óê?Ñú ?ûà?ä§?Ü†Í∑∏Îû® Íµ¨Ìï®
plt.plot(h,color='r',linewidth=1)

plt.show()