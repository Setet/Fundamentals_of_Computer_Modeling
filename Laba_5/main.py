import numpy as np
from prettytable import PrettyTable


def gen_errors(start):
    return np.random.normal(20, 2) + start


def gen_orders(start):
    return np.random.exponential(1) + start


def errors_one(mass_errors):
    return len(mass_errors) == 1


def orders_one(mass_orders):
    return len(mass_orders) == 1


def get_time_details(start):
    return (np.random.rand() * 0.3 + 0.2) + np.random.normal(0.5, 0.1) + start


def errors_in(start, end, chi):
    return start <= chi <= end


def orders_in(start, end, chi):
    return start <= chi <= end


def get_time_errors(start):
    return (np.random.rand() * 0.4 + 0.1) + start


def main():
    li_detail = (list())
    li_errors = (list())
    li_time = (list())
    li_errors_time = (list())

    for i in range(10):
        time = 0
        order = 0
        detail = 0
        errors = 0
        errors_time = 0
        mass_orders = []
        mass_errors = []
        mass_errors.append(gen_errors(0))
        mass_orders.append(gen_orders(0))
        mass_errors.append(gen_errors(mass_errors[0]))
        mass_orders.append(gen_orders(mass_orders[0]))

        while detail < 500:
            if order == 0:
                if mass_errors[0] > mass_orders[0]:
                    time = mass_orders[0]
                    order += 1
                    if orders_one(mass_orders):
                        mass_orders.append(gen_orders(mass_orders[0]))
                    mass_orders.pop(0)
                else:
                    new_error = get_time_errors(mass_errors[0])
                    if orders_in(time, new_error, mass_orders[0]):
                        while orders_in(time, new_error, mass_orders[0]):
                            if orders_one(mass_orders):
                                mass_orders.append(gen_orders(mass_orders[0]))
                            order += 1
                            mass_orders.pop(0)
                    errors_time = errors_time + (new_error - mass_errors[0])
                    time = new_error
                    mass_errors.pop(0)
                    mass_errors.append(gen_errors(mass_errors[0]))
                    errors += 1

            else:
                new_details = get_time_details(time)
                if orders_in(time, new_details, mass_orders[0]):
                    while orders_in(time, new_details, mass_orders[0]):
                        if orders_one(mass_orders):
                            mass_orders.append(gen_orders(mass_orders[0]))
                        order += 1
                        mass_orders.pop(0)
                if errors_in(time, new_details, mass_errors[0]):
                    new_error = get_time_errors(mass_errors[0])
                    if orders_in(time, new_error, mass_orders[0]):
                        while orders_in(time, new_error, mass_orders[0]):
                            if orders_one(mass_orders):
                                mass_orders.append(gen_orders(mass_orders[0]))
                            order += 1
                            mass_orders.pop(0)
                    errors_time = errors_time + (new_error - mass_errors[0])
                    time = new_error
                    mass_errors.pop(0)
                    mass_errors.append(gen_errors(mass_errors[0]))
                    errors += 1
                else:
                    time = new_details
                    order -= 1
                    detail += 1

        print("Общая информация:\n"
              f"Кол-во деталей = {detail}\n"
              f"Кол-во сбоев = {errors}\n"
              f"Время работы над деталями = {round(time, 4)}\n"
              f"Время потраченное на сбои = {round(errors_time, 4)}")

        li_detail.append(detail)
        li_errors.append(errors)
        li_time.append(time)
        li_errors_time.append(errors_time)

    mytable = PrettyTable()

    mytable.field_names = ["Кол-во деталей", "Кол-во сбоев", "Время работы над деталями", "Время потраченное на сбои"]

    for i in range(10):
        mytable.add_row([li_detail[i], li_errors[i], round(li_time[i], 4), round(li_errors_time[i], 4)])

    print(mytable)


if __name__ == '__main__':
    main()
