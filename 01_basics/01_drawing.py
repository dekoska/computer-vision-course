import cv2
import numpy as np

img = cv2.imread('assets/python.png')
copy = img.copy()

# cv2.imshow('image', img)
# cv2.waitKey(0)

height, width = img.shape[:2]
print(f"height: {height}, width: {width}")

cv2.line(img, (0,0), (width,height), (0,255,0), 5)
cv2.imshow('line', img)
cv2.waitKey(1000)

cv2.rectangle(img, (200, 50), (400, 230), (255, 0, 0), 3)
cv2.imshow('rectangle', img)
cv2.waitKey(1000)

cv2.circle(img, (300, 140), 90, (0, 0, 255), 3)
cv2.imshow('circle', img)
cv2.waitKey(1000)

pts = np.array([[300,140], [200,200],[200,50], [300,50]], 'int32').reshape((-1, 1, 2))
cv2.polylines(img,[pts], True, (0,255,0), 3)
cv2.imshow('img', img)
cv2.waitKey(1000)

cv2.putText(
    img, text='Python wymiata',
    org=(20,40), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1.5, color=(0,255,0), thickness=2
)
cv2.imshow('text',img)
cv2.waitKey(1000)