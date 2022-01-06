#import math
#a = int(input())
#b = int(input())
#S = a*b/2
#c = math.sqrt(a**2 + b**2)
#print(f'Треугольник 1 с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}')
import math
a = input()
b = input()
a = [int(i) for i in a.split()]
b = [int(i) for i in b.split()]
for index in range(0,len(a)):
    S = a[index] * b[index] / 2
    c = math.sqrt(a[index]**2 + b[index]**2)
    
    print(f'Треугольник {index+1} с катетами {a[index]} и {b[index]} имеет площадь {S} и гипотенузу {c}')
    
#sides = [(a[index], b[index]) for index in range(len(a))]
#S = a*b/2
#c = math.sqrt(a**2 + b**2)
#for element in input().split():
#a.append(input('введите значение 1-го катета в формате a1, a2, a3... '))
#b.append(input('введите значение 2-го катета в формате b1, b2, b3... '))
#array = zip(a, b)
#print(list(array))
