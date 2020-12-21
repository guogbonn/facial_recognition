import numpy as np
import face_recognition
import cv2


def resize(img, scale_percent_in=1):
    scale_percent = scale_percent_in  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def facial_recognition():
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
    cv2.imshow("Elon Musk", imgElon)
    cv2.imshow("Elon Musk Test", imgElonTest)
    cv2.waitKey(0)


if __name__ == '__main__':
    facial_recognition()
