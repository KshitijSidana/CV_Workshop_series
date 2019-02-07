import cv2

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('raw', img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            edges = cv2.Canny(blur, 1000, 1500, apertureSize=5)
            cv2.imshow('edge', edges)
            ch = cv2.waitKey(1)
            if ch == 27:
                break
    cv2.destroyAllWindows()
