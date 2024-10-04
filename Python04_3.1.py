#!/usr/bin/env python3

############## Questão 3 ###############
#### Método 1 ####
my_list = ['a','bb','ccc']
list_copy = my_list # Ambas as listas foram alteradas porque apenas foi copiado um ponteiro para a lista original quando escreve-se copy_list=my_list, ou seja, não se criou uma cópia independente
print(my_list)
list_copy.append('dddd')
print(my_list)
