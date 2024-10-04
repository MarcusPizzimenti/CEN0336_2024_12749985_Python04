#!/usr/bin/env python3

############## Questão 13 ################
dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for indice in range(len(dna_list)): #range(len(dna_list)) cria um iterador que percorre todos os indices da lista; cada vez que loop roda, indice assume o valor de um número da sequência gerada por range(len(nt_list)), sendo o indice atual da lista
    print(f"{indice + 1}\t{len(dna_list[indice])}\t{dna_list[indice]}") # imprime o número da posição (+1 porque queremos que a contagem do indice comece em 1, se não colocarmos nada o Python começa com 0), o comprimento da sequência e a sequência, todos separados por tabulação, usando formatação de string.
