import cv2
import numpy as np

def quantizar_imagem(imagem, num_cores=64):
    # Dividir o intervalo de valores de 0 a 255 em 'num_cores' cores
    fator_quantizacao = 256 // num_cores
    
    # Quantizar cada canal RGB
    imagem_quantizada = (imagem // fator_quantizacao) * fator_quantizacao + fator_quantizacao // 2
    
    return imagem_quantizada.astype(np.uint8)

def classificar_borda_interior(imagem_quantizada, bordas):
    # Criar máscaras de borda e interior
    borda_mask = bordas > 0
    interior_mask = bordas == 0

    # Criar imagens para bordas e interiores
    imagem_borda = np.ones_like(imagem_quantizada) * 255  # Branco por padrão
    imagem_interior = np.ones_like(imagem_quantizada) * 255  # Branco por padrão

    # Preencher a imagem de bordas com a cor original dos pixels de borda
    imagem_borda[borda_mask] = imagem_quantizada[borda_mask]

    # Preencher a imagem de interiores com a cor original dos pixels de interior
    imagem_interior[interior_mask] = imagem_quantizada[interior_mask]

    return imagem_borda, imagem_interior

def calcular_histograma(imagem_quantizada, mascara):
    # Calcular o histograma para os pixels da imagem baseados na máscara
    # Somente considerar os pixels da máscara
    pixels = imagem_quantizada[mascara].reshape(-1, 3)  # Pegar apenas os pixels com máscara válida
    histograma = np.zeros((256, 3), dtype=int)  # Histograma de 256 níveis para R, G e B

    for pixel in pixels:
        histograma[pixel[0], 0] += 1  # Canal R
        histograma[pixel[1], 1] += 1  # Canal G
        histograma[pixel[2], 2] += 1  # Canal B

    return histograma

# Função principal para aplicar o descritor BIC
def extrair_descritor_bic(imagem_quantizada, bordas):
    # Classificar os pixels como bordas e interior
    imagem_borda, imagem_interior = classificar_borda_interior(imagem_quantizada, bordas)

    # Criar máscaras para borda e interior
    borda_mask = bordas > 0
    interior_mask = bordas == 0

    # Calcular os histogramas
    histograma_borda = calcular_histograma(imagem_quantizada, borda_mask)
    histograma_interior = calcular_histograma(imagem_quantizada, interior_mask)

    return imagem_borda, imagem_interior, histograma_borda, histograma_interior

# Carregar a imagem original RGB e a imagem de bordas
imagem_rgb = cv2.imread('../image/cidade_1024X1024.png')
bordas = cv2.imread('../q7/imagem_bordas.png', cv2.IMREAD_GRAYSCALE)

# Quantizar a imagem manualmente para reduzir a quantidade de cores (64 cores, por exemplo)
imagem_quantizada = quantizar_imagem(imagem_rgb, num_cores=64)

# Extrair as imagens e histogramas do descritor BIC
imagem_borda, imagem_interior, histograma_borda, histograma_interior = extrair_descritor_bic(imagem_quantizada, bordas)

# Salvar as imagens de borda e interior
cv2.imwrite('imagem_borda.png', imagem_borda)
cv2.imwrite('imagem_interior.png', imagem_interior)

# Salvar os histogramas em um arquivo de texto
np.savetxt('histograma_borda.txt', histograma_borda, fmt='%d', header='Histograma de Borda (R, G, B)')
np.savetxt('histograma_interior.txt', histograma_interior, fmt='%d', header='Histograma de Interior (R, G, B)')
