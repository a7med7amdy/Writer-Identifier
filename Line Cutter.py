import numpy as np
import cv2

gray = cv2.imread('formsA-D/a02-111.png')
edges = cv2.Canny(gray,90,100,apertureSize = 3)
minLineLength=55
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=0)

linesNew=[ line[0][1] for line in lines if line[0][1]==line[0][3]]
linesNew=sorted(linesNew)
finalList=[linesNew[0]]
for i in range(1,len(linesNew)):
    if linesNew[i]-linesNew[i-1]>=100:
        finalList.append(linesNew[i])
io.imshow(gray[finalList[1]:finalList[2],:])
gray=gray[finalList[1]:finalList[2],:]
