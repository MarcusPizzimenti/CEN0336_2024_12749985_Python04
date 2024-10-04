#!/usr/bin/env python3

################ Questão 11 #################
dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for dna in dna_list:    # inicia um loop que percorre cada elemento da lista dna_list
    comprimento_dna = len(dna) # para cada elemento, a função len() calcula o comprimento de nucleotídeos do dna
    print(f"{comprimento_dna}\t{dna}") # Imprime a variável comprimento_dna e o respectivo elemento da lista, '\t' mostra uma tabulação entre estas duas impressões
