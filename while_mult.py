#!/usr/bin/python3

quantidade = int(input('digite a quantidade de numeros a ser multiplicado:'))
contador = 0
mult = 1

while contador < quantidade:
    numero = int(input('digite o numero a ser multiplicado:'))
    mult = mult * numero
    contador = contador + 1
print('o valor dos numeros multiplicados e:',mult)