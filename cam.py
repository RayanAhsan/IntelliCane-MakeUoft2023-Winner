import cv2
from picamera2 import Picamera2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np
from collections import Counter
import pyttsx3
import threading


x = 5
detected_objects = ['person']
picam2 = Picamera2() 
picam2.preview_configuration.main.size = (640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
model=YOLO('yolov8n.pt')
my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")


def find_mode_with_tts(arr):
    # Sort the array
    arr.sort()

    # Count occurrences of each word
    word_freq = Counter(arr)

    # Calculate average frequency
    total_freq = sum(word_freq.values())
    num_unique = len(word_freq)
    avg_freq = total_freq / num_unique


    # Implement text-to-speech
    engine = pyttsx3.init()
    for i, word in enumerate(word_freq):
        if word_freq[word] >= avg_freq:
            engine.say(f"{word} ahead")
            engine.runAndWait()

def detection_object():
    results = model.predict(im)
    for box in results.xyxy[0]:
        x1, y1, x2, y2, conf, cls = box
        c = class_list[int(cls)]
        detected_objects.append(c)

def thread_function():
    count=0
    while True:
        global im
        im = picam2.capture_array()
        count += 1
        if count % 2 != 0:
            continue
        im=cv2.flip(im,-1)
        results=model.predict(im)
        a=results[0].boxes.data
        px=pd.DataFrame(a).astype("float")
            
        for index,row in px.iterrows():
    #        print(row)
     
            x1=int(row[0])
            y1=int(row[1])
            x2=int(row[2])
            y2=int(row[3])
            d=int(row[5])
            c=class_list[d]
            print (c)
            
            cv2.rectangle(im,(x1,y1),(x2,y2),(0,0,255),2)
            cvzone.putTextRect(im,f'{c}',(x1,y1),1,1)
        
        cv2.imshow("Camera", im)
        
        if cv2.waitKey(1) == ord('q'):
            break

        if (x == 5):
            find_mode_with_tts(detected_objects)

def main():
    thread1 = threading.Thread(target=thread_function)
    thread2 = threading.Thread(target=detection_object)
    thread1.start()
    thread2.start()

if __name__ == "__main__":
    main()