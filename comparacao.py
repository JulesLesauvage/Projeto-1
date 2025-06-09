# Importamos as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === 1. Carregar os dados exportados do ParaView ===
# Certifique-se de que o arquivo 'openfoam_profile.csv' está no mesmo diretório
dados = pd.read_csv('openfoam_profile.csv')

# === 2. Extrair as informações relevantes ===
# 'Points:1' corresponde à coordenada y (posição vertical)
# 'U:0' é a componente da velocidade na direção x (assumimos escoamento unidimensional)
y_numerico = dados['Points:1']
u_numerico = dados['U:0']

# === 3. Definir os parâmetros físicos ===
mu = 1e-3       # viscosidade dinâmica (Pa.s)
G = 1           # gradiente de pressão (Pa/m)
h = max(abs(y_numerico))  # altura da meia-canal estimada a partir dos dados

# === 4. Calcular a solução analítica de Poiseuille ===
# Fórmula: u(y) = (G / 2μ) * (h² - y²)
y_analitico = np.linspace(-h, h, 100)
u_analitico = (G / (2 * mu)) * (h**2 - y_analitico**2)

# === 5. Plotar os perfis de velocidade ===
plt.figure(figsize=(8, 5))
plt.plot(u_analitico, y_analitico, '--', color='black', label='Solução Analítica')
plt.plot(u_numerico, y_numerico, '-', color='red', linewidth=2, label='OpenFOAM')

# === 6. Personalizar o gráfico ===
plt.xlabel('Velocidade u (m/s)')
plt.ylabel('Posição y (m)')
plt.title('Comparação do Perfil de Velocidade: Analítica vs Numérica')
plt.grid(True)
plt.legend()
plt.tight_layout()

# === 7. Salvar e exibir ===
plt.savefig('comparacao.png', dpi=300)  # Salva a imagem com boa resolução
plt.show()
