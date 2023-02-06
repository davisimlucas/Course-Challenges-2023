'''  Desafio 4: If, ELif and Else
Cálculos de IMC - Índice de Massa Corporal 
- menor que 18,4 = magreza 
- entre 18,5 e 24,9 = normal
- entre 25 e 29,9 = sobre peso
- entre 30 e 39,9 = obesidade 
- maior que 40 = obesidade grave
'''
import math

peso = float(input('Insira seu peso em kg: '))
altura = float(input('Insira sua altura em metros: '))

def cálculo():
    # É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
    imc = float(peso / (pow(altura, 2.0)))
    return imc

print(f'Seu IMC é de {cálculo():.1f}\n')

if cálculo() <= 18.4:
    print('Magreza.')
elif cálculo() >= 18.5 and cálculo() <= 24.9:
    print('Normal.')
elif cálculo() >= 25 and cálculo() <= 29.9:
    print('Sobrepeso.')
elif cálculo() >= 30 and cálculo() <= 39.9:
    print('Obesidade.')
else: 
    print('Obseidade grave.')
print()