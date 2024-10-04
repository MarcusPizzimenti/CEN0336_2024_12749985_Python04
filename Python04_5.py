#!/usr/bin/env python3

############### Questão 5 ####################
contagem = 1000  # Inicia a contagem a partir de 1000
fatorial = 1 # Inicia a multiplicação necessária na fatoração

while contagem > 0:  # Condicional para o loop
    fatorial *= contagem # A cada iteração, fatorial é multiplicado pelo valor atual de contagem
    contagem -= 1 # A cada iteração, a contagem vai reduzindo de 1000 a 1 (um número por ietração)
print(fatorial) # Imprime o resultado final de 1000 fatorial
