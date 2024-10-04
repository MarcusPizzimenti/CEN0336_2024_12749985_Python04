#!/usr/bin/env python3

# Não esqueça de utilizar na linha de comando: chmod +x TAREFA4.py

########## Questão 1 ############

coisas_favoritas = ['Café','Formula1','Academia','Viajar','Amigos']  # Lista das coisas que eu gosto
print(coisas_favoritas)   # Imprime minha lista
print(coisas_favoritas[2]) # Imprime o elemento do meio da lista (lembrando que no python, o índice começa em 0)

coisas_favoritas[2] = 'Sabiá' # Troca o elemento do meio ("Academia") por "Sabiá"
print(coisas_favoritas) # Imprime a lista com a mudança do elemento do meio (lembre-se que listas são mutáveis)

coisas_favoritas.append('Correr') # Adiciona um novo elemento ao final da lista ('Correr')
#print(coisas_favoritas)
coisas_favoritas.insert(0,'Tênis') # Adiciona um novo elemento ao começo da lista ('Tênis')
#print(coisas_favoritas)
coisas_favoritas.insert(3,'Frutas') # Insere um novo elemento a posição 3 da lista (nem no começo, nem no final)
#print(coisas_favoritas)
coisas_favoritas.pop() # Remove o último elemento da lista
#print(coisas_favoritas)

coisas_favoritas.remove('Tênis') # remove o elemento 'Tênis' da lista (começo da lista)
#print(coisas_favoritas)
coisas_favoritas.pop(3) # Remove o elemento que está na posição 3 da lista
#print(coisas_favoritas)

coisas_favoritas_string = ", ".join(coisas_favoritas) # Cria uma string, juntando os elementos da lista, os quais são separados por uma vírgula
print(coisas_favoritas_string)
