import cv2

def testar_camera():
    # 0 tenta abrir a webcam do PC
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("\n[AVISO] Não foi possível aceder à Webcam (normal se estiveres num servidor ou PC sem câmara).")
        print("[SUCESSO] Mas o OpenCV está a funcionar perfeitamente!\n")
        return

    print("\n[SUCESSO] Câmara aberta! Pressiona 'q' na janela do vídeo para fechar.\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Project Palanca - Teste", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    testar_camera()
