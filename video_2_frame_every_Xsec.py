# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 13:01:54 2021

@author: DST project
"""

import cv2
import math
import numpy as np

# Make sure that the print function works on Python 2 and 3
# from future import print_function

# Capture every n seconds (here, n = 5) 

#################### Setting up the file ################
videoFile = r"E:\PYTHON code\1.mp4"
vidcap = cv2.VideoCapture(videoFile)
success, image = vidcap.read()

#################### Setting up parameters ################

seconds = 1
fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
print(fps)
multiplier = round(fps/seconds)
# print(multiplier)
#################### Initiate Process ################

while success:
    frameId = int(round(vidcap.get(1))) #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
    # print(frameId % multiplier)
    success, image = vidcap.read()
    # print(image)
    if frameId % multiplier == 0:
        cv2.imwrite(r"E:\PYTHON code/frame%d.jpg" % frameId, image)
        
vidcap.release()
print("Completed")