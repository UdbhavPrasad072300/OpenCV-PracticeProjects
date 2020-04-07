#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 
import os 
  
cam = cv2.VideoCapture("IMG_7959_HEVC.mov") 
  
try:  
    if not os.path.exists('data'): 
        os.makedirs('data') 
except OSError: 
    print ('Error: Creating directory of data') 
current = 0

while(True): 
    ret,frame = cam.read() 
    if ret:  
        name = './data/f' + str(current) + '.jpg'
        print ('Created----------' + name) 
 
        cv2.imwrite(name, frame) 
  
        current += 1
    else: 
        break

cam.release()
cv2.destroyAllWindows()

