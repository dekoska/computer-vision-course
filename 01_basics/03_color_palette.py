import cv2
import numpy as np

def nothing(x):
    pass

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Kliknięty kolor RGB: ({img[y, x][2]}, {img[y, x][1]}, {img[y, x][0]})')

img = np.zeros(shape=(300,500,3), dtype=np.uint8)
cv2.namedWindow('paleta')

#paski przewijania
cv2.createTrackbar('Red', 'paleta', 0, 255, nothing)
cv2.createTrackbar('Green', 'paleta', 0, 255, nothing)
cv2.createTrackbar('Blue', 'paleta', 0, 255, nothing)

cv2.setMouseCallback('paleta', mouse_callback)

while True:
    cv2.imshow('paleta', img)

    r = cv2.getTrackbarPos('Red', 'paleta')
    g = cv2.getTrackbarPos('Green', 'paleta')
    b = cv2.getTrackbarPos('Blue', 'paleta')

    img[:] = [b,g,r]

    if cv2.waitKey(1) == 27:
        break