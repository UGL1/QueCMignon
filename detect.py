import cv2.aruco

from cv_settings import *




def detect(image: mat):
    corners, tag_numbers, rejected = tag_detector.detectMarkers(img)
    if tag_numbers is not None:
        for corner_array, tag_number in zip(corners, tag_numbers):
            print(corner_array.shape)
            c: mat = corner_array.reshape(4, 2).astype(int)
            print(c[0], c[2])
            cv2.line(image, c[0], c[1], color=(255, 0, 255), thickness=10)
            cv2.line(image, c[1], c[2], color=(0, 255, 0), thickness=10)
            cv2.line(image, c[2], c[3], color=(255, 0, 0), thickness=10)




vid = cv2.VideoCapture(0)

go_on = True
while go_on:

    _, img = vid.read()
    detect(img)
    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        go_on = None
