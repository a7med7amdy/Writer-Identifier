from skimage.feature import local_binary_pattern
import skimage.io as io
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.exposure import histogram
 
def cutLines(gray):
    edges = cv2.Canny(gray,90,100,apertureSize = 3)
    minLineLength=100
    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=0)
 
    linesNew=[ line[0][1] for line in lines if line[0][1]==line[0][3]]
    linesNew=sorted(linesNew)
    finalList=[linesNew[0]]
    for i in range(1,len(linesNew)):
        if linesNew[i]-linesNew[i-1]>=100:
            finalList.append(linesNew[i])
    io.imshow(gray[finalList[1]:finalList[2],:])
    return gray[finalList[1]:finalList[2],:]
 
def lines_segments(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    kernel = np.ones((5,100), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    images = []
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr) 
        roi = gray[y:y+h, x:x+w]
        if(len(roi)>25 and y+h<x+w): #20 is thershold you can change this, this is for small lines and points, remove them from return images 
            images.append(roi)
            io.imsave(str(i)+'.png',roi)
    # write
    return images
 
def LBP (images, stride = 1):
    hist = np.zeros(256)
    for img in images:
        lbp = local_binary_pattern(img, 8, 1)   #‘default’, ‘ror’, ‘uniform’, ‘var’, nri_uniform
        hist += np.asarray(histogram(lbp)).astype(int)
    return hist
 
 
image= cv2.imread('formsA-D/a02-124.png')
imageHist= LBP(lines_segments(cutLines(image)))
