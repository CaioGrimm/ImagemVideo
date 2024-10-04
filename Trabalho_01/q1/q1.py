import cv2
import numpy as np

def alterar_brilho(imagem, fator_brilho):
    # Criação de uma nova matriz de mesmo tamanho e tipo para armazenar a imagem alterada
    imagem_brilho = np.zeros_like(imagem)

    # Iterar sobre cada pixel para ajustar o brilho manualmente
    altura, largura, canais = imagem.shape
    for i in range(altura):
        for j in range(largura):
            for c in range(canais):
                # Ajustar o brilho e garantir que os valores estejam no intervalo [0, 255]
                novo_valor = int(imagem[i, j, c]) + fator_brilho
                if novo_valor > 255:
                    novo_valor = 255
                elif novo_valor < 0:
                    novo_valor = 0
                
                # Atribuir o valor ajustado ao pixel da nova imagem
                imagem_brilho[i, j, c] = novo_valor

    return imagem_brilho

# Lendo a imagem
imagem = cv2.imread('../image/cidade_300x300.png')  # Carregar a imagem com OpenCV

# Alterar o brilho
fator_brilho = 50  # Exemplo: aumenta o brilho em 50 unidades
imagem_brilho = alterar_brilho(imagem, fator_brilho)

# Salvar a nova imagem
cv2.imwrite('imagem_brilho.png', imagem_brilho)

