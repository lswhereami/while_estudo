def whileloop(quantidade):
    soma = [0, 1]
    while True:
        soma.append(sum(soma[-2:]))
        if len(soma) == quantidade:
            break
    return soma


if __name__ == '__main__':
    for loop in whileloop(20):
        print(loop)
