# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

def operation():
    numb1 = int(input("Введите первое число"))
    numb2 = int(input("Введите второе число "))
    a = input("Введите знак операции ")
    if a == 0:
        return print("Завершение программы")
    if a != "0" and a != "+" and a != "-" and a != "*" and a != "/":
        print("Ошибка")
        a = input("Введите знак операции ")
    if numb2 == 0:
        print("Деление на 0")
        numb2 = int(input("Введите второе число "))
    if a == "+":
        print(numb1 + numb2)
    elif a == "/":
        print(numb1 + numb2)
    elif a == "-":
        print(numb1 + numb2)
    elif a == "*":
        print(numb1 + numb2)
    return operation()

operation()

# 2

a = int(input("Введите число "))
even = 0
odd = 0

while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a = a // 10

print("Even: %d, odd: %d" % (even, odd))

# 3

t = int(input("Введите число "))
g = 0
while t > 0:
    g = g * 10 + t % 10
    t = t // 10
print(g)

# 4

e = int(input("Введите количество элементов ряда: "))
u = 1
i = 0
summ = 0
while i < e:
    summ += u
    u = u / -2
    i += 1

print(summ)

# 5

for i in range(32, 128):
    print("%4d-%s" % (i, chr(i)), end='')
    if i % 10 == 0:
        print()

print()

# 6

from random import random
n = round(random() * 100)
i = 1
print("Компьютером было загадано число. Отгадайте его. У вас 10 попыток")
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Слишком много')
    elif u < n:
        print('Мало')
    else:
        print('Число угадано с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы превысили чило попыток. Было загадано число ', n)

# 7

n = int(input("Введите число "))
s = 0
for i in range(1, n+1):
    s += i
m = n * (n + 1) // 2
print(s)
print(m)

# 8
n = int(input("Сколько будет чисел? "))
d = int(input("Какую цифру считать? "))
count = 0
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print("Было введено %d цифр %d" % (count, d))

# 9
n = int(input())
max_s = 0
max_m = 0
while n != 0:
    m = n
    s = 0
    while n>0:
        s += n%10
        n //= 10
    if s > max_s:
        max_s = s
        max_m = m
    n = int(input())
print('Число',max_m,'имеет максимальную сумму цифр:', max_s)