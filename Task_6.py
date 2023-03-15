leftSum = 0
rightSum = 0
i = 6
n = int(input("Введите шестизначный номер билета: "))
while i > 0:
    if (i > 3):
        rightSum = rightSum + n % 10
    if (i <= 3):
        leftSum = leftSum + n % 10
    n //= 10
    i-=1
if (leftSum == rightSum):
    print("Билет счастливый!")
else:
    print("Билет не счастливый :(")