import numpy as np
import face_recognition
import cv2
import os


def resize(img, scale_percent_in=1):
    scale_percent = scale_percent_in  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def project_1_facial_recognition():
    """This function processes two images and acertains if the same face appears in both"""
    imgElon = face_recognition.load_image_file('faces/elon_musk_1.jpg')
    imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
    imgElon = resize(imgElon, scale_percent_in=40)

    imgElonTest = face_recognition.load_image_file('faces/elon_musk_2.jpg')
    imgElonTest = cv2.cvtColor(imgElonTest, cv2.COLOR_BGR2RGB)
    imgElonTest = resize(imgElonTest, scale_percent_in=20)

    # returns (top right, bottom right, left)
    faceLoc = face_recognition.face_locations(imgElon)[0]
    encodeElon = face_recognition.face_encodings(imgElon)[0]

    cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]),
                  (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

    faceLocTest = face_recognition.face_locations(imgElonTest)[0]
    encodeElonTest = face_recognition.face_encodings(imgElonTest)[0]
    cv2.rectangle(imgElonTest, (faceLocTest[3], faceLocTest[0]),
                  (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

    results = face_recognition.compare_faces([encodeElon], encodeElonTest)
    # lower the distance the better the match
    faceDis = face_recognition.face_distance([encodeElon], encodeElonTest)
    print(results, faceDis)  # values range from zero to 1

    cv2.putText(imgElonTest, f'{results} {round(faceDis[0],2)}', (
        50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Elon Musk", imgElon)
    cv2.imshow("Elon Musk Test", imgElonTest)
    cv2.waitKey(0)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def project_2_facial_recognition_attendance():
    path = 'faces_2'
    images = []
    classNames = []
    myList = os.listdir(path)
    for cls in myList:
        curImg = cv2.imread(f'{path}/{cls}')
        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])

    encodeListKnown = findEncodings(images)

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(
                encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2+35), (x2, y2),
                              (0, 255, 0), cv2.FILLED)

                cv2.putText(img, name, (x1+6, y2-6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.imshow('Webcam', img)
            cv2.waitKey(1)


if __name__ == '__main__':

    # project_1_facial_recognition()

    project_2_facial_recognition_attendance()
