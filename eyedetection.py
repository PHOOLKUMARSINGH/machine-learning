import numpy as np
import cv2
cv2.imread(r"E:\aap development\pkgs\opencv-3.4.1-py36_200\Library\etc\haarcascades\Hrithik.JPG",cv2.IMREAD_GRAYSCALE)
cv2.CascadeClassifier(r"E:\aap development\pkgs\opencv-3.4.1-py36_200\Library\etc\haarcascades\haarcascade_frontalface_default.xml)
eye=cv2.CascadeClassifier(r"E:\aap development\pkgs\opencv-3.4.1-py36_200\Library\etc\haarcascades\haarcascade_eye.xml)
mygrayimage=cv2.cvtcolor(image,cv2.BGR2BGRA)
myface=face.detectMultiscale(mygrayimage,1,3,5)
for(x,y,w,h) in myface:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray=mygrayimage[y:y+h,x:x+w]
    roi_color=image[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(roi_gray)
    for(ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('mywindow',image)
   