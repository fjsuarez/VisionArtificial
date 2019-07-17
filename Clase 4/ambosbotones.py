import cv2
import numpy as np

def crear_circulo(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0,255,0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0,0,255), -1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(winname='mi_dibujo')
cv2.setMouseCallback('mi_dibujo',crear_circulo)

while True:
    cv2.imshow('mi_dibujo', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()