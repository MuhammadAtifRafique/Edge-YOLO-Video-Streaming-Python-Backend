import threading
import datetime
from PySignal import Signal
import time
from time import sleep
import cv2
import torch
from config import *

class YoloThread(threading.Thread):
    sendSignal = Signal()
    def __init__(self):
        threading.Thread.__init__(self)
        self.Class_ = class_()
        self.camera1 = cv2.VideoCapture(0)
        self.camera1.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.camera1.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        self._fps = self.camera1.get(cv2.CAP_PROP_FPS)
        self.frame_size = (640, 640)
        self.count = 0
        self.cam1_frame = None
        pass  # end of SaverClass constructor
    def run(self):
        while(1):
            
            image1_ret, frame1 = self.camera1.read()
            results = self.model(frame1)
            
            
            if image1_ret:
                for box in results.xyxy[0]:
                    if True:		#box[5]==0:
                        start = time.time()
                        dateTime = datetime.datetime.now()
                        self.count += 1
                        print(f"[INFO] counts is now = {self.count} ....................., Class Name = {self.Class_.numToName[int(box[5])]}........................")
                        xB = int(box[2])
                        xA = int(box[0])
                        yB = int(box[3])
                        yA = int(box[1])
                        #cv2.rectangle(frame1, (xA, yA), (xB, yB), (0, 255, 0), 2)
                        #cv2.putText(frame1,"%.2f %.2f %s"%(self._fps,float(box[4]),self.Class_.numToName[int(box[5])]),(xA,yA-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
                        dimensions = [yA,yB,xA,xB]
                        self.sendSignal.emit(dateTime,self.Class_.numToName[int(box[5])],frame1,dimensions,self.count)
                        end = time.time()
                        print(f"[INFO] total time in capture picture loop = {end-start}..................................................................")
                    cv2.waitKey(1)         
        self.camera1.release()
        pass  # end of run function
    pass  # end of SaverClass

if __name__ == "__main__":
    yoloThread = YoloThread()
    yoloThread.start()