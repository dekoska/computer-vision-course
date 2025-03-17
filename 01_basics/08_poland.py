import cv2

img = cv2.imread('assets/poland.png')
img = cv2.copyMakeBorder(img, top=20, bottom=20, left=20, right=20, borderType=cv2.BORDER_CONSTANT, value=(255,255,255))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = cv2.threshold(gray, thresh=180, maxval=255, type=cv2.THRESH_BINARY)[1]

contours = cv2.findContours(mask, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'liczba konturów: {len(contours)}')

img_with_contours = img.copy()
img_with_contours = cv2.drawContours(img_with_contours, contours, contourIdx=0, color=(0, 255, 0), thickness=3)

contour = contours[0]
leftmost = contour[contour[:,:,0].argmin()][0]
rightmost = contour[contour[:,:,0].argmax()][0]
topmost = contour[contour[:,:,1].argmin()][0]
bottommost = contour[contour[:,:,1].argmax()][0]

''' 
contour = np.array([[[10, 20]], [[30, 40]], [[50, 60]]])
contour[:,:,0]  # Wartości x: [10, 30, 50]
contour[:,:,1]  # Wartości y: [20, 40, 60]
'''

for point in [leftmost, rightmost, topmost, bottommost]:
    cv2.circle(img_with_contours, center=point, radius=10, color=(0, 0, 255), thickness=-1)

cv2.imshow('extreme_points', img_with_contours)
cv2.waitKey(0)

