n = input("Введите строку: ").lower()

for i in " ,.!?;:":
    n = n.replace(i, "")

if n == n[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")
print(n)