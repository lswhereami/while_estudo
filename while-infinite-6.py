def whileloop(quantidade):
    soma = [0, 1]
    for _ in range(2, quantidade):
        soma.append(sum(soma[-2:]))
    return soma


if __name__ == '__main__':
    for loop in whileloop(20):
        print(loop)
