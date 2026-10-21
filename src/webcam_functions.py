import cv2, datetime

# inicializa a webcam
cam = cv2.VideoCapture(0)

# captura um frame
ret, frame = cam.read()

if not ret:
    print("A captura de imagem falhou!")
else:
    cv2.imshow("Captured", frame)
    datetime_object = datetime.datetime.now()

    cv2.imwrite(str(datetime_object).replace(" ", "_")[:19] + ".png", frame)
    cv2.waitKey(0)
    cv2.destroyWindow("Captured")       

cam.release()