''' -----> Desafio 2: Functions 
Criar um programa que calcula a quantidade de tinta necessária para 
pintar uma parede. O usuário deverá fornecer as seguintes
informações: rendimento, altura e largura.
O programa deve mostrar na tela a mensagem "Você necessita de x lata de tinta".
'''

#importar o módulo math para realizar uma aproximação maior do número de latas ----> math.ceil (maior), math.floor (menor)

import math
rend = float(input('Insira o rendimento da lata de tinta (m^2): '))
largura = float(input('Insira a largura da parede (m^2): '))
altura = float(input('Insira a altura da parede (m^2): '))
def calculo():
    area_parede = float(largura * altura)
    latas = float(area_parede / rend)    
    return latas 
resultado = calculo()
print(f'Você precisa de {math.ceil(resultado)} latas de tinta.')
print()
