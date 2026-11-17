try:
    n1 = int(input("Введите первое число: "))
    c2 = n1 ** 2
    print("Квадрат числа:", c2)
except ValueError:
    print("Введите целое число")