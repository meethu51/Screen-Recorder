#import modules
import datetime

#this module grabs the image
from PIL import ImageGrab

import numpy as np
import cv2 as cv

# we want to get system metrics info using the win32 api
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

#print(width,height)

#Give dynamic name to out files by adding format string
timeStamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')

recordName = f'{timeStamp}.mp4'


#We are giving four characters for video file decoding and encoding

fourChar = cv.VideoWriter_fourcc('m','p','4','v')

captured_video = cv.VideoWriter('recordName.mp4',fourChar,10.0,(width,height))


while True:
    #image variable  with boundary box parameters
    img = ImageGrab.grab(bbox=(0,0,width,height))

    #convert image to nunmpy array
    img_np = np.array(img)

    #Convert img_np to RGB
    color_img = cv.cvtColor(img_np,cv.COLOR_BGR2RGB)

    #call opencv
    cv.imshow("RainI", color_img)

    #call capture video to wite converted image (color_img)
    captured_video.write(color_img)

    #Stopping screen recording when q is pressed
    if cv.waitKey(10) == ord('q'):
        break



