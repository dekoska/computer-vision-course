import cv2
import imutils
import numpy as np
from imutils import contours
import argparse

def prepare_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 70, 70)
    thresh = cv2.threshold(edges, thresh=50, maxval=255, type=cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return thresh

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args()) #ap.parse_args() -parsuje argumenty przekazane do skryptu z linii poleceń  vars(...) – konwertuje obiekt Namespace na słownik {'image': 'obraz.jpg'}

ANSWER_KEY = {0: 1, 1: 3, 2: 0, 3: 2, 4: 1, 5: 3, 6: 4, 7: 1, 8: 3, 9: 0}

image = cv2.imread(args["image"])

thresh = prepare_image(image)

cnts = cv2.findContours(thresh.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts) #imutils.grab_contours zapewnia kompatybilność kodu z różnymi wersjami OpenCV i zawsze zwraca poprawną listę konturów
print(f'liczba konturow: {len(cnts)}')

question_contours = []

for cnt in cnts:
    (x,y,w,h) = cv2.boundingRect(cnt)
    aspect_ratio = w / float(h)

    if w > 50 and h > 50 and 0.9 < aspect_ratio < 1.1:
            question_contours.append(cnt)

print(f'liczba odpowiedzi: {len(question_contours)}')

img = image.copy()

correct = 0
question_contours = imutils.contours.sort_contours(question_contours, method='top-to-bottom')[0]

for question, idx in enumerate(range(0, len(question_contours), 5)):
    fields = question_contours[idx:idx + 5]
    fields = imutils.contours.sort_contours(fields, method='left-to-right')[0]
    marked = None

    for cnt_idx, cnt in enumerate(fields):
        mask = np.zeros(thresh.shape, dtype='uint8')
        cv2.drawContours(image=mask, contours=[cnt], contourIdx=-1, color=255, thickness=-1)
        mask = cv2.bitwise_and(src1=thresh, src2=thresh, mask=mask)

        total = cv2.countNonZero(mask)
        if marked is None or total > marked[0]:
            marked = (total, cnt_idx)

    color = (0, 0, 255)
    key = ANSWER_KEY[question]

    if key == marked[1]:
        color = (0, 255, 0)
        correct += 1

    cv2.drawContours(image=img, contours=[fields[key]], contourIdx=-1, color=color, thickness=2)

checked = cv2.copyMakeBorder(
    img, top=50, bottom=0, left=0, right=0,
    borderType=cv2.BORDER_CONSTANT, value = (255, 255, 255)
    )

score = (correct / 10)

color = (50, 168, 82) if score >= 0.6 else (71, 7, 219)
text = 'Passed' if score >= 0.6 else 'Failed'

cv2.putText(img=checked, text=f'{text}: {score * 100}%', org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.9,
            color=color, thickness=2)

# cv2.imwrite('checked.png', checked)
cv2.imshow('image', checked)
cv2.waitKey(0)