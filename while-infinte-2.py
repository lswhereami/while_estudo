def whileloop():
    valor0 = 0
    valor1 = 1
    limitador = 100
    soma = valor0 + valor1

    print(f'{valor0},{valor1},', end=',')
    while soma < limitador:  # while True
        valor0, valor1 = valor1, valor0 + valor1
        print(valor1, end=',')


if __name__ == '__main__':
    whileloop()
