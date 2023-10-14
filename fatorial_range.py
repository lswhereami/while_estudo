#!/usr/bin/python3
fator = int(input('Digite um numero'))
valor = 1
for n in range(0, fator):
    valor = valor * (n + 1)

print(valor)