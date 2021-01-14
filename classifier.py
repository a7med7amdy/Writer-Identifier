import cv2
import numpy as np
# import matplotlib.pyplot as plt 
import skimage.io as io
from sklearn import svm
import os
import collection

def classifier(path):
    features = []
    labels = []
    # path = 'data'
    for root, dirs, files in os.walk(path):
        for d in dirs:
            print(path + d + '/')
            for root1, dir1s, file1s in os.walk(path +'/'+ d + '/'):
                for d1 in dir1s:
                    for root2, dir2s, file2s in os.walk(path +'/'+ d + '/'+ d1+'/'):
                        print(" "+path+d+d1)
                        for filename in file2s:
                            print(path +'/'+ d + '/' + d1 + '/' + filename)
                            image = cv2.imread(path +'/'+ d + '/' + d1 + '/' + filename)
                            image2 = collection.cutLines(image)
                            images = collection.lines_segments(image2)
                            feature = collection.LBP(images)
                    
                            features.append(feature)
                            labels.append(d) 
                        break           
                break
        break              


    classifier = svm.SVC(C=5.0, gamma='auto', probability=True)
    classifier.fit(features, labels)
