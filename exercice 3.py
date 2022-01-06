str1 = 'abc'
str2 = 'de'
str3 = str1 + str2
print(str3)         # abcde

tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple3 = tuple1 + tuple2
print(tuple3)       # (1, 2, 3, 4, 5)
 
a = [1, 2, 3]
b = [4, 5]
c = a + b           
print(a, b, c)      # [1, 2, 3]  [4, 5]  [1, 2, 3, 4, 5]

a = [1, 2, 3]
b = [4, 5]
c = a + [b]
print(a, b, c)     # [1, 2, 3]  [4, 5]  [1, 2, 3, [4, 5]]

a = [1, 2, 3]
b = [4, 5]
c = [*a, *b]  # работает на версии питона 3.5 и выше
print(c)      # [1, 2, 3, 4, 5]

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
#dict3 = dict1.copy() # копируем словарь 1 в словарь 3
#dict3 = {}
dict1.update(dict2)  # обновляем словарть 3 словарем 2
print(dict1)        	# {'a': 1, 'c': 3, 'b': 2, 'd': 4}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {**dict1, **dict2}
print(dict3)        	# {'a': 1, 'c': 3, 'b': 2, 'd': 4}
#Объединение (union):
a = {'a', 'b'}
b = {    'b', 'c'}	# отступ перед b для наглядности
c = a.union(b)     # c = b.union(a) даст такой же результат	
# c = a + b        # Обычное объединение оператором + не работает
		   # TypeError: unsupported operand type(s) for +: 'set' and 'set'
c = a | b          # Альтернативная форма записи объединения
print(c)	   # {'a', 'c', 'b'}

#Пересечение (intersection)
a = {'a', 'b'}
b = {    'b', 'c'}	# отступ перед b для наглядности
c = a.intersection(b)    # c = b.intersection(a) даст такой же результат
c = a & b                # Альтернативная форма записи пересечения
print(c)                 # {'b'}

a = {'a', 'b'}
b = {     'b', 'c'}
c = {    'b', 'd'}
d = a.intersection(b, c)	# Первый вариант записи
d = set.intersection(a, b, c)   # Второй вариант записи (более наглядный)
print(d)                        # {'b'}

#Разница (difference)
a = {'a', 'b'}
b = {    'b', 'c'}
c = a.difference(b)      # c = a - b другой способ записи дающий тот же результат
print(c)                 # {'a'}
c = b.difference(a)      # c = b - a другой способ записи дающий тот же результат
print(c)                 # {'c'}

#Симметричная разница (symmetric_difference) Это своего рода операция противоположная пересечению 
#— выбирает элементы из обеих множеств которые не пересекаются, то есть все кроме совпадающих:
a = {'a', 'b'}
b = {    'b', 'c'}
c = b.symmetric_difference(a)   
# c = a.symmetric_difference(b)       # даст такой же результат
c = b ^ a                             # Альтернативная форма записи симметричной разницы
print(c)        		      # {'a', 'c'}



list_a = [-2, -1, 0, 1, 2, 3, 4, 5]    # Пусть у нас есть исходный список
list_b = [x for x in list_a]           # Создадим новый список используя генератор списка
print(list_b)                          # [-2, -1, 0, 1, 2, 3, 4, 5]
print(list_a is list_b)                # False - это разные объекты!

# if x % 2 == 0 - остаток от деления на 2 равен нулю - число четное
list_a = [-2, -1, 0, 1, 2, 3, 4, 5] 
list_b = [x for x in list_a if x % 2 == 0]
print(list_b)   # [-2, 0, 2, 4]

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x for x in list_a if x % 2 == 0 and x > 0]
# берем те x, которые одновременно четные и больше нуля
print(list_b)   # [2, 4]

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x**2 for x in list_a]
print(list_b)   # [4, 1, 0, 1, 4, 9, 16, 25]

list_a = ['a', 'abc', 'abcde']
list_b = [len(x) for x in list_a]
print(list_b)   # [1, 3, 5]

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x if x < 0 else x**2 for x in list_a]
# Если x-отрицательное - берем x, в остальных случаях - берем квадрат x
print(list_b)   # [-2, -1, 0, 1, 4, 9, 16, 25]

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x**3 if x < 0 else x**2 for x in list_a if x % 2 == 0]
# вначале фильтр пропускает в выражение только четные значения
# после этого ветвление в выражении для отрицательных возводит в куб, а для остальных в квадрат
print(list_b)   # [-8, 0, 4, 16]

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = []
for x in list_a:
    if x % 2 == 0:
        if x < 0:
            list_b.append(x ** 3)
        else:
            list_b.append(x ** 2)
print(list_b)   # [-8, 0, 4, 16]


numbers = range(10)

# Before
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]

print(squared_evens)




list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
# используем генератор прямо в .join() одновременно приводя элементы к строковому типу
my_str = ''.join(str(x) for x in list_a)
print(my_str)  # -2-1012345



list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_e = [x for i, x in enumerate(list_a,1) if i % 3 == 0] # list_a, 1 значит что он считает с 1 индекса,
print(list_e)   # [0, 3]

from collections import namedtuple

Features = namedtuple('Features', ['age', 'gender', 'name'])
row = Features(age=22, gender='male', name='Alex')
print(row.gender)