import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('soccer.jpg') 
h=cv.calcHist([img],[2],None,[256],[0,256]) # 2λ²? μ±λ?Έ R μ±λ?? ??€? κ·Έλ¨ κ΅¬ν¨
plt.plot(h,color='r',linewidth=1)

plt.show()