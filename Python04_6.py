#!/usr/bin/env python3

########### Questão 6 ##############
numeros = [101,2,15,22,95,33,2,27,72,15,52]

for numero in numeros:  # Iterador, passa de número a número na lista
    if numero % 2 == 0:   # Condicional para um número ser par: o resto da divisão deve ser 0
      print(numero) # Imprime os números que atingiram a condição supracitada
