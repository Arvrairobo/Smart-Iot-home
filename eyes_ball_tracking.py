import numpy as np
import cv2
import time
import dlib
from scipy.spatial import distance as dist
from imutils import face_utils

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3
COUNTER = 0
TOTAL = 0
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear


# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('/home/kush/shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture("/home/kush/Ad/ad2.mp4")  # 640,480

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        # downsample
        # frameD = cv2.pyrDown(cv2.pyrDown(frame))
        # frameDBW = cv2.cvtColor(frameD,cv2.COLOR_RGB2GRAY)

        # detect face
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier('/home/kush/opencv-3.1.0/data/haarcascades_cuda/haarcascade_eye_tree_eyeglasses.xml')
        detected = faces.detectMultiScale(frame, 1.3, 5)
        rects = detector(gray, 0)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 20, param1=30, param2=20, minRadius=1, maxRadius=5)

        # loop over the face detections
        for rect in rects:
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # extract the left and right eye coordinates, then use the
            # coordinates to compute the eye aspect ratio for both eyes
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            # average the eye aspect ratio together for both eyes
            ear = (leftEAR + rightEAR) / 2.0
            # compute the convex hull for the left and right eye, then
            # visualize each of the eyes
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
            # check to see if the eye aspect ratio is below the blink
            # threshold, and if so, increment the blink frame counter
            if ear < EYE_AR_THRESH:
                COUNTER += 1

            # otherwise, the eye aspect ratio is not below the blink
            # threshold
            else:
                # if the eyes were closed for a sufficient number of
                # then increment the total number of blinks
                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    TOTAL += 1

                # reset the eye frame counter
                COUNTER = 0

                # draw the total number of blinks on the frame along with
                # the computed eye aspect ratio for the frame
                cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        pupilFrame = frame
        pupilO = frame
        windowClose = np.ones((5, 5), np.uint8)
        windowOpen = np.ones((2, 2), np.uint8)
        windowErode = np.ones((2, 2), np.uint8)

        # draw square
        for (x, y, w, h) in detected:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 255, 0), 1)
            # cv2.line(frame, (x + w / 2 , y), ((x + w / 2, y + h)), (255, 255, 0), 1)
            # cv2.line(frame, (x, y + h / 2), ((x + w, y + h / 2)), (255, 255, 0), 1)
            pupilFrame = cv2.equalizeHist(gray[int(y + h * .25):(y + h), x:(x + w)])
            pupilO = pupilFrame
            ret, pupilFrame = cv2.threshold(pupilFrame, 20, 255, cv2.THRESH_BINARY)  # 50 ..nothin 70 is better
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_CLOSE, windowClose)
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_ERODE, windowErode)
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_OPEN, windowOpen)

            # so above we do image processing to get the pupil..
            # now we find the biggest blob and get the centriod

            threshold = cv2.inRange(pupilFrame, 250, 255)  # get the blobs
            image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

            # if there are 3 or more blobs, delete the biggest and delete the left most for the right eye
            # if there are 2 blob, take the second largest
            # if there are 1 or less blobs, do nothing
            if len(contours) < 0:
                cv2.putText(frame, "blink", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2)

            if len(contours) >= 2:
                # find biggest blob
                maxArea = 0
                MAindex = 0  # to get the unwanted frame
                distanceX = []  # delete the left most (for right eye)
                currentIndex = 0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    center = cv2.moments(cnt)
                    if center['m00'] != 0:
                        cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])
                    distanceX.append(cx)
                    if area > maxArea:
                        maxArea = area
                        MAindex = currentIndex
                    currentIndex = currentIndex + 1
                    cv2.putText(frame, "center", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    print "center"
                del contours[MAindex]  # remove the picture frame contour
                del distanceX[MAindex]

            if len(contours) >= 2:  # delete the left most blob for right eye
                if distanceX.index(min(distanceX)) == 1:
                    edgeOfEye = distanceX.index(min(distanceX))
                    print "edge", edgeOfEye
                    cv2.putText(frame, "right", (150, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 255, 0), 2)
                    print "right"
                else:
                    edgeOfEye = distanceX.index(max(distanceX))
                    cv2.putText(frame, "left", (280, 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (0, 255, 0), 2)
                    print "left"
                del contours[edgeOfEye]
                del distanceX[edgeOfEye]

            if len(contours) >= 1 & len(contours) <= 2 :  # get largest blob
                maxArea = 0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if area > maxArea:
                        maxArea = area
                        largeBlob = cnt

            if len(largeBlob) > 0:
                center = cv2.moments(largeBlob)
                cx, cy = int(center['m10'] / center['m00']), int(center['m01'] / center['m00'])
                cv2.circle(frame, (int(x +cx), int(y + cy + h/4)), 5, (255, 255, 255), -1)
                #cv2.circle(pupilO, (int(cx), int(cy + h / 4)), 5, (255, 255, 255), -1)
                for i in circles[0, :]:
                    cv2.circle(frame, (int(x +cx), int(y + cy + h/4)), i[2], (255, 255, 255), -1)

        # show picture
        cv2.imshow('frame', pupilO)
        cv2.imshow('frame2', pupilFrame)
    cv2.imshow('frame3', frame)
    if cv2.waitKey(1) % 0x100 == 27:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()


