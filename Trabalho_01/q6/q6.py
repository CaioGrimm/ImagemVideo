import numpy as np
import cv2
from collections import Counter

def filtro_media(imagem, kernel_size=3):
    altura, largura, canais = imagem.shape
    padding = kernel_size // 2
    imagem_padded = np.pad(imagem, ((padding, padding), (padding, padding), (0, 0)), mode='constant', constant_values=0)
    imagem_filtrada = np.zeros_like(imagem)

    # Iterar sobre cada canal RGB
    for c in range(canais):
        for i in range(padding, altura + padding):
            for j in range(padding, largura + padding):
                # Extrair a vizinhança
                janela = imagem_padded[i - padding:i + padding + 1, j - padding:j + padding + 1, c]
                # Calcular a média e atribuir ao pixel
                imagem_filtrada[i - padding, j - padding, c] = np.mean(janela)

    return imagem_filtrada

def filtro_k_vizinhos(imagem, kernel_size=3, k=4):
    altura, largura, canais = imagem.shape
    padding = kernel_size // 2
    imagem_padded = np.pad(imagem, ((padding, padding), (padding, padding), (0, 0)), mode='constant', constant_values=0)
    imagem_filtrada = np.zeros_like(imagem)

    # Iterar sobre cada canal RGB
    for c in range(canais):
        for i in range(padding, altura + padding):
            for j in range(padding, largura + padding):
                # Extrair a vizinhança
                janela = imagem_padded[i - padding:i + padding + 1, j - padding:j + padding + 1, c].flatten()
                # Ordenar e pegar os K vizinhos mais próximos
                vizinhos_proximos = np.sort(janela)[:k]
                # Calcular a média dos K vizinhos mais próximos
                imagem_filtrada[i - padding, j - padding, c] = np.mean(vizinhos_proximos)

    return imagem_filtrada


def filtro_mediana(imagem, kernel_size=3):
    altura, largura, canais = imagem.shape
    padding = kernel_size // 2
    imagem_padded = np.pad(imagem, ((padding, padding), (padding, padding), (0, 0)), mode='constant', constant_values=0)
    imagem_filtrada = np.zeros_like(imagem)

    # Iterar sobre cada canal RGB
    for c in range(canais):
        for i in range(padding, altura + padding):
            for j in range(padding, largura + padding):
                # Extrair a vizinhança
                janela = imagem_padded[i - padding:i + padding + 1, j - padding:j + padding + 1, c].flatten()
                # Calcular a mediana
                imagem_filtrada[i - padding, j - padding, c] = np.median(janela)

    return imagem_filtrada

def filtro_moda(imagem, kernel_size=3):
    altura, largura, canais = imagem.shape
    padding = kernel_size // 2
    imagem_padded = np.pad(imagem, ((padding, padding), (padding, padding), (0, 0)), mode='constant', constant_values=0)
    imagem_filtrada = np.zeros_like(imagem)

    # Iterar sobre cada canal RGB
    for c in range(canais):
        for i in range(padding, altura + padding):
            for j in range(padding, largura + padding):
                # Extrair a vizinhança (janela deslizante)
                janela = imagem_padded[i - padding:i + padding + 1, j - padding:j + padding + 1, c].flatten()
                
                # Calcular a moda manualmente usando o Counter
                contador = Counter(janela)
                moda = contador.most_common(1)[0][0]  # Acessar o valor mais frequente

                # Atribuir a moda ao pixel correspondente
                imagem_filtrada[i - padding, j - padding, c] = moda

    return imagem_filtrada

def adicionar_ruido(imagem, proporcao=0.1):
    altura, largura, canais = imagem.shape
    imagem_ruidosa = np.copy(imagem)
    num_pix = int(proporcao * altura * largura)

    # Adicionar "sal" (branco)
    coords_sal = [np.random.randint(0, i - 1, num_pix) for i in (altura, largura)]
    imagem_ruidosa[coords_sal[0], coords_sal[1], :] = 255

    # Adicionar "pimenta" (preto)
    coords_pimenta = [np.random.randint(0, i - 1, num_pix) for i in (altura, largura)]
    imagem_ruidosa[coords_pimenta[0], coords_pimenta[1], :] = 0

    return imagem_ruidosa

# Carregar a imagem original
imagem_original = cv2.imread('../image/cidade_1024X1024.png')

# Adicionar ruído sal e pimenta
imagem_ruido = adicionar_ruido(imagem_original, proporcao=0.1)

# Aplicar os filtros
imagem_media = filtro_media(imagem_ruido)
imagem_k_vizinhos = filtro_k_vizinhos(imagem_ruido)
imagem_mediana = filtro_mediana(imagem_ruido)
imagem_moda = filtro_moda(imagem_ruido)

# Salvar as imagens resultantes
cv2.imwrite('imagem_ruido.png', imagem_ruido)
cv2.imwrite('imagem_media.png', imagem_media)
cv2.imwrite('imagem_k_vizinhos.png', imagem_k_vizinhos)
cv2.imwrite('imagem_mediana.png', imagem_mediana)
cv2.imwrite('imagem_moda.png', imagem_moda)


