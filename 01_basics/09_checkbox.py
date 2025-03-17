import cv2
import numpy as np

img = cv2.imread('assets/checkbox.png')

img = cv2.copyMakeBorder(img, 20, 20, 20, 20, borderType=cv2.BORDER_CONSTANT, value=(255,255,255))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

thresh = cv2.threshold(blurred, 75, 200, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
print(len(contours))

# for contour in contours:
#     img_cnt = cv2.drawContours(img.copy(), contour, contourIdx=-1, color=(0,255,0), thickness=5)
#     cv2.imshow('img_cnt', img_cnt)
#     cv2.waitKey(0)

checked_idx = 0
total = 0

for idx in [1, 2]:
    mask = np.zeros(shape=gray.shape, dtype='uint8')
    # cv2.drawContours(mask, contours[idx], contourIdx=-1, color=(255,255,255), thickness=-1) #nie dziala!!!!!! niepelne kontury:(
    cv2.fillPoly(mask, [contours[idx]], color=(255, 255, 255))
    # cv2.imshow(f'mask', mask)
    # cv2.waitKey(0)

    mask_inv= cv2.bitwise_not(mask)
    # cv2.imshow(f'mask_inv{idx}', mask_inv)
    # cv2.waitKey(0)

    answer = cv2.add(gray, mask_inv)
    # cv2.imshow(f'answer {idx}', answer)
    # cv2.waitKey(0)

    answer_inv = cv2.bitwise_not(answer)
    # cv2.imshow(f'answer_inv {idx}', answer_inv)
    # cv2.waitKey(0)

    cnt= cv2.countNonZero(answer_inv)
    # cv2.imshow(f'cnt {idx}', cnt)
    # cv2.waitKey(0)

    if cnt > total:
        checked_idx = idx

print(checked_idx)

img = cv2.drawContours(img, contours[checked_idx], contourIdx=-1, color=(0, 255, 0), thickness=3)
cv2.imshow('checked_contours', img)
cv2.waitKey(0)
