def whileloop(limitador):
    soma = [0, 1]
    while soma[-1] < limitador:
        soma.append(sum(soma[-2:]))
    return soma


if __name__ == '__main__':
    for loop in whileloop(100):
        print(loop)
