#!/usr/bin/python3

def whileloop(limitador):
    soma = [0, 1]
    while soma[-1] < limitador:
        soma.append(soma[-2] + soma[-1])
    return soma


if __name__ == '__main__':
    for loop in whileloop(100):
        print(loop)
