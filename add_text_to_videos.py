import cv2
import datetime

cap = cv2.VideoCapture(0); # if we want to display a video file then write its name as argument

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208) # can also be written as cap.set(3, val)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # can also be written as cap.set(4, val)

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True :

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet =  str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame) # if we dont want gray scale image we pass frame as second argument

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows