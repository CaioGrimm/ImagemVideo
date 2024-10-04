import cv2
import numpy as np

def calcular_histograma(imagem):
    # Inicializa os histogramas para os canais R, G e B
    histograma_r = np.zeros(256, dtype=int)
    histograma_g = np.zeros(256, dtype=int)
    histograma_b = np.zeros(256, dtype=int)

    # Iterar sobre cada pixel e contar as intensidades
    altura, largura, canais = imagem.shape
    for i in range(altura):
        for j in range(largura):
            histograma_b[imagem[i, j, 0]] += 1  # Canal B
            histograma_g[imagem[i, j, 1]] += 1  # Canal G
            histograma_r[imagem[i, j, 2]] += 1  # Canal R

    return histograma_r, histograma_g, histograma_b

def particionar_e_calcular_histograma(imagem, num_particoes):
    # Altura e largura da imagem
    altura, largura, canais = imagem.shape

    # Tamanhos das partições
    particao_altura = altura // num_particoes
    particao_largura = largura // num_particoes

    histograma_global = []

    # Iterar sobre as partições
    for i in range(num_particoes):
        for j in range(num_particoes):
            # Definir a região da partição
            particao = imagem[i * particao_altura:(i + 1) * particao_altura, j * particao_largura:(j + 1) * particao_largura]

            # Calcular o histograma para esta partição
            hist_r, hist_g, hist_b = calcular_histograma(particao)

            # Concatenar os histogramas R, G, B desta partição e adicionar ao histograma global
            histograma_global.append(np.concatenate((hist_r, hist_g, hist_b)))

    # Concatenar todas as partições em um único vetor
    histograma_global_concatenado = np.concatenate(histograma_global)
    
    return histograma_global_concatenado

# Carregar a imagem
imagem_cidade_caminho = "../image/cidade_1024X1024.png"
imagem = cv2.imread(imagem_cidade_caminho)

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho.")
else:
    # Definir o número de partições (no mínimo 3)
    num_particoes = 3

    # Calcular o histograma local (por partição)
    histograma_local = particionar_e_calcular_histograma(imagem, num_particoes)

    # Salvar o histograma local em um arquivo texto
    np.savetxt("histrograma_local.txt", histograma_local, fmt='%d')

