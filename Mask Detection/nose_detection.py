import cv2
face_cascade = cv2.CascadeClassifier('frontalface.xml')
nose_cascade = cv2.CascadeClassifier('nose.xml')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _,img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        noses = nose_cascade.detectMultiScale(roi_gray)
        for(nx,ny,nw,nh) in noses:
            #cv2.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(0,255,0),5)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0, 255),3)
            
            cv2.putText(img, "Mask : {} detected".format("not"),  (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv2.LINE_AA)
    cv2.imshow('img',img)

    if cv2.waitKey(1) == 27:
        break
cap.release()  
cv2.destroyAllWindows()