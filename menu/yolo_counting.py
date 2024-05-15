from ultralytics import YOLO
from ultralytics.solutions import object_counter
import cv2
from datetime import datetime as dt

def yoloCounting(videoLink, date : dt):
    model = YOLO("yolov8n.pt")
    footageVideo = cv2.VideoCapture(videoLink)
    assert footageVideo.isOpened(), "Error reading video file"

    # fV = footage video
    fV_width, fV_height, fV_fps = (int(footageVideo.get(x)) for x in (cv2.
    CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    
    # garis hitung
    line_points = [(10, int(fV_height/2)), (fV_width-10, int(fV_height/2))]
    video_writer = cv2.VideoWriter(f"asd.avi",
                               cv2.VideoWriter_fourcc(*'mp4v'),
                               fV_fps,
                               (fV_width, fV_height))
    counter = object_counter.ObjectCounter()
    counter.set_args(view_img=True,
                 reg_pts=line_points,
                 classes_names=model.names,
                 draw_tracks=True)
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

        # Menulis frame yang telah diproses ke video output
        video_writer.write(im0)

    # Melepas sumber daya
    footageVideo.release()
    video_writer.release()
    cv2.destroyAllWindows()
    return [counter.out_counts, counter.in_counts]