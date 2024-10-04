import cv2
import numpy as np

import cv2
import numpy as np

def expansao_contraste_linear(imagem):
    I_min, I_max = np.min(imagem), np.max(imagem)
    L_min, L_max = 0, 255  # Valores desejados

    # Expansão linear manual
    imagem_expansao = (imagem - I_min) * ((L_max - L_min) / (I_max - I_min)) + L_min

    # Clipping manual dos valores para manter no intervalo [0, 255]
    imagem_expansao[imagem_expansao > 255] = 255
    imagem_expansao[imagem_expansao < 0] = 0

    return imagem_expansao

def compressao_expansao(imagem, c=0.0001):
    # Aplicar a transformação quadrática
    imagem_transformada = c * np.power(imagem, 2)

    # Escalar os valores resultantes para [0, 255]
    imagem_transformada = (imagem_transformada - np.min(imagem_transformada)) * (255 / (np.max(imagem_transformada) - np.min(imagem_transformada)))

    return imagem_transformada.astype(np.uint8)


def dente_de_serra(imagem, T=128):
    # Aplicar a função dente de serra
    imagem_transformada = (imagem % T) * (255 // T)

    # Clipping manual dos valores para manter no intervalo [0, 255]
    imagem_transformada[imagem_transformada > 255] = 255
    imagem_transformada[imagem_transformada < 0] = 0

    return imagem_transformada

def transformada_logaritmica(imagem):
    # Adicionar um valor muito pequeno para evitar log(0)
    imagem_temp = imagem + 1e-5  # Adiciona um valor pequeno sem alterar a imagem original

    # Calcular o valor máximo da imagem
    I_max = np.max(imagem_temp)

    # Garantir que I_max não seja zero
    if I_max == 0:
        I_max = 1

    # Calcular a constante de normalização 'c'
    c = 255 / (np.log(1 + I_max))

    # Aplicar a transformação logarítmica
    imagem_transformada = c * np.log(1 + imagem_temp)

    # Normalizar o resultado para a faixa [0, 255]
    imagem_transformada = (imagem_transformada - np.min(imagem_transformada)) * (255 / (np.max(imagem_transformada) - np.min(imagem_transformada)))

    return imagem_transformada.astype(np.uint8)

# Carregar a imagem
imagem = cv2.imread('../image/cidade_1024X1024.png', cv2.IMREAD_GRAYSCALE)

# Aplicar as transformações radiométricas
imagem_expansao = expansao_contraste_linear(imagem)
imagem_compressao = compressao_expansao(imagem)
imagem_dente_serra = dente_de_serra(imagem)
imagem_logaritmica = transformada_logaritmica(imagem)

# Salvar os resultados
cv2.imwrite('imagem_expansao_contraste.png', imagem_expansao)
cv2.imwrite('imagem_compressao_expansao.png', imagem_compressao)
cv2.imwrite('imagem_dente_de_serra.png', imagem_dente_serra)
cv2.imwrite('imagem_logaritmica.png', imagem_logaritmica)
