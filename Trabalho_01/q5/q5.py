import cv2
import numpy as np

def expansao_contraste_linear(imagem):
    # Separar os canais manualmente
    canais = [imagem[:, :, 0], imagem[:, :, 1], imagem[:, :, 2]]  # R, G, B

    canais_expandidos = []
    for canal in canais:
        I_min, I_max = np.min(canal), np.max(canal)
        L_min, L_max = 0, 255

        # Aplicar a expansão de contraste
        canal_expansao = (canal - I_min) * ((L_max - L_min) / (I_max - I_min)) + L_min

        # Garantir valores válidos entre 0 e 255
        canal_expansao = np.clip(canal_expansao, 0, 255)
        canais_expandidos.append(canal_expansao)

    # Reunir os canais manualmente
    imagem_expansao = np.stack(canais_expandidos, axis=-1)
    return imagem_expansao.astype(np.uint8)


def compressao_expansao(imagem, c=0.0001):
    # Separar os canais manualmente
    canais = [imagem[:, :, 0], imagem[:, :, 1], imagem[:, :, 2]]  # R, G, B

    canais_comprimidos = []
    for canal in canais:
        # Aplicar a transformação quadrática
        canal_compressao = c * np.power(canal, 2)

        # Reescalar para [0, 255]
        canal_compressao = (canal_compressao - np.min(canal_compressao)) * (255 / (np.max(canal_compressao) - np.min(canal_compressao)))

        # Garantir valores válidos entre 0 e 255
        canal_compressao = np.clip(canal_compressao, 0, 255)
        canais_comprimidos.append(canal_compressao)

    # Reunir os canais manualmente
    imagem_compressao = np.stack(canais_comprimidos, axis=-1)
    return imagem_compressao.astype(np.uint8)

def dente_de_serra(imagem, T=128):
    # Separar os canais manualmente
    canais = [imagem[:, :, 0], imagem[:, :, 1], imagem[:, :, 2]]  # R, G, B

    canais_dente_serra = []
    for canal in canais:
        # Aplicar a função dente de serra
        canal_dente_serra = (canal % T) * (255 // T)

        # Garantir valores válidos entre 0 e 255
        canal_dente_serra = np.clip(canal_dente_serra, 0, 255)
        canais_dente_serra.append(canal_dente_serra)

    # Reunir os canais manualmente
    imagem_dente_serra = np.stack(canais_dente_serra, axis=-1)
    return imagem_dente_serra.astype(np.uint8)

def transformada_logaritmica(imagem):
    # Separar os canais manualmente
    canais = [imagem[:, :, 0], imagem[:, :, 1], imagem[:, :, 2]]  # R, G, B

    canais_log = []
    for canal in canais:
        # Adicionar um pequeno valor para evitar log(0)
        canal_temp = canal + 1e-5

        # Calcular a constante de normalização
        I_max = np.max(canal_temp)
        c = 255 / np.log(1 + I_max)

        # Aplicar a transformação logarítmica
        canal_log = c * np.log(1 + canal_temp)

        # Reescalar para [0, 255]
        canal_log = (canal_log - np.min(canal_log)) * (255 / (np.max(canal_log) - np.min(canal_log)))

        # Garantir valores válidos entre 0 e 255
        canal_log = np.clip(canal_log, 0, 255)
        canais_log.append(canal_log)

    # Reunir os canais manualmente
    imagem_log = np.stack(canais_log, axis=-1)
    return imagem_log.astype(np.uint8)


# Carregar a imagem
imagem = cv2.imread('../image/cidade_1024X1024.png')

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
