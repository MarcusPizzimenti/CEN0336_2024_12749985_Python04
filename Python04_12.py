#!/usr/bin/env python3

################# Questão 12 ##################
dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

tupla_dna = [(len(dna),dna) for dna in dna_list]  # Gera um lista de tuplas em que cada tupla contém o comprimento da sequencia e a própria sequencia
print(tupla_dna)
