from matplotlib import pyplot as plt 
import os
counter = 1
def create_plot(xl, yl, x, y, y1, name):
    plt.xlabel(xl)
    plt.ylabel(yl)
    if y == y1:
        plt.plot(x, y)
        print(xl, yl, x, y, y1, name)
        plt.grid(axis = 'x')
        plt.grid(axis = 'y')
        plt.savefig(f'{name}.png')
    else:
        plt.plot(x, y)
        plt.plot(x, y1)
        plt.grid(axis = 'x')
        plt.grid(axis = 'y')
        plt.savefig(f'{name}.png')
    plt.clf()
while True:
    xl = input('Введите подпись по x')
    yl = input('Введите подпись по y')
    n = int(input('Введите число строк: '))
    co = []
    sp = []
    pr = []
    for j in range(n):
        co.append(int(input("Введите цену: ")))
        sp.append(int(input("Введите объем спроса: ")))
        pr.append(int(input("Введите объем предложения: ")))
    create_plot(xl, yl, co, sp, sp, f'Spros{counter}')
    create_plot(xl, yl, co, pr, pr, f'Pred{counter}')
    create_plot(xl, yl, co, sp, pr, f'Spros_Pred{counter}')
    counter+=1
    if input('Продолжить?\n') == 'НЕТ':
        break