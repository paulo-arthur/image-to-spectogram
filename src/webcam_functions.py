import cv2, datetime

def capture_image():
    # inicializa a webcam
    cam = cv2.VideoCapture(0)

    # captura um frame
    ret, frame = cam.read()

    if not ret:
        print("A captura de imagem falhou!")
    else:
        image_filename = str(datetime.datetime.now()).replace(" ", "_")[:19] + ".png"

        cv2.imwrite(image_filename, frame)

    cam.release()
    return image_filename