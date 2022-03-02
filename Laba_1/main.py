import math
import matplotlib.pyplot as plt

global yg
yg = []


def Linear(Xi, Yi, n):
    SumX = 0
    SumY = 0
    SumX2 = 0
    SumXY = 0

    for i in range(n):
        SumX += Xi[i]
        SumX2 += Xi[i] * Xi[i]
        SumY += Yi[i]
        SumXY += Xi[i] * Yi[i]

    delta = SumX2 * n - SumX * SumX

    if delta != 0:
        deltaA = round(SumXY * n - SumY * SumX, 4)
        deltaB = round(SumX2 * SumY - SumX * SumXY, 4)

        a = round(deltaA / delta, 2)
        b = round(deltaB / delta, 2)

        global e1
        e1 = 0
        for i in range(n):
            e1 += (Yi[i] - (a * Xi[i] + b)) ** 2

        print(
            'Линейная функция: y = ' + str(a) + 'x' + ' + ' + str(b) + '\tS(a,b): {0}'.format(round(e1, 2)))
        yg.append(round(e1, 2))
        global yg1
        yg1 = []
        for elem in Xi:
            yg1.append(a * elem + b)


def Sedate(Xi, Yi, n):
    lnx = 0
    lnx2 = 0
    lny = 0
    ylnx = 0

    for i in range(n):
        lnx += math.log(Xi[i])
        lnx2 += math.log(Xi[i]) * math.log(Xi[i])
        lny += math.log(Yi[i])
        ylnx += math.log(Yi[i]) * math.log(Xi[i])

    lnx = round(lnx, 4)
    lnx2 = round(lnx2, 4)
    lny = round(lny, 4)
    ylnx = round(ylnx, 4)

    delta = n * lnx2 - (lnx * lnx)

    if delta != 0:
        deltaA = (lny * lnx2) - (ylnx * lnx)
        deltaB = (n * ylnx) - (lny * lnx)

        lna = round(deltaA / delta, 4)
        a = round(math.exp(lna), 2)
        b = round(deltaB / delta, 2)

        global e2
        e2 = 0
        for i in range(n):
            e2 += (Yi[i] - (a * (Xi[i] ** b))) ** 2

        print('Степенная функция: y = ' + str(a) + ' * x^' + str(b) + '\tS(a,b): {0}'.format(round(e2, 2)))
        yg.append(round(e2, 2))
        global yg2
        yg2 = []
        for elem in Xi:
            yg2.append(a * (elem ** b))


def Demonstration(Xi, Yi, n):
    lny = 0
    x2 = 0
    xlny = 0
    x = 0

    for i in range(n):
        lny += math.log(Yi[i])
        x += Xi[i]
        x2 += Xi[i] * Xi[i]
        xlny += math.log(Yi[i]) * Xi[i]

    lny = round(lny, 4)
    x2 = round(x2, 4)
    x = round(x, 4)
    xlny = round(xlny, 4)

    delta = n * x2 - (x * x)

    if delta != 0:
        deltaA = (lny * x2) - (xlny * x)
        deltaB = (n * xlny) - (lny * x)

        lna = round(deltaA / delta, 4)
        a = round(math.exp(lna), 2)
        b = round(deltaB / delta, 2)

        global e3
        e3 = 0
        for i in range(n):
            e3 += (Yi[i] - (a * math.exp(Xi[i] * b))) ** 2

        print('Показательная функция: y = ' + str(a) + ' * e3^(' + str(b) + ' * x)\tS(a,b): {0}'.format(round(e3, 2)))
        yg.append(round(e3, 2))
        global yg3
        yg3 = []
        for elem in Xi:
            yg3.append(a * math.exp(elem * b))

    else:
        print('Система имеет больше одного решения!!!')


def Quadratic(Xi, Yi, n):
    x4 = 0
    x3 = 0
    x2 = 0
    x = 0
    x2y = 0
    xy = 0
    y = 0

    for i in range(n):
        x4 += round(Xi[i] ** 4, 4)
        x3 += round(Xi[i] ** 3, 4)
        x2 += round(Xi[i] ** 2, 4)
        x += round(Xi[i], 4)
        x2y += round((Xi[i] ** 2) * Yi[i], 4)
        xy += round(Xi[i] * Yi[i], 4)
        y += round(Yi[i], 4)

    delta = x4 * x2 * n + x3 * x * x2 + x3 * x * x2 - x2 * x2 * x2 - x * x * x4 - x3 * x3 * n

    if delta != 0:
        deltaA = x2y * x2 * n + x3 * x * y + xy * x * x2 - y * x2 * x2 - x * x * x2y - xy * x3 * n
        deltaB = x4 * xy * n + x2y * x * x2 + x3 * y * x2 - x2 * xy * x2 - y * x * x4 - x3 * x2y * n
        deltaC = x4 * x2 * y + x3 * x * x2y + x3 * xy * x2 - x2 * x2 * x2y - x * xy * x4 - x3 * x3 * y

        a = round(deltaA / delta, 2)
        b = round(deltaB / delta, 2)
        c = round(deltaC / delta, 2)

        global e4
        e4 = 0
        for i in range(n):
            e4 += (Yi[i] - (a * (Xi[i] ** 2) + b * Xi[i] + c)) ** 2

        print('Квадратичная функция: y = {0}*x^2 + {1}*x + {2}*c\tS(a,b): {3}'.format(a, b, c, round(e4, 2)))
        yg.append(round(e4, 2))
        global yg4
        yg4 = []
        for elem in Xi:
            yg4.append(a * (elem ** 2) + b * elem + c)


def main():
    point = input("Какие взять точки?\n"
                  "1. Из контрольного примера\n"
                  "2. Вариант 3\n:>")

    if point == "1":
        x = "1,2,3,4,5,6"
        y = "1.0,1.5,3.0,4.5,7.0,8.5"
    elif point == "2":
        x = "3,5,7,9,11,13"
        y = "26,76,150,240,360,500"

    Yi = y.split(',')
    Xi = x.split(',')

    for i in range(len(Xi)):
        Xi[i] = float(Xi[i])
    for i in range(len(Yi)):
        Yi[i] = float(Yi[i])

    n = len(Xi)

    Linear(Xi, Yi, n)
    Sedate(Xi, Yi, n)
    Demonstration(Xi, Yi, n)
    Quadratic(Xi, Yi, n)

    de = min(yg)

    if de == round(e1, 2):
        print(" Лучшая Аппроксимирующая функция = Линейная функция")
    elif de == round(e2, 2):
        print(" Лучшая Аппроксимирующая функция = Степенная функция")
    elif de == round(e3, 2):
        print(" Лучшая Аппроксимирующая функция = Показательная функция")
    elif de == round(e4, 2):
        print(" Лучшая Аппроксимирующая функция = Квадратичная функция")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(Xi, Yi, color='black', linestyle=' ', marker='o', label='Эксперементальные данные')
    plt.plot(Xi, yg1, color='red', label="Линейная функция")
    plt.plot(Xi, yg2, label="Степенная функция")
    plt.plot(Xi, yg3, color='green', label="Показательная функция")
    plt.plot(Xi, yg4, color='pink', label="Квадратичная функция")
    plt.legend()
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
