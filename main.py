import sys
import os
import cv2 as cv
import re
import numpy as np
from PIL import Image
import fileio_handler as fh

def main():
    if(not fh.checkdir("AsciiFrame")):
        fh.createpath("AsciiFrame")

    fh.changedirtopath("AsciiFrame")

    if(not fh.checkcwddir("Projects")):
        fh.createcwdpath("Projects")

    project_name, video_path = gettingvid()
    extract_frames(video_path, namefolder(project_name))
    fh.changedirtopath("AsciiFrame")

        
def gettingvid():
    project_name = input("Project Name: ")
    video_path = input("Video Path: ")
    if "." in video_path:
        e = video_path.split(".")[1]
        if os.path.isfile(os.path.expanduser(video_path)) and (e=="webm" or e=="mp4" or e =="mov" or e=="avi" or e=="wmv"):
            return (project_name, video_path)
        else:
            print("Wrong Video Path or File Format")
            sys.exit()
    else:
          print("Wrong Video Path or File Format")
          sys.exit()        

def namefolder(x):
    fh.changedirtopath(os.path.join("AsciiFrame", "Projects"))
    flag = False
    last = ""
    arr = [i for i in os.listdir(".")]
    arr.sort()
    for i in arr:
        if x == i.split("_")[0]:
            last = i
            flag = True
    if flag:
        r = re.search(r"^\w+_(?P<number>\d+)$", last)
        os.mkdir(x+"_"+str(int(r.group("number"))+1))
        return x+"_"+str(int(r.group("number"))+1)
    else:
        os.mkdir(x+"_1")
        return x+"_1"
    

def extract_frames(path, name):
    capture = cv.VideoCapture(path)
    count = 0
    try: 
        while True:
            count +=1
            isTrue, frame = capture.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imwrite(os.path.expanduser(f"~/AsciiFrame/Projects/{name}/Frame{count}.jpg"), gray)
            cv.waitKey(1)
    except :
        pass


main()
