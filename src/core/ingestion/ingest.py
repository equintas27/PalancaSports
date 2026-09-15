import cv2

def openVideo (path :str):
    if not path:
        return 
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print ("Erro ao abrir este ficheiro!")
        return 
    cv2.namedWindow("Palanca Sports", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Palanca Sports", 800, 600)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print ("Erro ao ler o frame")
            break 
        cv2.imshow("Palanca Sports", frame)
        cv2.waitKey(250)
    cap.release()
    cv2.destroyAllWindows()