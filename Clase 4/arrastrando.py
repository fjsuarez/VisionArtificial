import cv2
import numpy as np

dibujando = False
ix, iy = -1, -1


def crear_rectangulo(event, x, y, flags, params):
    global dibujando, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        ix, iy = x, y
    if event == cv2.EVENT_MOUSEMOVE:
        if dibujando:
            cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), -1)
    if event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), -1)


img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(winname='mi_dibujo')
cv2.setMouseCallback('mi_dibujo',crear_rectangulo)

while True:
    cv2.imshow('mi_dibujo', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()