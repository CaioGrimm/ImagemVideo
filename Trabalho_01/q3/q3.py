import cv2
import numpy as np

def calcular_histograma(imagem):
    # Inicializa os histogramas para os canais R, G e B
    histograma_r = np.zeros(256, dtype=int)
    histograma_g = np.zeros(256, dtype=int)
    histograma_b = np.zeros(256, dtype=int)

    # Verificar as dimensões da imagem
    altura, largura, canais = imagem.shape
    print(f"Dimensões da imagem: {altura}x{largura}, Canais: {canais}")

    # Iterar sobre cada pixel e contar as intensidades
    for i in range(altura):
        for j in range(largura):
            # Para cada canal, incrementar o contador correspondente
            histograma_b[imagem[i, j, 0]] += 1  # Canal B
            histograma_g[imagem[i, j, 1]] += 1  # Canal G
            histograma_r[imagem[i, j, 2]] += 1  # Canal R

    return histograma_r, histograma_g, histograma_b

# Exemplo de uso
imagem = cv2.imread('../image/cidade_1024X1024.png')  # Carregar a imagem com OpenCV

# Calcular os histogramas
histograma_r, histograma_g, histograma_b = calcular_histograma(imagem)

# Concatenar os histogramas em um único vetor
histograma_global = np.concatenate((histograma_r, histograma_g, histograma_b))

# Salvar o vetor do histograma em um arquivo texto
np.savetxt('histograma_global.txt', histograma_global, fmt='%d')

print("Histograma global gerado e salvo em 'histograma_global.txt'.")
