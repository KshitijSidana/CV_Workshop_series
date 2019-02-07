import cv2
import numpy as np

kernel = np.array([[1, 0, 1],
                   [0, -4, 0],
                   [1, 0, 1]])

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('raw', img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            dst = cv2.filter2D(img, -1, kernel)
            cv2.imshow('filter', dst)
            ch = cv2.waitKey(1)
            if ch == 27:
                break
    cv2.destroyAllWindows()