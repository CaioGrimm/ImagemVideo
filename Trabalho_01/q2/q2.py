import cv2
import numpy as np

def inverter_cores(imagem):
    # Criar uma nova matriz para armazenar a imagem invertidaS
    imagem_negativa = np.zeros_like(imagem)
    
    # Iterar sobre cada pixel e inverter as cores
    altura, largura, canais = imagem.shape
    for i in range(altura):
        for j in range(largura):
            for c in range(canais):
                # Subtrair o valor do pixel de 255 para inverter a cor
                imagem_negativa[i, j, c] = 255 - imagem[i, j, c]
    
    return imagem_negativa

# Carregar a imagem com OpenCV
imagem = cv2.imread('../image/cidade_1024X1024.png')  

# Inverter as cores
imagem_negativa = inverter_cores(imagem)

# Salvar a imagem negativaS
cv2.imwrite('imagem_negativa.png', imagem_negativa)
