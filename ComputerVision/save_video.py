import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    #Read a frame
    ret, frame = cap.read()

    #If camera is working
    if ret == True:
        frame = cv2.flip(frame,0)

        #write the flipped frame
        out.write(frame)

        #Show frame
        cv2.imshow('frame',frame)


        #If input key is q - stop playing video
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    else:
         break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()