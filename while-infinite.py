def whileloop():
    valor0 = 0
    valor1 = 1
    limitador = 100
    soma = valor0 + valor1

    print(f'{valor0},{valor1},', end=',')
    while soma < limitador: # while True
        soma = valor0 + valor1
        print(soma, end=',')
        valor0 = valor1
        valor1 = soma

if __name__=='__main__':
    whileloop()