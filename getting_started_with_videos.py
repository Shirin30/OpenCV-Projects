#How to read, write and show videos using camera

import cv2

cap = cv2.VideoCapture(0); # if we want to display a video file then write its name as argument
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True :
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) # this is to convert our frame to gray scale
        cv2.imshow('frame', gray) # if we dont want gray scale image we pass frame as second argument

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows