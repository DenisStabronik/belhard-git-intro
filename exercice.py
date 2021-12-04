a = (1, [2, 3], 4)
print(type(a))   # <type 'tuple'> Кортеж - не изменяемый,не уникальный, индексированный(каждому значению присваивается индекс)
b = {}
print(type(b))   # type 'dict'> Словарь - ключи не изменяемы,значения и элементы изменяемы,не индексируется,элементы 
c = {1, 2, 3}    #и ключи уникальны значения -нет
print(type(c))   #<type 'set'> Множество- изменяемое, неиндексируемое, уникальное
d = {'a' : 1, 'b' : 2} #<type 'dict'>
print(type(d))
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print(my_list)
print(my_dict)
print(len(my_list)) # 6
print(len(my_dict)) # 6 - для словаря пара ключ-значение считаются одним элементом. 
print(len('ab d')) # 4 - для строки элементом является 1 символ длина строки'ab d'
print('*' * 140)
print('a' in my_list)     # находится ли ,буква в списке
print('q' in my_list)
print('a' not in my_list) #  не находится ли буква в списке
print('q' not in my_list)
print('*' * 140)
print('a' in my_dict)               # True - без указания метода поиск по ключам
print('a' in my_dict.keys())        # True - аналогично примеру выше ищет ключь с именем 'a'
print('a' in my_dict.values())      # False - так как 'а' — ключ, не значение 
print(1 in my_dict.values())        # True
print('*' * 140)
print(('a',1) in my_dict.items())   # True проверяем наличие пары ключ - значение
print(('a',2) in my_dict.items())   # False-такой пары нет
print('ab' in 'abc')    # True в строчке "abc" ищем 'ab'
print('*' * 140)
for elm in my_list:
    print(elm)           # Выводит элементы списка по очереди
for elm in my_dict: # При таком обходе словаря, перебираются только ключи
     	print(elm)  # равносильно for elm in my_dict.keys()
for elm in my_dict.values():
    print(elm)
for key, value in my_dict.items():
	# Проход по .items() возвращает кортеж (ключ, значение), 
	# который присваивается кортежу переменных key, value
	print(key, value)

print('*' * 140)

print(min(my_list))               # a
print(sum(my_dict.values()))      # 21
my_list = [1, 2, 2, 2, 2, 3]
print(my_list.count(2))     # 4 экземпляра элемента равного 2
print(my_list.count(5))     # 0 - то есть такого элемента в коллекции нет
print(my_list.index(2))  # первый элемент равный 2 находится по индексу 1 (индексация с нуля!)
print(my_list.index(3))  # ValueError: 5 is not in list - отсутствующий элемент выдаст ошибку!

print('*' * 140)

my_set = {1, 2, 3}
my_set_2 = my_set.copy()
print(my_set_2 == my_set)  # True - коллекции равны - содержат одинаковые значения
print(my_set_2 is my_set)  # False - коллекции не идентичны - это разные объекты с разными id
my_set.clear()
print(my_set)  # set()




