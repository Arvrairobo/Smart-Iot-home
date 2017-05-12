import cv2
import glob, os
import numpy as np
import subprocess
path = '/home/kush/pks/'
im = glob.glob(os.path.join(path, '*'))
cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)
e1 = cv2.getTickCount()
a = subprocess.call(['eog','--slide-show', path])
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print t, image
