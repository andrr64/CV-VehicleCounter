from ultralytics import YOLO
from ultralytics.solutions import object_counter
import cv2
import torch
from datetime import datetime as dt

def yoloCounting(videoLink, mode: bool) -> dict:
    if torch.cuda.is_available():
        model = YOLO("yolov8n.pt").to('cuda')
        # ... (rest of your CUDA-enabled code)
    else:
        model = YOLO("yolov8n.pt")  # Use CPU for inference if no GPU
        # ... (rest of your CPU-compatible code)
        print("Warning: CUDA not available, using CPU for inference.")

    footageVideo = cv2.VideoCapture(videoLink)
    assert footageVideo.isOpened(), "Error reading video file"

    # fV = footage video
    fV_width, fV_height, fV_fps = (int(footageVideo.get(x)) for x in (cv2.
    CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    
    # garis hitung
    line_points = [(10, int(fV_height/2)), (fV_width-10, int(fV_height/2))]
    counter = object_counter.ObjectCounter(
        view_img=False,
        reg_pts=line_points,
        classes_names=model.names,
        draw_tracks=True,
        line_thickness=2
    )

    # Target ukuran HD
    target_width = 1280
    target_height = 720

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

        # Mengubah ukuran frame ke HD
        im0_resized = cv2.resize(im0, (target_width, target_height))

        if mode:
            cv2.imshow('Video', im0_resized)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Melepas sumber daya
    footageVideo.release()
    cv2.destroyAllWindows()
    raw_data = counter.class_wise_count
    filtered_data = {key: value for key, value in raw_data.items() if value['IN'] != 0 or value['OUT'] != 0}
    return filtered_data
