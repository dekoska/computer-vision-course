import cv2
import imutils

img = cv2.imread('assets/guido.jpg')
img = imutils.resize(img, height=500)

# canny = cv2.Canny(img, threshold1=250, threshold2=250)

for thresh in [0,25,50,75,100,125,150,175,200,225,250]:
    canny = cv2.Canny(img, threshold1=thresh, threshold2=thresh)
    cv2.imshow(f'canny:{thresh}', canny)
    cv2.waitKey(0)
    cv2.destroyWindow(f'canny:{thresh}')

cv2.waitKey(0)

