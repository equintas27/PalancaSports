# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    teste_opencv.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: equintas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/08 17:34:58 by equintas          #+#    #+#              #
#    Updated: 2026/07/08 17:35:03 by equintas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import cv2

def test_openv():
    image = cv2.imread('Barcelona.png')
    if image is None:
        print ("Erro na leitura da imagem")
        return 
    cv2.imshow('My image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    test_openv()
