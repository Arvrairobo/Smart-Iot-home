import cv2
import numpy as np

class CoordinateStore:
    def __init__(self):
        self.points = []
        self.cropping = False

    def select_point(self,event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                self.points.append((x,y))
                self.cropping = True
CS1 = CoordinateStore()
img = cv2.imread('/home/kush/485475478454/gdfg.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image', CS1.select_point)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == ord('c'):
        for i in range(0, len(CS1.points), 1):
            roi = img[CS1.points[i - 1][1]: CS1.points[i][1],CS1.points[i - 1][0]: CS1.points[i][0]]
            rect = cv2.rectangle(img, CS1.points[i - 1], CS1.points[i], -1)
            img2gray = cv2.cvtColor(rect, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(img2gray, 120, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            cv2.imwrite('/home/kush/Desktop/licence_plate_image/rect100.jpg', roi)
    if k == 27:
        print len(CS1.points)
        break
cv2.destroyAllWindows()


print "Selected Coordinates: "
for i in CS1.points:
    print i