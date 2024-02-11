import matplotlib.pyplot as plt

# Parameters for the investment
valor_investido_mes =   5000
taxa_de_juros_mensal =   0.005  #   0.5% mesly interest rate
tempo_do_investimento =   10
total_de_meses = tempo_do_investimento *   12
total_de_trimestres = total_de_meses //   3


# Initialize the starting value for the investment
valor_inicial =   0

# List to store the quarterly values
valores_trimestrais = []


# Start at mes  1 because mes  0 has no interest applied
for mes in range(1, total_de_meses + 1):
    # Increase the investment by the mesly amount
    valor_inicial += valor_investido_mes
    # Apply the interest to the current value
    valor_inicial += valor_inicial * taxa_de_juros_mensal

    # Check if we're at the end of a quarter and record the value
    if (mes +  2) %  3 ==  0:  # +2 because we start counting from  1, not  0
        valores_trimestrais.append(valor_inicial)


# Plot the quarterly values
plt.figure(figsize=(10,   6))
plt.scatter(range(1, len(valores_trimestrais) +   1), valores_trimestrais)
plt.title('Investmento')
plt.xlabel('Trimestre')
plt.ylabel('Valor total (BRL)')
plt.grid(True)
plt.show()
