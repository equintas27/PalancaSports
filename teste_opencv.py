import cv2

def test_openv():
    image = cv2.imread('Barcelona.png')
    if image is None:
        print ("Erro na leitura da imagem")
        return 
    cv2.namedWindow("Palanca Grande", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Palanca Grande", 1920, 1080)
    cv2.imshow('Palanca Grande', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    test_openv()
