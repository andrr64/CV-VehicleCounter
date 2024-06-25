import cv2
from ultralytics import YOLO, solutions
from datetime import datetime as dt
from copy import deepcopy

def yoloCounting(videoLink, mode : bool) -> dict:
    model = YOLO("yolov8n.pt")
    footageVideo = cv2.VideoCapture(videoLink)
    assert footageVideo.isOpened(), "Error reading video file"

    # fV = footage video
    fV_width, fV_height, fV_fps = (int(footageVideo.get(x)) for x in (cv2.
    CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    
    # garis hitung
    line_points = [(0, int(fV_height/2) + 20), (fV_width, int(fV_height/2) + 20)]
    counter = solutions.ObjectCounter(
        view_img=mode,
        reg_pts=line_points,
        classes_names=model.names,
        draw_tracks=True,
        line_thickness=2,
)

    # Loop untuk membaca setiap frame video
    while footageVideo.isOpened():
        success, im0 = footageVideo.read()
        if not success:
            print("Video frame is empty or video processing has been successfully completed.")
            break

        # Melacak objek dalam frame
        tracks = model.track(im0, persist=True, show=False)

        # Memulai perhitungan objek
        im0 = counter.start_counting(im0, tracks)

    # Melepas sumber daya
    footageVideo.release()
    cv2.destroyAllWindows()
    raw_data = counter.class_wise_count
    filtered_data = {key: value for key,value in raw_data.items() if value['IN'] != 0 and value['OUT'] != 0}
    return deepcopy(filtered_data)