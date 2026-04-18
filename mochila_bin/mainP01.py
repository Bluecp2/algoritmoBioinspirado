import matplotlib
import os
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from Item import Item
from MochilaGA import MochilaGA


nome_pasta = "saida_P01"
if not os.path.exists(nome_pasta):
    os.makedirs(nome_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso")

c = 165
valores_p = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
pesos_w = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
lista_itens = [Item(i,v,p) for i,(v,p) in enumerate(zip(valores_p, pesos_w))]
ag = MochilaGA(itens=lista_itens, capacidade=c,tam_pop=30)
melhor_solucao, historico = ag.executa(n_geracoes=50)
peso_melhor_solucao = sum(melhor_solucao[i] * lista_itens[i].peso for i in range(len(melhor_solucao)))

plt.plot(historico, label='Melhor Fitness')
plt.title('Convergência do Algoritmo Genético')
plt.xlabel('Geração')
plt.ylabel('Fitness (Valor Total)')
plt.grid(True)
plt.legend()
caminho_grafico = os.path.join(nome_pasta,'convergencia_P01.png')
plt.savefig(caminho_grafico)

caminho_texto = os.path.join(nome_pasta, "melhor_solucao.txt")

with open(caminho_texto, "w") as arquivo:
    arquivo.write("Resultado")
    arquivo.write(f"Melhor solução: {melhor_solucao}\n")
    arquivo.write(f"Melhor solução peso: {peso_melhor_solucao}\n")
    arquivo.write(f"Melhor solução fit: {ag.calcular_fitness(melhor_solucao)}")



