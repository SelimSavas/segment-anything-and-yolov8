# Segment Anything and YoloV8 Collaboration

This project is a collaboration between Segment Anything and YOLOv8 algorithms, focusing on object segmentation. The goal of the project is to automatically identify and segment objects in images, providing region-specific highlights.

![image](https://github.com/SelimSavas/segment-anything-and-yolov8/assets/48186387/bfe8f1ca-6fb8-4fab-93bd-c3d6fd182408)

**Note"": Also, if you want to segment low light images by illuminating them, you can refer to my [Low-light-segmentation](https://github.com/SelimSavas/low-light-segmentation-with-mirnet-yolov8-segment-anything) work.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jCgiaBe1ony_uXr-tscMsQStrD6-jfMr#scrollTo=LWfVExQJTK5w)

## Installation
To run this project locally, please follow the steps below:

1. Clone this repository:

```
!git clone https://github.com/SelimSavas/segment-anything-and-yolov8.git
```

2. Install the required dependencies (Do this if you are using colab. If you are working in your external environment, pay special attention to the installations required):

```
!pip install -r requirements.txt
```

3. Run the project:

To perform image segmentation, you can use the provided Colab notebook: [SAMandYOLOv8.ipynb](https://github.com/SelimSavas/segment-anything-and-yolov8/SAMandYOLOv8.ipynb).

For video segmentation, you can utilize the Colab notebook: [SAMandYOLOv8video.ipynb](https://github.com/SelimSavas/segment-anything-and-yolov8/SAMandYOLOv8video.ipynb).

If you prefer to run the video segmentation on your own local environment, execute the following command:
```
!python SAMandYOLOv8video.py
```

## Results

Here are some example results from the project:

**Image Segmentation**

![image](https://user-images.githubusercontent.com/48186387/234813581-e1d3f070-3e92-46c5-99f1-0460c422fbd7.png)


**Video Segmentation**

https://user-images.githubusercontent.com/48186387/234838019-724f8e8f-8cb6-432d-8609-bb18603f132a.mp4


## Contributing

Contributions to this project are always welcome. If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.


## License

This project is licensed under the [Apache Licene](https://github.com/SelimSavas/segment-anything-and-yolov8/blob/main/LICENSE). See the LICENSE file for more information.


## Acknowledgements

We would like to express our gratitude to the creators of [Segment Anything](https://github.com/facebookresearch/segment-anything) and [YOLOV8](https://github.com/ultralytics/ultralytics) for their invaluable contributions to the field of computer vision and object segmentation.


## Contact

For any questions or inquiries, please contact **16savasselim@gmail.com**

Feel free to explore and use this project for your own applications. Happy segmenting!

You can throw a **star** to support.

