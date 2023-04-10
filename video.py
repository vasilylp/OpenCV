import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# img = cv2.imread('Face.jpg') # распознование по фото------------
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# faces = face_cascades.detectMultiScale(img_gray)
# # print(faces)
# for(x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y), (x + w , y + h), (255,0,0),2)

# cv2.imshow('Resalt', img)

# cv2.waitKey(0)

cap = cv2.VideoCapture(0) # распознование по видео------------------

while True:
    _, frame = cap.read()
#     cv2.imshow("camera", frame)
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Preview', frame)
    faces = face_cascades.detectMultiScale(img_gray)

    for(x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y), (x + w , y + h), (255,0,0),2)

    cv2.imshow('Resalt', frame)


    if cv2.waitKey(0) & 0xff == ord ("q"):
        break