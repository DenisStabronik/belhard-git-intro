# Получение значения по индексу
my_str = "abcde"
print(my_str[0]) 		# a - первый элемент
print(my_str[-1])		# e - последний элемент 
print(my_str[len(my_str)-1]) 	# e - так тоже можно взять последний элемент
print(my_str[-2]) 		# d - предпоследний элемент

print('*'*140)

my_2lvl_list = [[1, 2, 3], ['a', 'b', 'c']]
print(my_2lvl_list[0])      # [1, 2, 3] - первый элемент — первый вложенный список
print(my_2lvl_list[0][0])   # 1 — первый элемент первого вложенного списка
print(my_2lvl_list[1][-1])  # с — последний элемент второго вложенного списка

print('*'*140)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])	  # 1
#my_tuple[0] = 100         # TypeError: 'tuple' object does not support item assignment пытаемся изменить 0 
#но он не изменяемый А вот для списка, если взятие элемента по индексу располагается в левой части выражения,
#  а далее идёт оператор присваивания =, то мы задаём новое значение элементу с этим индексом.
my_list = [1, 2, 3, [4, 5]]
my_list[0] = 10
my_list[-1][0] = 40
print(my_list)      	# [10, 2, 3, [40, 5]]
#При срезе, первый индекс входит в выборку, а второй нет
#[ <первый включаемый> : <первый НЕ включаемый> : <шаг> ]
person = ('Alex', 'Smith', "May", 10, 1980)
NAME, BIRTHDAY = slice(None, 2), slice(2, None)     # нон - значение по умолчанию и равносильно записи [:2]
	# задаем константам именованные срезы
        # данные константы в квадратных скобках заменятся соответствующими срезами
print(person[NAME])      # ('Alex', 'Smith')
print(person[BIRTHDAY])  # ('May', 10, 1980)
my_list = [1, 2, 3, 4, 5, 6, 7]
EVEN = slice(1, None, 2)
print(my_list[EVEN])     # [2, 4, 6]
#Изменение списка срезом
my_list = [1, 2, 3, 4, 5]
# my_list[1:2] = 20     # TypeError: can only assign an iterable
my_list[1:2] = [20]     # Вот теперь все работает (значению2 по индексу 1 значение 20)
print(my_list)          # [1, 20, 3, 4, 5]
print('*'*140)
my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [20, 30]
print(my_list)          # [1, 20, 30, 4, 5]
my_list[1:3] = [0]      # нет проблем заменить два элемента на один
print(my_list)          # [1, 0, 4, 5]
my_list[2:] = [40, 50, 60]   # или два элемента на три
print(my_list)               # [1, 0, 40, 50, 60]
my_list[:2] = []    # или del my_list[:2]
print(my_list)      # [40, 50, 60]
my_list = [1, 2, 3, 4, 5]
print(my_list[0:10])      # [1, 2, 3, 4, 5] — отработали в пределах коллекции
print(my_list[10:100])	  # [] - таких элементов нет — вернули пустую коллекцию
print(my_list[10:11])     # [] - проверяем 1 отсутствующий элемент - пустая коллекция, без ошибки

my_files = ['somecat.jpg', 'pc.png', 'apple.bmp', 'mydog.gif']
my_files_sorted = sorted(my_files, key=len)
print(my_files_sorted)      # ['pc.png', 'apple.bmp', 'mydog.gif', 'somecat.jpg']
print('*'*140)
my_dict = {'a': 1, 'c': 3, 'e': 5, 'f': 6, 'b': 2, 'd': 4}
mysorted = sorted(my_dict)
print(mysorted)           # ['a', 'b', 'c', 'd', 'e', 'f']
mysorted = sorted(my_dict.items())
print(mysorted)           # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]
mysorted = sorted(my_dict.values())
print(mysorted)           # [1, 2, 3, 4, 5, 6]
print('*'*140)
population = {"Shanghai": 24256800, "Karachi": 23500000, "Beijing": 21516000, "Delhi": 16787941}
# отсортируем по возрастанию населения:
population_sorted = sorted(population.items(), key=lambda x: x[1]) #лямбда берет для сортировки значение x[по индексу 1]
# что дает нам сортировку по численности населения.population.items() означает (пары) словаря
print(population_sorted)
# [('Delhi', 16787941), ('Beijing', 21516000), ('Karachi', 23500000), ('Shanghai', 24256800)] Сортед для словаря !!!!!!!

print('*'*140)

shop = [('каретка', 1200), ('шатун', 1000), ('седло', 300),
        ('педаль', 100), ('седло', 1500), ('рама', 12000),
        ('обод', 2000), ('шатун', 200), ('седло', 2700)]
shop.sort(key=lambda x: (x[0], -x[1]))
for det, price in shop:
    print('{:<10} цена: {:>5}р.'.format(det, price))
l = [1, 2, 3, 4]  # List
print(l.pop(0))          # -> 1 | O(n)
print(l.pop())           # -> 4 | O(1)

