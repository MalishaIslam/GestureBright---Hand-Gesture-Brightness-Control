import cv2
import handpart as hp
import numpy as np
import winsound
import pyttsx3
import  math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

#weigth_cap, height_cap = 1280,720
capture = cv2.VideoCapture(0)
#capture.set(3, weigth_cap)
#capture.set(4, height_cap)

# engine = pyttsx3.init()
# engine.say('Dear, Turukka, I am here')
# engine.say('I also believe in your fav quote be hurukka be purukka')
# engine.say('Turn on the webcam')
# engine.runAndWait()

handdetect = hp.handdetector()

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
#volume.GetMasterVolumeLevel()
#print(volume.GetVolumeRange())
volrange = volume.GetVolumeRange()
#volume.SetMasterVolumeLevel(0, None)
minvol = volrange[0]
maxvol = volrange[1]
vol = 0
volbar = 400

while capture.isOpened():
    _ , frame = capture.read()
    flip_frame = cv2.flip(frame, 1)
    flip_frame = handdetect.findhands(flip_frame)
    lmlist = handdetect.findpos(flip_frame, draw = False)
    if len(lmlist) != 0:
        #print(lmlist[4],lmlist[8],lmlist[12],lmlist[16],lmlist[20])
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        x3, y3 = lmlist[12][1], lmlist[12][2]
        x4, y4 = lmlist[16][1], lmlist[16][2]
        x5, y5 = lmlist[20][1], lmlist[20][2]
        #print(x1,x2,y1,y2)
        cx, cy = (x1 + x2)//2 , (y1 + y2)//2

        cv2.circle(flip_frame, (x1, y1), 10, (120, 0, 120), cv2.FILLED)
        cv2.circle(flip_frame, (x2, y2), 10, (120, 0, 120), cv2.FILLED)
        #cv2.circle(flip_frame, (x3, y3), 10, (120, 0, 120), cv2.FILLED)
        #cv2.circle(flip_frame, (x4, y4), 10, (120, 0, 120), cv2.FILLED)
        #cv2.circle(flip_frame, (x5, y5), 10, (120, 0, 120), cv2.FILLED)

        cv2.arrowedLine(flip_frame, (x1, y1), (x2, y2), (120, 0, 120), 1)
        cv2.circle(flip_frame, (cx, cy), 10, (120, 0, 120), cv2.FILLED)
        #cv2.arrowedLine(flip_frame, (x2, y2), (x3, y3), (120, 0, 120), 1)

        length = math.hypot(x2 - x1, y2 - y1)
        #print(length)

        #vol = np.interp(length, [45,265], [minvol,maxvol])
        vol = np.interp(length, [45, 265], [0, 100])
        volbar = np.interp(length, [45, 265], [400, 150])
        print(int(length),vol)
        #volume.SetMasterVolumeLevel(vol, None)
        sbc.set_brightness(vol, display=0)
        print(sbc.get_brightness())
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        #winsound.Beep(440,500)

        if length < 50:
            cv2.circle(flip_frame, (cx,cy), 15, (0,255,0), cv2.FILLED)

    cv2.rectangle(flip_frame, (50, 150), (85, 400), (0,255,0), 3)
    cv2.rectangle(flip_frame, (50, int(volbar)), (85, 400), (0, 255, 0), cv2.FILLED)

    cv2.imshow('Turukka',flip_frame)
    if cv2.waitKey(10) == ord('q'):
        break
capture.release()