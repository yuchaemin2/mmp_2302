import cv2 as cv
import numpy as np

def embossing(img):
    femboss = np.array([[-1.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0],
                        [0.0, 0.0, 1.0]])

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray16 = np.int16(gray) # gray는 1바이트(8bits) => 16bit
    # int8로 음수를 표현하는 경우 -128~127까지만 표현 가능
    emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))

    return emboss

#     def cartoonFunction(self):
#         self.cartoon=cv.stylization(self.img,sigma_s=60,sigma_r=0.45)
#         cv.imshow('Cartoon',self.cartoon)
#
#     def sketchFunction(self):
#         self.sketch_gray,self.sketch_color=cv.pencilSketch(self.img,sigma_s=60,sigma_r=0.07,shade_factor=0.02)
#         cv.imshow('Pencil sketch(gray)',self.sketch_gray)
#         cv.imshow('Pencil sketch(color)',self.sketch_color)
#
#     def oilFunction(self):
#         self.oil=cv.xphoto.oilPainting(self.img,10,1,cv.COLOR_BGR2Lab)
#         cv.imshow('Oil painting',self.oil)

def cartoon(img):
    cartoon = cv.stylization(img, sigma_s=60, sigma_r=0.45)
    return cartoon

def pencilGray(img):
    sketch_gray, _ = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
    return sketch_gray

def pencilColor(img):
    _, sketch_color = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
    return sketch_color

def oilPainting(img):
    oil = cv.xphoto.oilPainting(img, 10, 1, cv.COLOR_BGR2Lab)
    return oil

def enhance(img):
    detail = cv.detailEnhance(img, sigma_s=10, sigma_r=0.15)
    return detail