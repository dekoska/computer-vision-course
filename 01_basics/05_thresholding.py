import cv2

img = cv2.imread('assets/grey.png')
# cv2.imshow('grey', img)

# thresh_binary = cv2.threshold(img, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh_binary', thresh_binary)

titles = ['THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV']
for title in titles:
    for thresh in [0, 50, 100, 150, 200]:
        thresh_type = getattr(cv2, title)
        thresh_image = cv2.threshold(img, thresh=thresh, maxval=255, type=thresh_type)[1]
        cv2.imshow(f'title:{title}: thresh:{thresh}', thresh_image)
        cv2.waitKey(0)
        cv2.destroyWindow(f'title:{title}: thresh:{thresh}')

cv2.waitKey(0)