import random

class MochilaGA:
    def __init__(self, itens, capacidade, tam_pop):
        self.itens = itens
        self.capacidade = capacidade
        self.tam_pop =  tam_pop
        self.n_itens = len(itens)
    
    def calcular_fitness(self,cromossomo):
        v_total = sum(cromossomo[i] * self.itens[i].valor for i in range(self.n_itens))
        p_total = sum(cromossomo[i] * self.itens[i].peso for i in range(self.n_itens))
        
        if p_total <= self.capacidade:
            return v_total
        else:
            excedente = p_total - self.capacidade
            return v_total - (v_total * excedente)
    
    def selecao_torneio(self, populacao):
        competidores = random.sample(populacao, 3)
        return max(competidores, key = self.calcular_fitness)
    
    def cruzamento(self, pai1, pai2):
        ponto  =  random.randint(1,self.n_itens - 1)
        
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
        return filho1, filho2
    
    def mutacao(self, individuo, taxa=0.1):
        for i in range(self.n_itens):
            if random.random() < taxa:
                individuo[i] = 1 - individuo[i]
    
    def executa(self, n_geracoes):
        populacao = [[random.randint(0, 1) for _ in range(self.n_itens)]
                     for _ in range(self.tam_pop)]
        historico_fitnnes = []
        
        for _ in range(n_geracoes):
            populacao.sort(key=self.calcular_fitness, reverse=True)
            
            melhor_atual_fit = self.calcular_fitness(populacao[0])
            historico_fitnnes.append(melhor_atual_fit)
            
            nova_pop = [populacao[0]]
            
            while len(nova_pop) < self.tam_pop:
                pai1 = self.selecao_torneio(populacao)
                pai2 = self.selecao_torneio(populacao)
                
                filho1,filho2 = self.cruzamento(pai1,pai2)
                self.mutacao(filho1)
                self.mutacao(filho2)
                nova_pop.extend([filho1,filho2])
            
            populacao = nova_pop[:self.tam_pop]
        
        melhor = max(populacao, key=self.calcular_fitness)
        return melhor, historico_fitnnes
            