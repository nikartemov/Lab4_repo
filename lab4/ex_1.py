#!/usr/bin/env python3
from librip.gens import field
from librip.gens import gen_random
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': None, 'price': 7000, 'color': 'white'},
    {'title': None, 'price': None, 'color': 'white'}
]

# Реализация задания 1
g = field(goods, 'title', 'price')
for i in g:
    print(i, end=" ")

print()

num = gen_random(1, 5, 3)
for i in num:
    print(i, end=" ")


#a = [1,2,3,4,5]
#perv = [x**3 for x in a]
#lamb = list(map(lambda x : x**3, a))

#print()
#print(perv)
#print()
#print(lamb)