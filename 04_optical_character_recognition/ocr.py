import pytesseract
from PIL import Image
import imutils
import cv2

def ocr(filename):
    return pytesseract.image_to_string(Image.open(filename))

filename = 'cap_1.JPG'
img = cv2.imread(filename)

print(ocr(filename))

cv2.imshow('original', img)
cv2.waitKey(0)