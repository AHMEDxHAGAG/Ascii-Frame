import sys
import os

def checkdir(x):
    # Check if the app root folder is in the system path
    # os.environ to get the default home page
    # os.path.exists explain itself
    if os.path.exists(os.path.join(os.environ.get('HOME'), x)):
        return True
    else:
        return False
    
def checkcwddir(x):
    # Check if the app root folder is in the system path
    # os.environ to get the default home page
    # os.path.exists explain itself
    if os.path.exists(os.path.join(os.getcwd(), x)):
        return True
    else:
        return False

def createpath(x):
    os.mkdir(os.path.join(os.environ.get('HOME'), x))

def createcwdpath(x):
     os.mkdir(os.path.join(os.getcwd(), x))

def changedirtopath(x):
    os.chdir(os.path.join(os.environ.get("HOME"), x))



