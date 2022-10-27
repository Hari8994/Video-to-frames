import cv2
import numpy as np
import glob
import os
from tqdm import tqdm
 
img_array = []
image_files = [f for f in glob.glob(r'E:\MCET\HARI MCET\croped_videos\Video_annotation_samples\1_101' "/**/*", recursive=True) if not os.path.isdir(f)]
image_files.sort(key=os.path.getctime)
for filename in tqdm(image_files, total=len(image_files)):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('project101_1.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 25, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()