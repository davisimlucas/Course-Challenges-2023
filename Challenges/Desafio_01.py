''' -------> Desafio If, Elif, Else
Criar um programa que dependendo da temperatura (°C) do steak 
ele retorne o ponto de cozimento em português. O usuário deverá 
fornecer a temperatura 

Temperaturas de Cozimento:
120°F (48°C) - Rare (Selada)
130°F (54°C) - Medium Rare (Ao ponto para mal)
140°F (60°C) - Medium (Ao ponto)
150°F (65°C) - Medium well (Ao ponto para bom)
160°F (71°C) - Well done (Bem passada)
'''
''' -----> Algoritmo 
1: Fazer o usuário entrar com uma temperatura em °C
2: Realizar um cálculo de conversão de unidades de temperatura
3: Montar a estrutura condicional para cada temperatura específica
'''
T_c = float(input('Insira um valor para a temperatura em °C: '))
def T_fahr():
    Tf = float(((T_c * 9)/ 5) + 32)
    print(f'A temperatura pode ser expressa como {Tf:.2f}°F.')
    return Tf

if T_fahr() <= 120:
    print('O steak precisa cozinhar por mais alguns minutos.') 
elif 120 < T_fahr() <= 130:
    print('O steak está selada.')
elif 130 < T_fahr() <= 140:
    print('O steak está ao ponto para mal.')
elif 140 < T_fahr() <= 150:
    print('O steak está ao ponto.')
elif 150 < T_fahr() <= 160:
    print('O steak está ao ponto para bom.')
else: 
    print('O steak está ao ponto.')
