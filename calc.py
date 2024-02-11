
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

valor_investido_mes =   5000
taxa_de_juros_mensal =   0.005  #   0.5% mesly interest rate
tempo_do_investimento =   10
total_de_meses = tempo_do_investimento *   12
total_de_trimestres = total_de_meses //   3


valor_inicial =   0

valores_trimestrais = []


for mes in range(1, total_de_meses + 1):

    valor_inicial += valor_investido_mes

    valor_inicial += valor_inicial * taxa_de_juros_mensal

    if (mes +  2) %  3 ==  0:
        valores_trimestrais.append(valor_inicial)


plt.figure(figsize=(10,   6))
plt.bar(range(1, len(valores_trimestrais) +   1), valores_trimestrais)
plt.title('Investimento')
plt.xlabel('Trimestre')
plt.ylabel('Valor total (BRL)')
plt.grid(True)

# Remove padding by setting x-limits to exactly fit the data
plt.xlim(0, len(valores_trimestrais) + 1)


plt.show()
