from cv_settings import *


def detect(image: mat):
    corners, tag_numbers, rejected = tag_detector.detectMarkers(img)
    if tag_numbers is not None:
        for corner_array, tag_number in zip(corners, tag_numbers):
            c: mat = corner_array.reshape(4, 2).astype(int)
            middles = [(c[i] + c[(i + 1) % 4]) // 2 for i in range(4)]

            upper_middle = None
            upper_middle_index = 0
            min_point_y = float('inf')
            i = 0
            for point in middles:
                if point[1] < min_point_y:
                    min_point_y = point[1]
                    upper_middle = point
                    upper_middle_index = i
                i += 1
            # DEBUG
            center = sum(c) // 4
            for i in range(len(middles)):
                try:
                    cv.putText(image, f"{upper_middle_index}", upper_middle, fontFace=font, fontScale=1,
                               color=(0, 0, 255), thickness=3)
                except ValueError:
                    print(upper_middle)
                cv.putText(image, f"{tag_number[0]}", center, fontFace=font, fontScale=2, color=(0, 255, 0),
                           thickness=4)


vid = cv.VideoCapture(1)

go_on = True
while go_on:

    _, img = vid.read()
    detect(img)
    cv.imshow("result", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        go_on = None
