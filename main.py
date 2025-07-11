import sys
import os
import cv2
import numpy as np
from PIL import Image
import fileio_handler as fh

def main():
    if(not fh.checkdir("AsciiFrame")):
        fh.createpath("AsciiFrame")

    fh.changedirtopath("AsciiFrame")

    if(not fh.checkcwddir("Projects")):
        fh.createcwdpath("Projects")

    if(not fh.checkcwddir(".tmp")):
        fh.createcwdpath(".tmp")

        


main()
