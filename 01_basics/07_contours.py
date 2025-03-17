import cv2

img = cv2.imread('assets/python.png')
copy = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
mask = cv2.threshold(gray, thresh=250, maxval=255, type=cv2.THRESH_BINARY)[1]

contours = cv2.findContours(mask, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'liczba konturów: {len(contours)}')

# for contour in contours:
#     img_cnt = cv2.drawContours(img.copy(), contour, contourIdx=-1, color=(0,255,0), thickness=3)
#     cv2.imshow('img_cnt', img_cnt)
#     cv2.waitKey(0)

#liczenie pola konturow
max_area = 0
idx_flag_area = 0
for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour, oriented=True)
    if area > max_area:
        max_area = area
        idx_flag_area = idx

print(f'max field: {max_area}, idx: {idx_flag_area}')
img_cnt_mac_area = cv2.drawContours(img.copy(), [contours[idx_flag_area]], contourIdx=-1, color=(0,255,0), thickness=3)
cv2.imshow('img_cnt_mac_area', img_cnt_mac_area)
cv2.waitKey(0)

perimeter = cv2.arcLength(curve=contours[idx_flag_area], closed=True)
print(f'perimeter: {perimeter}')