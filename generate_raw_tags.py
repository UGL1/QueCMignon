from temp_tests.cv_settings import *



def generate_and_save_aruco_tag(tag_number: int, tag_size=500) -> None:
    tag_mat = np.zeros((tag_size, tag_size, 1), dtype="uint8")
    cv2.aruco.generateImageMarker(aruco_dict, tag_number, tag_size, tag_mat, 1)
    tag_name = f"raw_aruco_markers/{str(tag_number).zfill(2)}.png"
    cv2.imwrite(tag_name, tag_mat)


for i in range(1, 36):
    generate_and_save_aruco_tag(i)
