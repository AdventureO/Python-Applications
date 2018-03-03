import cv2

#Capture a video You want to play
cap = cv2.VideoCapture(path_to_video)

while(cap.isOpened()):
    #Read frame
    ret, frame = cap.read()

    #Make a frame gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Show frame
    cv2.imshow('frame',gray)

    #If input key is q - stop playing video
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()