#Jogo Básico De Par Ou Impar Desenvolvido Para O Exercício Do Curso Em Vídeo.

import random
from time import sleep

escolhajogador = ' '
escolhapc = 0
count = 0

while True:
    escolhajogador = int(input(('\33[33mEscolha Um Numero De 0 A 10. ')))
    if escolhajogador > 10 or escolhajogador < 0:
        print('\33[31mSó É Aceito Numeros De 0 A 10.')
        exit()
    escolhapc = random.randint(0, 10)
    parouimpar = (input('\33[34mEscolha Impar Ou Par. ')).lower()
    if parouimpar != 'par' and parouimpar != 'impar':
        print('\33[31mSó É Aceito Par Ou Impar')
        exit()
    sleep(0.50)
    print(f'\33[35mO Resultado Foi: {escolhapc+escolhajogador}')
    print(f'\33[31mA Maquina Escolheu: {escolhapc}')
    sleep(0.50)
    if (escolhapc + escolhajogador) % 2 == 0:
        if parouimpar == 'par':
            print('\33[1;32mO Jogador Venceu!\33[m ')
            count += 1
        else:
            print('\33[1;31mA Maquina Venceu!\33[m ')
            count = 0
            desejaparar = input('\33[34mDeseja Continuar?\n[S]\n[N] ').lower()
            if desejaparar == 'n':
                break
            elif desejaparar != 's' and desejaparar != 'n':
                print('\33[31mSó É Aceito "S" Ou "N".')
                exit()
    if (escolhapc + escolhajogador) % 2 != 0:
        if parouimpar == 'impar':
            print('\33[1;32mO Jogador Venceu!\33[m ')
            count += 1
        else:
            print('\33[1;31mA Maquina Venceu!\33[m ')
            count = 0
            desejaparar = input('\33[34mDeseja Continuar?\n[S]\n[N] ').lower()
            if desejaparar == 'n':
                break
            elif desejaparar != 's' and desejaparar != 'n':
                print('\33[31mSó É Aceito "S" Ou "N".')
                exit()
    print(f'\33[32mVitorias Consecutivas: {count}')


