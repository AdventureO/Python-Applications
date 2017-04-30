import cv2

#Read cascade which already has all face characteristics
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread(path_to_picture)

#Convert RGD image to gray image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Find the face and return coordinates of it((pixel column, pixel row) - point to start), hight, width)
#selectFactor - every time when python will search for faces it will decrease searching scale by 5%
#minNeighbors - Parameter specifying how many neighbors each candidate rectangle should have to retain it.
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5)

for x, y, w, h in faces:
    #0 for red, 255 for green, and 0 for blue, 3 - width of frame
    image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255,0), 3)

cv2.imshow("Face detection", image)
cv2.waitKey(5000)
cv2.destroyAllWindows()
