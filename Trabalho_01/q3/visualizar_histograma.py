import matplotlib.pyplot as plt
import numpy as np

# Ler o histograma do arquivo
histograma_lido = np.loadtxt('histograma_global.txt', dtype=int)

# Plotar o histograma
plt.figure(figsize=(12, 6))

# Histograma para R, G, B
plt.subplot(1, 3, 1)
plt.title("Histograma R")
plt.bar(range(256), histograma_lido[:256], color='red')

plt.subplot(1, 3, 2)
plt.title("Histograma G")
plt.bar(range(256), histograma_lido[256:512], color='green')

plt.subplot(1, 3, 3)
plt.title("Histograma B")
plt.bar(range(256), histograma_lido[512:], color='blue')

plt.tight_layout()
plt.show()
