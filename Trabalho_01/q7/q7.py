import cv2
import numpy as np

def quantizar_imagem(imagem, num_cores=64):
    # Dividir o intervalo de valores de 0 a 255 em 'num_cores' cores
    fator_quantizacao = 256 // num_cores
    
    # Quantizar cada canal RGB
    imagem_quantizada = (imagem // fator_quantizacao) * fator_quantizacao + fator_quantizacao // 2
    
    return imagem_quantizada.astype(np.uint8)


def detectar_bordas(imagem):
    # Converter a imagem para escala de cinza manualmente
    imagem_gray = 0.299 * imagem[:, :, 0] + 0.587 * imagem[:, :, 1] + 0.114 * imagem[:, :, 2]

    # Definir os kernels Sobel para gradiente horizontal (Gx) e vertical (Gy)
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # Inicializar a imagem de bordas
    altura, largura = imagem_gray.shape
    bordas = np.zeros_like(imagem_gray)

    # Aplicar o filtro Sobel (convolução) para detectar bordas
    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            # Extrair a janela 3x3 ao redor de cada pixel
            janela = imagem_gray[i - 1:i + 2, j - 1:j + 2]
            
            # Aplicar os kernels sobel_x e sobel_y
            gx = np.sum(sobel_x * janela)
            gy = np.sum(sobel_y * janela)
            
            # Calcular a magnitude do gradiente
            bordas[i, j] = np.sqrt(gx**2 + gy**2)

    # Normalizar o resultado para o intervalo [0, 255]
    bordas = (bordas / np.max(bordas)) * 255

    return bordas.astype(np.uint8)


# Carregar a imagem original RGB
imagem_rgb = cv2.imread('../image/cidade_1024X1024.png')

# Quantizar a imagem para reduzir a quantidade de cores
imagem_quantizada = quantizar_imagem(imagem_rgb, num_cores=64)

# Detectar bordas na imagem quantizada
bordas = detectar_bordas(imagem_quantizada)

# Salvar a imagem quantizada e a imagem com bordas detectadas
cv2.imwrite('imagem_quantizada.png', imagem_quantizada)
cv2.imwrite('imagem_bordas.png', bordas)
