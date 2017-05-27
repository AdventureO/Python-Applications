import cv2

# read cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread(name_of_image)

#Convert RGD image to gray image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Find the face and return coordinates of it((pixel column, pixel) - point to start) row, hight, width)
#selectFactor - every time when python will search for faces it will decrease searching scale by 5%
#minNeighbors - Parameter specifying how many neighbors each candidate rectangle should have to retain it.
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.35, minNeighbors=5)

print(faces)
for x, y, w, h in faces:
    image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255,0), 3) #o for red and blue, 3 - width

cv2.imshow("Face", image)
cv2.waitKey(0) #any key
cv2.destroyAllWindows()