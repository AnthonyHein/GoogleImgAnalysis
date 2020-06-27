import cv2
import sys
import numpy as np

def isFace(filepath):
    # Get user supplied values
    imagePath = filepath
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print("SUCCES - Found {0} faces in filepath {1}".format(len(faces), filepath))

    return len(faces) > 0

def drawFace(filepath):
    # Get user supplied values
    imagePath = filepath
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

def skinColor(filepath):
    # Get user supplied values
    imagePath = filepath
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        blue = 0
        green = 0
        red = 0
        for r in range(h):
            for c in range(w):
                blue += image[r+y,x+c, 0]
                green += image[r+y,x+c, 1]
                red += image[r+y,x+c, 2]
        print("Avg blue: ", blue / (w * h))
        print("Avg green: ", green / (w * h))
        print("Avg red: ", red / (w * h))

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

if __name__ == "__main__":
    if sys.argv[1] == "skin":
        skinColor(sys.argv[2])
    elif sys.argv[1] == "draw":
        skinColor(sys.argv[2])
    else:
        isFace(sys.argv[2])
