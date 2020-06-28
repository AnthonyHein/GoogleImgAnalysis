import cv2
import sys
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import csv
import math

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

def skinColorJson(target_folder):

    data = []
    images = glob.glob(target_folder + "/*.jpg", recursive=True)

    for imagePath in images:

        print("Working on", imagePath)

        # Create the haar cascade
        cascPath = "haarcascade_frontalface_default.xml"
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

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            blue = 0
            green = 0
            red = 0
            for r in range(h):
                for c in range(w):
                    blue += image[r+y,x+c, 0]
                    green += image[r+y,x+c, 1]
                    red += image[r+y,x+c, 2]
            data.append((blue / (w * h), green / (w * h), red / (w * h)))

    with open(target_folder + '.json', 'w') as outfile:
        json.dump(data, outfile)

def visualize(jsonfile):
    with open(jsonfile) as f:
        data = json.load(f)
    blue = [i[0] for i in data]
    green = [i[1] for i in data]
    red = [i[2] for i in data]

    plt.figure()

    plt.subplot(221)
    plt.title('Blue')
    plt.grid(True)
    plt.hist(blue, bins=20)

    plt.subplot(222)
    plt.title('Green')
    plt.grid(True)
    plt.hist(green, bins=20)

    plt.subplot(223)
    plt.title('Red')
    plt.grid(True)
    plt.hist(red, bins=20)

    plt.show()

    return

def jsonToCSV(csvname, jsons):
    with open(csvname, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Race", "Blue", "Green", "Red"])
        i = 0
        for jsonfile in jsons:

            with open(jsonfile) as f:
                data = json.load(f)

                for record in data:
                    writer.writerow([i, record[0], record[1], record[2]])

            i += 1

    return

INT = 5.397202801
BLUECOEFF = -0.024445013
GREENCOEFF = 0.009850173
REDCOEFF = -0.027310473

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def classify(filepath):

    ppl = []

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

    for (x, y, w, h) in faces:
        blue = 0
        green = 0
        red = 0
        for r in range(h):
            for c in range(w):
                blue += image[r+y,x+c, 0]
                green += image[r+y,x+c, 1]
                red += image[r+y,x+c, 2]

        blue /= w * h
        green /= w * h
        red /= w * h

        val = INT + BLUECOEFF * blue + GREENCOEFF * green + REDCOEFF * red
        ppl.append(sigmoid(val) >= 0.5)

    return ppl

def classifyAll(target_folder, sort=False):

    images = glob.glob(target_folder + "/*.jpg", recursive=True)

    output = []

    for imagePath in images:
        results = classify(imagePath)
        for result in results:
            output.append((imagePath, result))

    if sort:
        output = sorted(output, key=lambda x: x[0])

    for elem in output:
        print(elem)

    return output

# WHITE = 0
# BLACK = 1

if __name__ == "__main__":
    if sys.argv[1] == "skin":
        skinColor(sys.argv[2])
    elif sys.argv[1] == "draw":
        skinColor(sys.argv[2])
    elif sys.argv[1] == "data":
        skinColorJson(sys.argv[2])
    elif sys.argv[1] == "viz":
        visualize(sys.argv[2])
    elif sys.argv[1] == "csv":
        jsonToCSV(sys.argv[2], sys.argv[3:])
    elif sys.argv[1] == "classify":
        classifyAll(sys.argv[2], True)
    else:
        isFace(sys.argv[2])
