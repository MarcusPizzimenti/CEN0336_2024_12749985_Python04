#!/usr/bin/env python3

############ Questão 7 ################
numeros = [101,2,15,22,95,33,2,27,72,15,52]
numeros_ordenados = sorted(numeros)  # Organiza de maneira crescente os números da lista

soma_par = 0
soma_impar = 0   # Inicializa duas variávies (soma_par e soma_impar) com valor zero, estas representarão soma dos nº pares e ímpares

for numero in numeros_ordenados: #Inicia uma iteração
    print(numero)
    if numero % 2 == 0:  # se o número for par, o resto da divisão será igual a 0
        soma_par += numero  # se o número for par (satisfaz a condição if), ele é adicionado a variável soma_par
    else:
        soma_impar += numero  # caso a condição if não seja atendida (número é ímpar), ele é adicionado a variável soma_impar
print("Soma dos números pares:", soma_par, "\nSoma dos números ímpares:", soma_impar) #Imprime no formato string-variável soma, para as duas variáveis. '\n' indica uma quebra de linha
