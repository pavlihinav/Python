##Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
##*Пример:* 2 2 = 4

def sum(A, B):
    if (B==0):
        return A
    else:
        return sum(A+1,B-1)

a = int(input('Введите a:'))
print()
b = int(input('Введите b:'))
print()
if (a>=b):
    print (sum(a,b))
else:
    print(sum(b,a))
