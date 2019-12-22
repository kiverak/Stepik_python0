a = int(input())

num1 = int(a / 1000)
num2 = int(a % 1000)

sum1 = int(num1 % 10) + int(num1 % 100 / 10) + int(num1 / 100)
sum2 = int(num2 % 10) + int(num2 % 100 / 10) + int(num2 / 100)

if sum1 == sum2:
    print("Счастливый")

if sum1 != sum2:
    print("Обычный")