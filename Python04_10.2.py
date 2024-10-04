#!/usr/bin/env python3

############## Questão 10 #################
import sys # Importa o módulo sys, que dá acesso a variáveis e funções como sys.argv

começo = int(sys.argv[1]) # variável começo é convertida para numero inteiro, e é o primeiro argumento fornecido pelo usuário na linha de comando (lembre-se que sys.arv[0] se refere ao nome do arquivo do script)

final = int(sys.argv[2]) + 1 # o segundo argumento da linha de comando (excluindo o sys.argv[0]) e o converte em um número inteiro. Em seguida, soma 1 a este valor pois a função range() não conta o último valor (range(0,4) vai até 3).

[print (num) for num in range(começo,final) if num % 2 != 0] # faz o mesmo que a linha anterior mas adiciona uma condição: só será impresso os números que forem ímpares (resto da divisão por 2 diferente de 0)
