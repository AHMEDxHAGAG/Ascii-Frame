import sys
import os
import cv2
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
    namefolder(project_name)
    

        
def gettingvid():
    project_name = input("Project Name: ")
    video_path = input("Video Path: ")
    e = video_path.split(".")[1]
    if os.path.isfile(video_path) and (e=="webm" or e=="mp4" or e =="mov" or e=="avi" or e=="wmv"):
        return (project_name, video_path)
    else:
        print("Wrong Video Path or File Format")

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
    else:
        os.mkdir(x+"_1")

    fh.changedirtopath("AsciiFrame")

main()
