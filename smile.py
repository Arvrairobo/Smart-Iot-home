import cv2
import numpy as np
import sys
from math import sin, cos, radians


def rotate_image(image, angle):
    if angle == 0: return image
    height, width = image.shape[:2]
    rot_mat = cv2.getRotationMatrix2D((width/2, height/2), angle, 0.9)
    result = cv2.warpAffine(image, rot_mat, (width, height), flags=cv2.INTER_LINEAR)
    return result


def rotate_point(pos, img, angle):
    if angle == 0: return pos
    x = pos[0] - img.shape[1]*0.4
    y = pos[1] - img.shape[0]*0.4
    newx = x*cos(radians(angle)) + y*sin(radians(angle)) + img.shape[1]*0.4
    newy = -x*sin(radians(angle)) + y*cos(radians(angle)) + img.shape[0]*0.4
    return int(newx), int(newy), pos[2], pos[3]

facePath = "/home/kush/opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml"
smilePath = "/home/kush/Downloads/opencv-3.1.0/data/haarcascades_cuda/haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)

cap = cv2.VideoCapture(0)
cap.set(4, 480)
sF = 1.05

while True:

    ret, frame = cap.read()
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    for angle in [0, -180, 180]:
        rimg = rotate_image(img, angle)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor= sF,
            minNeighbors=8,
            minSize=(55, 55)
        )
        if len(faces):
            faces = [rotate_point(faces[-1], img, -angle)]
            break
    # ---- Draw a rectangle around the faces

    for (x, y, w, h) in faces[-1:]:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.7,
            minNeighbors=22,
            minSize=(25, 25)
            )

        # Set region of interest for smiles
        for (x, y, w, h) in smile:
            print "Found", len(smile), "smiles!"
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
            cv2.imwrite('/home/kush/Smile_Face.jpg', img)
            #print "!!!!!!!!!!!!!!!!!"

    #cv2.cv.Flip(frame, None, 1)
    cv2.imshow('Smile Detector', frame)
    c = cv2.waitKey(1) % 0x100
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()




