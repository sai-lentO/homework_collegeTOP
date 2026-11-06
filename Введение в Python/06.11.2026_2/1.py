a = int(input("Введите начало диапозона: "))
b = int(input("Введите конец диапозона: "))

sum1 = 0
col1 = 0

sum2 = 0
col2 = 0

sum3 = 0
col3 = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        sum1 = sum1 + i
        col1 = col1 + 1
    elif i // 2 == 0:
        sum2 = sum2 + i
        col2 = col2 + 1
    elif i % 9 == 0:
        sum3 = sum3 + i
        col3 = col3 + 1
print("Сумма чётных:", sum1)
if col1 > 0:
    print("Ср. Ариф. чётных:", sum1 / col1)
print("Сумма нечётных:", sum2)
if col2 > 0:
    print("Ср. Ариф. нечётных:", sum2 / col2)
print("Сумма кратных 9:", sum3)
if col3 > 0:
    print("Ср. Ариф. крастных 9:", sum3 / col3)














