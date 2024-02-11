
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

valor_investido_mes =   5000
taxa_de_juros_mensal =   0.005  #   0.5% mesly interest rate
tempo_do_investimento_em_anos =   3
total_de_meses = tempo_do_investimento_em_anos *   12


valor_inicial =   0

valor_mes_a_mes = []


for mes in range(1, total_de_meses + 1):

    valor_inicial += valor_investido_mes

    valor_inicial += valor_inicial * taxa_de_juros_mensal

    # print valor inicial no formato BRL com 2 casas decimais
    print(f'mes {mes}: R$ {valor_inicial:.2f}')
    
    valor_mes_a_mes.append(valor_inicial)


# Function to format y-axis labels
def thousand_formatter(x, pos):
    return f'{x/1000:,.0f} K'

thousand_fmt = FuncFormatter(thousand_formatter)

plt.figure(figsize=(10,   6))
plt.bar(range(1, len(valor_mes_a_mes) +   1), valor_mes_a_mes)


for i, v in enumerate(valor_mes_a_mes):

    padding = 10
    
    plt.text(
        i + 1,
        v + padding,
        f'{v:.2f}',
        color='black',
        ha='center',
        va='bottom',
        rotation=90
        )
 

plt.title('investimento')
plt.xlabel('mes')
plt.ylabel('total acumulado (R$)')
plt.grid(which='major', axis='y')


# decrease the thikness of the grid lines
plt.gca().grid(color='gray', linestyle='dashed', linewidth=0.1)


# remove padding by setting x-limits to exactly fit the data
plt.xlim(0, len(valor_mes_a_mes) + 1)
plt.xticks(range(0, len(valor_mes_a_mes)+1, 2))

# define the padding for the y-axis values
plt.tick_params(axis='y', which='major', pad=5)

# apply the custom formatter to the y-axis
plt.gca().yaxis.set_major_formatter(thousand_fmt)

# ommits the superior and right borders of the graph
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# increase the thikness of the x and y major axes
plt.gca().spines['bottom'].set_linewidth(2.5)
plt.gca().spines['left'].set_linewidth(2.5)


plt.show()
