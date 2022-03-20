import math
import numpy as np
import matplotlib.pyplot as plt


def function_1(x, n):
    if x < n:
        return 10 * x / n
    else:
        return 10 * ((x - 20) / (n - 20))


# построение графика + площадь
def Task_1(N, n):
    b = 10
    a = 20
    epsilon = 0.01

    # генерим массив случ точек
    xPoints = np.random.uniform(0, a, N)
    while (xPoints.mean() - a / 2 >= epsilon) or (xPoints.var() - a * a / 12 >= epsilon):
        xPoints = np.random.uniform(0, a, N)

    yPoints = np.random.uniform(0, b, N)
    while (yPoints.mean() - b / 2 >= epsilon) or (yPoints.var() - b * b / 12 >= epsilon):
        yPoints = np.random.uniform(0, b, N)

    # массив x-ов
    x = np.arange(0, 20.1, step=0.5)

    # считаем значений функции
    y = np.array([])
    for i in range(len(x)):
        y = np.append(y, function_1(x[i], n))

    # строим график
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # считаем кол-во точек внутри фигуры
    M = 0
    for i in range(N):
        if yPoints[i] < function_1(xPoints[i], n):
            M += 1
            # Раставляем точки
            plt.scatter(xPoints[i], yPoints[i], s=10, color='black')
        else:
            plt.scatter(xPoints[i], yPoints[i], s=10, color='red')

    # площадь треугольника
    S = round(M / N * a * b, 2)
    print(f"Площадь фигуры: {S}")

    # тоже площадь но точнее
    S1 = 0
    for i in range(N):
        S1 += function_1(xPoints[i], n)
    S1 *= a / N
    S1 = round(S1, 4)
    print(f"Площадь фигуры: {S1}")

    ax.legend(fontsize=12,
              title=f'Всего точек: {N} \n'
                    f'Точек внутри фигуры: {M} \n'
                    f'Площадь: {S} \n'
                    f'Тоже площадь,но точнее: {S1}',
              title_fontsize='12',
              loc="upper right"
              )

    # Размер окна
    fig.set_figwidth(8)
    fig.set_figheight(8)

    # Удалить лишние пробелы
    fig.tight_layout()

    # Границы оси Y
    plt.ylim([0, 15])

    plt.show()


def function_2(x):
    return math.sqrt(11 - 2 * pow(math.sin(x), 2))


# построение графика + площадь
def Task_2(N):
    b = 3.5
    a = 5
    e = 0.01

    # генерим массив случ точек
    xPoints = np.random.uniform(0, a, N)
    while (xPoints.mean() - a / 2 >= e) or (xPoints.var() - a * a / 12 >= e):
        xPoints = np.random.uniform(0, a, N)

    yPoints = np.random.uniform(0, b, N)
    while (yPoints.mean() - b / 2 >= e) or (yPoints.var() - b * b / 12 >= e):
        yPoints = np.random.uniform(0, b, N)

    # массив x-ов
    x = np.arange(0, 5, step=0.125)

    # считаем значений функции
    y = np.array([])
    for i in range(len(x)):
        y = np.append(y, function_2(x[i]))

    # строим график
    fig, ax = plt.subplots()
    ax.plot(x, y)

    M = 0
    for i in range(N):
        if yPoints[i] < function_2(xPoints[i]):
            M += 1
            plt.scatter(xPoints[i], yPoints[i], s=10, color='red')
        else:
            plt.scatter(xPoints[i], yPoints[i], s=10, color='black')

    S = round(M / N * a * b, 2)
    print(f"Интеграл равен: {S}")

    S1 = 0
    for i in range(N):
        S1 += function_2(xPoints[i])
    S1 *= a / N
    S1 = round(S1, 4)
    print(f"Интеграл равен: {S1}")

    ax.legend(fontsize=12,
              title=f'Всего точек: {N} \n'
                    f'Точек под интеграллом: {M} \n'
                    f'Площадь: {S} \n'
                    f'Тоже площадь,но точнее: {S1}',
              title_fontsize='12',
              loc="upper right"
              )

    # Размер окна
    fig.set_figwidth(8)
    fig.set_figheight(8)

    fig.tight_layout()

    plt.ylim([0, 10])

    plt.show()


# вычисленние значение pi
def Task_3(N, R):
    zPoints = np.random.uniform(0, 2 * R, 2 * N)

    xPoints = np.array([])

    for i in range(0, N):
        xPoints = np.append(xPoints, zPoints[i])

    yPoints = np.array([])

    for i in range(N, 2 * N):
        yPoints = np.append(yPoints, zPoints[i])

    M = 0

    for i in range(0, N):
        if ((pow((xPoints[i] - R), 2) + pow((yPoints[i] - R), 2)) < R * R):
            M += 1

    S = (M / N) * pow((2 * R), 2)
    pi = S / (R * R)

    show(N, R, xPoints, yPoints, pi)


# отрисовка Task_3
def show(N, R, xPoints, yPoints, pi):
    fig, ax = plt.subplots()

    x = np.linspace(0, 2 * np.pi, num=150)

    # Вычисление точек круга заданных параметрических
    xG = np.array([])
    yG = np.array([])

    for i in range(len(x)):
        xG = np.append(xG, R + R * np.cos(x[i]))
        yG = np.append(yG, R + R * np.sin(x[i]))

    ax.plot(xG, yG)

    M = 0
    for i in range(0, N):
        if ((pow((xPoints[i] - R), 2) + pow((yPoints[i] - R), 2)) < R * R):
            M += 1
            plt.scatter(xPoints[i], yPoints[i], s=10, color="black")
        else:
            plt.scatter(xPoints[i], yPoints[i], s=10, color="red")

    ax.legend(fontsize=12,
              title=f'Всего точек: {N} \n'
                    f'Точек внутри фигуры: {M} \n'
                    f'Приближённо значение pi: {pi}',
              title_fontsize='12',
              loc="upper right"
              )

    fig.tight_layout()

    plt.ylim([0, R * 2])
    plt.xlim([0, R * 2])

    plt.show()


# функция в полярных координатах
def polar(x):
    return np.sqrt(14 * pow(np.cos(x), 2) + 8 * pow(np.sin(x), 2))


# f_i
def ff(x, y):
    if (x > 0):
        return math.atan(y / x)
    elif (x < 0):
        return math.atan(y / x) + math.pi
    elif (y > 0):
        return math.pi / 2
    else:
        return math.pi * 3 / 2


# r_i
def pp(x, y):
    return math.sqrt((x * x) + (y * y))


def Task_4(N):
    fig, ax = plt.subplots()

    x = np.linspace(0, 2 * np.pi, num=300)

    # вычисляю точки
    xG = np.array([])
    yG = np.array([])

    for i in range(len(x)):
        xG = np.append(xG, polar(x) * np.cos(x))
        yG = np.append(yG, polar(x) * np.sin(x))

    ax.plot(xG, yG)

    fig.tight_layout()

    a = 4
    b = 4

    xPoints = np.random.uniform(0, 2 * a, N) - a
    yPoints = np.random.uniform(0, 2 * b, N) - b

    M = 0

    for i in range(0, N):
        if (pp(xPoints[i], yPoints[i]) < polar(ff(xPoints[i], yPoints[i]))):
            plt.scatter(xPoints[i], yPoints[i], s=10, color="black")
            M += 1
        else:
            plt.scatter(xPoints[i], yPoints[i], s=10, color="red")

    S = M / N * (a * b * 4)

    ax.legend(fontsize=12,
              title=f'Всего точек: {N} \n'
                    f'Точек внутри фигуры: {M} \n'
                    f'Приближённая площадь фигуры: {S}',
              title_fontsize='12',
              loc="upper right"
              )

    plt.show()


def main():
    N = int(input("Количество случайных точек \n:>"))
    print("Количество случайных точек N = " + str(N))

    point = input("Какое задание?\n"
                  "1. Задание 1\n"
                  "2. Задание 2\n"
                  "3. Задание 3\n"
                  "4. Задание 4\n:>")

    if point == "1":
        n = 3
        print("Середина интервала n = " + str(n))
        Task_1(N, n)
    elif point == "2":
        Task_2(N)
    elif point == "3":
        R = int(input("Радиус \n:>"))
        Task_3(N, R)
    elif point == "4":
        Task_4(N)
    else:
        main()


if __name__ == '__main__':
    main()
