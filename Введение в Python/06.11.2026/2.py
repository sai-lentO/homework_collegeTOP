numbers = [5, -3, 8, -6, 2, -1, 7, 4]

# 1. Список только чётных чисел

numbers_two = []

for i in numbers:
    if i % 2 == 0:
        numbers_two.append(i)
        
print("Список только чётных чисел:", numbers_two)

# 2. Список только нечётных чисел

numbers_no_two = []

for i in numbers:
    if i % 2 == 1 or i % 2 == -1:
        numbers_no_two.append(i)

print("Список только нечётных чисел:", numbers_no_two)

# 3. Список только положительных чисел

plus_numbers = []

for i in numbers:
    if i > 0:
        plus_numbers.append(i)

print("Список только положительных чисел:", plus_numbers)

# 4. Список только отрицательных чисел

minus_numbers = []

for i in numbers:
    if i < 0:
        minus_numbers.append(i)

print("Список только отрицательных чисел:", minus_numbers)