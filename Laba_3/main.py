import matplotlib.pyplot as npt


# метод квадратов
def Square(x, n):
    li = list()
    for i in range(n):
        x = pow(x, 2)
        x = x // 100
        x = x % 10000
        li.append(x / 10000)
    return li


# метод произведений
def OP(x, y, n):
    li = list()

    for i in range(n):
        ymn = x * y
        y = ymn % 10000
        sl = (ymn // 100) % 10000
        li.append(sl / 10000)
    return li


# мультипликативный конгруэнтный метод
def Multiplicative(x, l, m, n):
    li = list()
    x1 = x
    for i in range(n):
        x = (x1 * l) % m
        x1 = x
        li.append(x1 / 10000)

    return li


#  методы, представляющие модификации перечисленных методов
def Mix(x, l, u, m, n):
    li = list()
    x1 = x
    for i in range(n):
        x = ((x1 * l) + u) % m
        x1 = x
        li.append(x1 / m)
    return li


def main():
    menu = input("Какое задание?\n"
                 "1. Метод квадратов\n"
                 "2. Метод произведений\n"
                 "3. Мультипликативный конгруэнтный метод\n"
                 "4. Методы, представляющие модификации перечисленных методов\n:>")

    point = int(input("Количество случайных точек\n:>"))

    if menu == "1":
        # (ядро,кол во случайных чисел)
        p1 = (Square(7153, point))
        npt.bar(range(point), p1)
        npt.suptitle(u'Метод квадратов')
        npt.ylabel('Случайное число')
        npt.xlabel('Кол-во раз которое оно встретилось')
        npt.show()
        main()
    elif menu == "2":
        p2 = (OP(5167, 3729, point))
        npt.bar(range(point), p2)
        npt.suptitle(u'Метод произведений')
        npt.ylabel('Случайное число')
        npt.xlabel('Кол-во раз которое оно встретилось')
        npt.show()
        main()
    elif menu == "3":
        p3 = (Multiplicative(1357, 1357, 5689, point))
        npt.bar(range(point), p3)
        npt.suptitle(u'Мультипликативный конгруэнтный метод')
        npt.ylabel('Случайное число')
        npt.xlabel('Кол-во раз которое оно встретилось')
        npt.show()
        main()
    elif menu == "4":
        p4 = (Mix(1357, 1357, 3459, 1113, point))
        npt.bar(range(point), p4)
        npt.suptitle(u'Методы, представляющие модификации перечисленных методов')
        npt.ylabel('Случайное число')
        npt.xlabel('Кол-во раз которое оно встретилось')
        npt.show()
        main()
    else:
        main()


if __name__ == '__main__':
    main()
