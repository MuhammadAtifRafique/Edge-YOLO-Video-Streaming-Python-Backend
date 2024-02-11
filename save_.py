import os
import threading
from yoloThread import YoloThread
import time
from config import *
import cv2

class Save_(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        self.yoloThread = YoloThread()
        self.yoloThread.start()
        self.yoloThread.sendSignal.connect(self.test)
        self.Frame=self.dateTime=self.class_=self.dimensions=self.count= None
        self.frame_size = (640, 640)
        pass # end of __init__ function
    def test(self,dateTime,class_,frame,dimensions,count):
        self.dateTime,self.class_,self.Frame,self.dimensions,self.count = dateTime,class_,frame,dimensions,count
        pass

    def saveData(self,dateTime,_class,frame,dimensions,count):
        
        frame = frame[dimensions[0]:dimensions[1], dimensions[2]:dimensions[3]]  # get time = 0.0
        #frame = cv2.resize(frame, self.frame_size) # get time = 0.002
        Name = dateTime.strftime("%Y-%m-%d %H-%M-%S.%f") # get time = 0.0
        cwd = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{dateTime.year}/" + f"{dateTime.month}/" + f"{dateTime.day}/" +  f"{_class}") #get time = 0.000535
        
        if not os.path.exists(cwd):
            
            print("[INFO] Making Parent directory and saving data ...........")
            os.makedirs(cwd) # # get time = 0.000884
            os.chdir(cwd) # get time = 0.0
            filename = f"{count}_{Name}.jpg" # get time = 0.0
            cv2.imwrite(filename, frame) # get time = 0.01843
            
        else:
            cwd = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{dateTime.year}/" + f"{dateTime.month}/" + f"{dateTime.day}/" +  f"{_class}") #get time = 0.000535
            print("[INFO] Saving data in exist's directory................")
            os.chdir(cwd) # get time = 0.0
            filename = f"{count}_{Name}.jpg" # get time = 0.0
            cv2.imwrite(filename, frame)  # get time = 0.01843
            
            
        

        pass # end of create directory function

    def run(self):
        while(1):
            if self.Frame is not None:
                start = time.time()
                self.saveData(self.dateTime,self.class_,self.Frame,self.dimensions,self.count)
                end = time.time()
                print(f"[INFO] total time in saving picture loop = {end-start}..................................................................")
                self.resetValues()
            else:
                pass

        pass # end of run function 
    def resetValues(self):
        self.Frame=self.dateTime=self.class_=self.dimensions=self.count = None

    pass # end of class Camera

if __name__ == "__main__":
    save_ = Save_()
    save_.start()