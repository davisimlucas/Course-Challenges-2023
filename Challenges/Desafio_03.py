''' ----> Desafio 3: List and 
Criar um programa que gere 3 listas de acordo com a necessidade logo abaixo:
- lista 1: funcionários que possuem carro e trabalham a noite
- lista 2: funcionários que possuem carro e trabalham durante o dia
- lista 3: funcionários que não têm carro.
'''

funcionários = {'Ana', 'Alice', 'Marcos', 'Pedro', 'Sofia', 'Bruno', 'Melissa'}
diurno = {'Ana', 'Alice', 'Marcos', 'Melissa'}
noturno = {'Pedro', 'Sofia', 'Bruno'}
tem_carro = {'Alice', 'Marcos','Bruno', 'Melissa'}


lista_1 = (noturno & tem_carro)
lista_2 = (diurno & tem_carro)
lista_3 = (funcionários - tem_carro)

print()
print(list(lista_1))
print(list(lista_2))
print(list(lista_3))
print()
