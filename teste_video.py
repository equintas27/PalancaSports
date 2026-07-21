import cv2

def     test_video_stream():
    video_path = "Videos/futebol.mp4"
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print ("Erro ao abrir vídeo")
        return 
    cv2.namedWindow("Palanca Sports - Scouting Track", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Palanca Sports - Scouting Track", 1920, 1080)
    while cap.isOpened():

        ret, frame = cap.read()
        if not ret:
            print ("Erro ao carregar frame")
            break 
        cv2.imshow("Palanca Sports - Scouting Track", frame)
        if cv2.waitKey(20) & 0xFF == 27 or cv2.waitKey(20) & 0xFF == ord('q') :
            print ("Usuário saiu do video!")
            break 

if __name__ == "__main__":
    test_video_stream()