import matplotlib.pyplot as plt
import numpy as np

# Função para visualizar o histograma local gerado
def visualizar_histograma_local(histograma_local, num_particoes):
    # Cada partição tem 768 valores (256 para R, 256 para G, 256 para B)
    valores_por_particao = 256 * 3  # R, G, B concatenados

    # Plotar o histograma de cada partição
    plt.figure(figsize=(15, 5 * num_particoes))

    for i in range(num_particoes):
        plt.subplot(num_particoes, 1, i + 1)
        plt.title(f"Histograma da Partição {i + 1}")
        
        # Pegar o intervalo da partição no vetor de histograma
        inicio = i * valores_por_particao
        fim = inicio + valores_por_particao

        # Separar o histograma em R, G e B
        hist_r = histograma_local[inicio:inicio + 256]
        hist_g = histograma_local[inicio + 256:inicio + 512]
        hist_b = histograma_local[inicio + 512:fim]

        plt.plot(hist_r, color='red', label='R')
        plt.plot(hist_g, color='green', label='G')
        plt.plot(hist_b, color='blue', label='B')
        plt.legend()

    plt.tight_layout()
    plt.show()
    

# Carregar o histograma local gerado pelo código anterior
histograma_local = np.loadtxt('histrograma_local.txt', dtype=int)

# Visualizar o histograma local para 3 partições
visualizar_histograma_local(histograma_local, 3)
