# import librairies
#
import cv2

cap=cv2.VideoCapture(0)

print("well imported.....")

# we will start by trying the eyeglass HaarCascade classifier
"initializing the face classifier"

face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    
# read the image from the cam
    _,image=cap.read()
    
# now i convert the image into grayscale
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# detect all faces in the image
    faces=face.detectMultiScale(image_gray,1.3,5)
# for every face draw a rectangle
    for x,y, width,height in glasses:
        cv2.rectangle(image,(x,y),(x+width,y+height),color=(255,0,0),thickness=1)
        
# cv2.putText(image,'Face',(10,500),font,1,(0,0,255),2)
    cv2.imshow('Stark',image)
    if cv2.waitKey(1)==ord('q'):
        break

# realising the videos
cap.release()
cv2.destroyAllWindows()






