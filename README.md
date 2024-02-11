# Edge YOLO Video Streaming Python Backend

## Overview

This Python application serves as the backend for a real-time video streaming web application with YOLO (You Only Look Once) object detection at the edge. The project includes components for processing video streams, detecting objects using YOLO, and saving images based on the detected objects.

## Components

### 1. **Edge YOLO Video Streaming (main.py)**

The main script is a Flask-based application for streaming video with real-time object detection. Key features include:

- **RESTful Endpoints:**
  - `/api/update_filter` (POST): Updates YOLO filters based on user input.
  - `/api/get_filter` (GET): Retrieves the last applied YOLO filter for visualization.

- **Real-time Object Detection:**
  - Utilizes YOLOv5 for object detection in video streams.
  - Threading for concurrent image processing.

### 2. **Database Interaction (dataBase.py)**

The `DataBase` class handles interactions with the MySQL database for fetching, inserting, and deleting data. Features include:

- Fetching data from the database.
- Inserting data into the database.
- Deleting data from the database.

### 3. **Image Saving Module (save_.py)**

The `Save_` class is a threaded module responsible for saving images based on YOLO detections. Key features include:

- Saving images in a directory structure based on date, class, and count.
- Threading for concurrent image saving.
- Real-time synchronization with the YOLO thread.

### 4. **YOLOv5 Object Detection (yoloThread.py)**

The `YoloThread` class utilizes YOLOv5 for real-time object detection. Features include:

- Real-time detection of objects using YOLOv5.
- Threading for concurrent image processing.
- Signal emission for communication with the `Save_` class.

### 5. **Configuration (config.py)**

The `config.py` file contains configuration parameters such as time intervals, device details, and API endpoints.

## Prerequisites

- Python 3.x
- Flask
- PyTorch
- OpenCV
- MySQL database

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/mycareer6107/Edge-YOLO-Video-Streaming-Python-Backend.git

# Contributors
- Muhammad Atif Rafique
