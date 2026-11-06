numbers = [5, -3, 8, -6, 2, -1, 7, 4]


# 1. Сумма отрицательных чисел

sum_negative = 0

for i in numbers:
    if i < 0:
        sum_negative = sum_negative + i

print("Сумма отрицательных чисел:", sum_negative)


# 2. Сумма чётных чисел

sum_two = 0

for i in numbers:
    if i % 2 == 0:
        sum_two = sum_two + i

print("Сумма чётных чисел:", sum_two)


# 3. Сумма нечётных чисел

sum_no_two = 0

for i in numbers:
    if i % 2 == 1 or i % 2 == -1:
        sum_no_two = sum_no_two + i

print("Сумма нечётных чисел:", sum_no_two)


# 4. Произведение элементов с индексами, кратными 3

i_three = 1

for i in range(len(numbers)):
    if i % 3 == 0:
        i_three = i_three * numbers[i]

print("Произведение элементов с индексами, кратными 3:", i_three)