!pip install ultralytics
!pip install supervision
!pip install roboflow
!{sys.executable} -m pip install 'git+https://github.com/facebookresearch/segment-anything.git'
!wget -q https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth

import numpy as np
import cv2
import os
import sys
import torch

#ROBOFLOW
from roboflow import Roboflow
rf = Roboflow(api_key="Pho4XVVaJnNcR3y3HNrK")
project = rf.workspace("team12").project("airplane-bp8fl")
dataset = project.version(2).download("yolov8")

# YOLO
from ultralytics import YOLO
yolo_model = YOLO('yolov8x.pt')

# SEGMENT-Anything
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
import supervision as sv

DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
MODEL_TYPE = "vit_l"

CHECKPOINT_PATH = os.path.join("sam_vit_l_0b3195.pth")
sam = sam_model_registry[MODEL_TYPE](checkpoint=CHECKPOINT_PATH).to(device=DEVICE)

mask_predictor = SamPredictor(sam)

# Run Code

VIDEO_SOURCE = '/content/airplane2.mp4'
VIDEO_DESTINATION = '/content/result2.avi'

# Video kaynağını aç
cap = cv2.VideoCapture(VIDEO_SOURCE)

# Video kaydedicisini ayarla
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
FPS = 30.0
out = cv2.VideoWriter(VIDEO_DESTINATION, fourcc, FPS, (width, height))

while True:
    # Frame oku
    ret, frame = cap.read()

    # Okuma başarısızsa video bitti
    if not ret:
        break

    # Girdi frame'ini SuperAnnotate'e uygun formata getir
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = yolo_model.predict(source=frame)
    
    boxes_class_name = np.array([])
    for r in results:
        for c in r.boxes.cls:
            boxes_class_name = np.append(boxes_class_name,yolo_model.names[int(c)])
    boxes_class_name

    k = 0
    result_np_son = np.array([])
    result_class = np.array([])
    result_score = np.array([])
    for result in results:
        result_np = np.array(result.boxes.data.cpu())

    for i in result_np:
        result_np_son = np.append(result_np_son,i[:][:-2])
        result_class = np.append(result_class,i[:][-1:])
        result_score = np.append(result_score,i[:][-2:-1])
        k += 1


    boxes = result_np_son.reshape((k,4))
    boxes_class = result_class.reshape((k,))
    boxes_score = result_score.reshape((k,))


    segmented_image = frame.copy()
    box_image = frame.copy()
    boxes_class_value = {'0':sv.Color.white(),
                         '1':sv.Color.blue(), 
                         '2':sv.Color.blue(),
                         '3':sv.Color.blue(),
                         '4':sv.Color.red(),
                         '5':sv.Color.blue(),
                         '7':sv.Color.black(),
                         '8':sv.Color.green(),
                         '9':sv.Color.blue(),
                         '37':sv.Color.blue()}
    mask_predictor.set_image(frame)

    boxes = result.boxes.xyxy
    if len(boxes) != 0:
      masks, scores, logits = mask_predictor.predict_torch(
          point_coords = None,
          point_labels = None,
          boxes = boxes * 1040/max(frame.shape),
          multimask_output=True
      )

      masks = masks.cpu().numpy()

      i = 0
      for box in boxes.cpu().numpy():

          box_annotator = sv.BoxAnnotator(color= boxes_class_value[str(int(boxes_class[i]))], text_padding=10)
          mask_annotator = sv.MaskAnnotator(color= boxes_class_value[str(int(boxes_class[i]))])

          detections = sv.Detections(
              xyxy=sv.mask_to_xyxy(masks=masks[i]),
              mask=masks[i]
          )
          
          detections = detections[detections.area == np.max(detections.area)]
          box_image = box_annotator.annotate(scene=box_image, detections=detections, skip_label=True)
          segmented_image = mask_annotator.annotate(scene=segmented_image, detections=detections)
          i += 1   

    # Video kaydediciye yaz
    out.write(cv2.cvtColor(segmented_image, cv2.COLOR_RGB2BGR))

# Video kaynak ve kaydediciyi serbest bırak
cap.release()

