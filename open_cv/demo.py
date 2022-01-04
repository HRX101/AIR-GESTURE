import cv2 
import screen_brightness_control as sb
import subprocess
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
from cvzone.ColorModule import ColorFinder
from cvzone import *
import cvzone
from cvzone import *

vid=cv2.VideoCapture(0)
vid.set(120,231)
detector=HandDetector(detectionCon=0.8)
face_detect=FaceDetector(minDetectionCon=0.5)
while True:
    frame,image=vid.read()
    image=cv2.flip(image,1)
    hands,image=detector.findHands(image,flipType=False)
    image,faces=face_detect.findFaces(image)
    if hands:
        lm=hands[0]['lmList']
        dis,info=detector.findDistance(lm[8],lm[12])
        dis1,info1=detector.findDistance(lm[8],lm[20])
        bright_dis,info2=detector.findDistance(lm[4],lm[8])
        start_p=(50,100)
        end_p=(200,200)
        end_p1=(100,200)
       # sb.set_brightness(round(bright_dis))
        #image=cv2.line(image,start_p,end_p,(0,255,0),3)
        if (round(dis)<=55 and round(dis)>=20):
            if(round(100/round(dis))>=2 and round(100/round(dis))<=5):
                start_p=(5+lm[8][0],20+lm[8][0])
                end_p1=(50+lm[8][0],40+lm[8][0])
                image=cv2.rectangle(image,start_p,end_p1,(0,255,0),2)
            else:
                image=cv2.rectangle(image,start_p,end_p1,(0,255,0),2)        

        """
        if(dis>=63 and dis<=65):
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
        elif(dis1>=124 and dis1<=125):
            
            subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        
        else:
            pass
        """
    cv2.imshow("demo",image)
    if cv2.waitKey(1)==ord('a'):
        break
vid.release()
cv2.destroyAllWindows()
