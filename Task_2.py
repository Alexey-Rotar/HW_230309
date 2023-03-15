result = 0
n = int(input("Введите число: "))
while n > 0:
    result = result + n % 10
    n //= 10
print(f"Сумма цифр в числе: {result}")