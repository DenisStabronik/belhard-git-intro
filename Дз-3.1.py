s1 = input()
s2 = input()
print(f'Вы ввели строку {s1} и {s2}')
print(f'Их длина соответственно {len(s1)} и {len(s2)}')
print(f'Первый символ первой строки {s1[0]}')
print(f'Последний символ последней строки {s2[-1]}')
print(f'"s1" равен "s2"? {s1 == s2}')
print(f'"s1" содержится ли в "s2"? {s1 in s2}')
print(f'А наоборот? {s2 in s1}')