import cv2
import imutils

img = cv2.imread('assets/view.jpg')
logo = cv2.imread('assets/python.png')
logo = imutils.resize(logo, height=150)

#roi - region of interest
rows, cols, channels = logo.shape
roi = img[:rows, :cols]

gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY) #blue green red to gray #zamiana koloru na szary

mask = cv2.threshold(gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY)[1] #progowanie - piksele jaśniejsze od wyznaczonego progu otrzymują jedną wartość, a ciemniejsze drugą
mask_inv = cv2.bitwise_not(mask) #odwrocenie progowania

img_bg = cv2.bitwise_and(roi, roi, mask=mask) #wyciagniecie tla z glownego obrazu
logo_fg = cv2.bitwise_and(logo, logo, mask=mask_inv) #usuniecie tla z obrazu

dst = cv2.add(img_bg, logo_fg) #polaczenie tla i logo
img[:rows, :cols] = dst #wrzucenie tego na glowny obraz
cv2.imshow('output', img)
cv2.waitKey(0)