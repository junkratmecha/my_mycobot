# ls /dev/video*
import cv2

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

ret, frame = cap.read()

cv2.imshow('Captured Image', frame)

cv2.waitKey(0)

cv2.destroyAllWindows()

cap.release()