#!/usr/bin/env python3

############# Questão 2 ###############
taxa = "sapiens, erectus, neanderthalensis" # Cria uma variável chamada 'taxa'
print(taxa) # Imprime a variável 'taxa'
print(taxa[1]) # Imprime a posição 1 da variável taxa ('a', pois cada caracter é um elemento distinto)
print(type(taxa)) # O tipo de variável da 'taxa' é uma string (<class 'str'>)
split_taxa = taxa.split(', ') # Divide a variável taxa em plavras individuais (o delimitador definido é ",")
print(split_taxa)
species = split_taxa # Determina que a variável species é igual a variável split_taxa
print(species)
print(species[1]) #Imprime o elemento 1 da lista species, já que foi utilizado '.split', aparece "erectus"
print(type(species)) # O tipo de arquivo da variável species é uma lista
sorted_species = sorted(species) # Organiza a lista em ordem alfabética
print(sorted_species)
print(sorted(split_taxa, key=len)) # Organiza a lista pelo comprimento (lenght) de cada string
