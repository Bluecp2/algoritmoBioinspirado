import pandas as pd
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt


df = pd.read_csv("dados.csv")

# cria a plot
plt.plot(df['Geracao'], df['Fitness'], marker='o', linestyle='-', color='b')

# cria a escala em log
plt.yscale('log')

# adiciona as labels
plt.xlabel('Geração')
plt.ylabel('Fitness (log)')

# adiciona o titulo
plt.title('Evolução do Fitness (Escala Logarítmica)')

# adiciona grid
plt.grid(True, which="both", ls="-", alpha=0.5)


plt.savefig('grafico_fitness_log.png', dpi=300)
print("Sucesso: Gráfico salvo como 'grafico_fitness_log.png'")

