try:
    n1 = int(input("Введите первое число: "))
    n2 = int(input("Введите второе число: "))
    delenie = n1 / n2
    print(delenie)
except ValueError:
    print("Ввести нужно два целых числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")