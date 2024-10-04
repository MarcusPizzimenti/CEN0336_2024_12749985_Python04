#!/usr/bin/env python3

############## Questão 3 ###############

#### Método 2 #####
my_list2 = ['a', 'bb', 'ccc']
list_copy2 = my_list2.copy() # Dessa forma, a lista 'list_copy2' é alterada, e a lista 'my_list2' não, ou seja, criou-se uma cópia independente
print(my_list2)
list_copy2.append('dddd')
print(my_list2)
