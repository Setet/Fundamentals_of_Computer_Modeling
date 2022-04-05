import matplotlib.pyplot as npt
import numpy as np


def funx_1(x, y):
    return (y)


def funy_1(x, y):
    return (2 * y)


def fun1_1(x):
    return np.exp(2 * x) + 1


def fun2_1(x):
    return 2 * np.exp(2 * x)


def funx_2(x, y):
    return ((-2) * x) + (4 * y)


def funy_2(x, y):
    return (-x) + (3 * y)


def fun1_2(x):
    return 4 * np.exp(-x) - np.exp(2 * x)


def fun2_2(x):
    return np.exp(-x) - np.exp(2 * x)


def main_2():
    a = 0
    b = 2

    h = 0.01

    x = 3
    y = 0

    lix = (list())
    liy = (list())
    lix.append(x)
    liy.append(y)

    for i in np.arange(a, b, h):
        k1 = h * funx_2(x, y)
        l1 = h * funy_2(x, y)

        k2 = h * funx_2(x + k1 / 2, y + l1 / 2)
        l2 = h * funy_2(x + k1 / 2, y + l1 / 2)

        k3 = h * funx_2(x + k2 / 2, y + l2 / 2)
        l3 = h * funy_2(x + k2 / 2, y + l2 / 2)

        k4 = h * funx_2(x + k3, y + l3)
        l4 = h * funy_2(x + k3, y + l3)

        x = x + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y = y + (l1 + 2 * l2 + 2 * l3 + l4) / 6

        lix.append(x)
        liy.append(y)
    print(lix)

    # funx and fun1
    npt.plot(np.arange(a, b + h, h), lix, color='blue')  # приближенное
    npt.plot(np.arange(a, b + h, h), fun1_2(np.arange(a, b + h, h)), '--', color='black')  # точное

    # funy and fun2
    npt.plot(np.arange(a, b + h, h), liy, color='red')  # приближенное
    npt.plot(np.arange(a, b + h, h), fun2_2(np.arange(a, b + h, h)), '--', color='orange')  # точное

    npt.legend(('Приближенное для funx', 'Точное для fun1', 'Приближенное для funy', 'Точное для fun2'))

    npt.show()


def main():
    a = 0
    b = 10
    h = 0.01
    x = 2
    y = 2

    lix = (list())
    liy = (list())
    lix.append(x)
    liy.append(y)

    for i in np.arange(a, b, h):
        k1 = h * funx_1(x, y)
        l1 = h * funy_1(x, y)

        k2 = h * funx_1(x + k1 / 2, y + l1 / 2)
        l2 = h * funy_1(x + k1 / 2, y + l1 / 2)

        k3 = h * funx_1(x + k2 / 2, y + l2 / 2)
        l3 = h * funy_1(x + k2 / 2, y + l2 / 2)

        k4 = h * funx_1(x + k3, y + l3)
        l4 = h * funy_1(x + k3, y + l3)

        x = x + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y = y + (l1 + 2 * l2 + 2 * l3 + l4) / 6

        lix.append(x)
        liy.append(y)

    # funx and fun1
    npt.plot(np.arange(a, b + h, h), lix, color='blue')  # приближенное
    npt.plot(np.arange(a, b + h, h), fun1_1(np.arange(a, b + h, h)), '--', color='black')  # точное

    # funy and fun2
    npt.plot(np.arange(a, b + h, h), liy, color='red')  # приближенное
    npt.plot(np.arange(a, b + h, h), fun2_1(np.arange(a, b + h, h)), '--', color='orange')  # точное

    npt.legend(('Приближенное для funx', 'Точное для fun1', 'Приближенное для funy', 'Точное для fun2'))

    npt.show()

    main_2()


if __name__ == '__main__':
    main()