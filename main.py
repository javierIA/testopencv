import numpy as np
import cv2


#Selecionar de acuerdo a tu camara web poner 0 de aucerdo tu camera 
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap= cv2.VideoCapture(2)


if not cap.isOpened():
    print("NO HAY CAMARA")
    exit()


while True:
    ret,frame=cap.read()

    if ret:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

        for (x,y,w,h)in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


        #cv2.imshow("Grises",gray)
        #print(gray)
        cv2.imshow("NORMAL",frame)
        #print(frame)
        
    else:
        print("NO HAY CAMARA")
        exit()

    if cv2.waitKey(1)& 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

