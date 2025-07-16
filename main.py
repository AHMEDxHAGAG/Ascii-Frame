import sys
import os
import cv2 as cv
import re
import numpy as np
from PIL import Image, ImageFont, ImageDraw
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
    print()
    capture = cv.VideoCapture(path)
    count = 0
    #try: 
    while True:
        count +=1
        isTrue, frame = capture.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        pixels = np.array(gray, dtype=np.uint8)
        black = np.zeros((int(pixels.shape[0]*1), int(pixels.shape[1]*1)), dtype=np.uint8)
        Blank = Image.fromarray(black)
        draw = ImageDraw.Draw(Blank)
        fonty = ImageFont.truetype(os.path.join(os.path.dirname(os.path.abspath(__file__)),'c.ttf'), size=12)
        word = fonty.getbbox("@")
        print(f"Width = {word[2]-word[0]}")
        print(f"Height = {word[3]-word[1]}")
        r =0
        for row in range(0,pixels.shape[0],10):
            c=0
            for col in range(0, pixels.shape[1], 7):
                meany = int(pixels[row:row+10, col:col+7].mean())

                if meany > 230:
                    draw.text((c,r), "@", font=fonty, fill=255)
                elif meany > 205:
                    draw.text((c,r), "%", font=fonty, fill=255)
                elif meany > 180:
                    draw.text((c,r), "#", font=fonty, fill=255)
                elif meany > 155:
                    draw.text((c,r), "*", font=fonty, fill=255)
                elif meany > 131:
                    draw.text((c,r), "+", font=fonty, fill=255)
                elif meany > 106:
                    draw.text((c,r), "=", font=fonty, fill=255)
                elif meany > 81:
                    draw.text((c,r), "-", font=fonty, fill=255)
                elif meany > 56:
                    draw.text((c,r), ":", font=fonty, fill=255)
                elif meany > 26:
                    draw.text((c,r), ".", font=fonty, fill=255)
                elif meany >=0 :
                    draw.text((c,r), " ", font=fonty, fill=255)
                
                c += 7
            r += 10
        
        cv.imwrite(os.path.expanduser(f"~/AsciiFrame/Projects/{name}/Frame{count}.jpg"), np.array(Blank))
        
    #except :
        #pass


main()
