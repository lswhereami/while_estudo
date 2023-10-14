#!/usr/bin/python3

x = int(input('Digite um número inteiro:'))
cont = 0
while(x != 0):
    sobra = x % 10
    x = x//10
    cont = cont + sobra
print(cont)
