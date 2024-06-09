#!/bin/python3
from math import sqrt

def main():
    continue_flag = True
    while(continue_flag == True):
        try:
            a, b, c = map(int, input('Enter a, b, c divided by space: ').split(' '))
            print(f'Root(-s): {solve(a, b, c)}')
            temp = input('Continue? ')
            if temp.lower()[0] != 'y':
                continue_flag = False
        except:
            pass
    return

# для визуального удобства явно прописываю альтернативные условия вместо простого else
def solve(a, b, c) -> tuple:
    if a == 0:
        if b == 0:
            if c == 0:
                return ('∞')
            elif c != 0: 
                return ('∅')
        elif b != 0:
            return (-c / b)
    elif a != 0:
        d = b**2 - 4 * a * c
        if d < 0:
            return ('∅')
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (min(x1, x2), max(x1, x2))
    return ('error')

if __name__ == '__main__':
    main()