# # def to_dict(lst):
# #     return {element: element for element in lst}

# # print(to_dict([1, 2, 3, 4]))
# # print(to_dict(['grey', (2, 17), 3.11, -4]))

# # my_dict = {'first_one': 'we can do it'}


# # def biggest_dict(**kwargs):
# #     my_dict.update(**kwargs)
    

# # biggest_dict(k1=22, k2=31, k3=11, k4=91)
# # biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
# # print(my_dict)

# # def count_it(sequence):
# #     # При помощи генератора создаем словарь, где ключом выступает уникальный элемент строки, а значением - его частота (вычисляется методом count()) 	
# #     num_frequency = {int(item): sequence.count(item) for item in sequence}

# #     # Сортируем словарь по значениям в порядке возрастания. Для этого методом items() формируем пары “(ключ, значение)” в виде кортежей по всем элементам словаря. Т. к. нужно сортировать по значениям, берем второй элемент кортежей. В результате получим список из кортежей “(ключ, значение)”
# #     sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])

# #     # Возвращаем последние 3 элемента списка, т. е. кортежи с самыми большими значениями второй компоненты, которые преобразовываем в словарь 
# #     return dict(sorted_num_frequency[-3:])

# # # Тесты
# # print(count_it('11222'))
# # print(count_it('133222'))
# # print(count_it('13444455'))



# # def sieve(lst):
# #     unique = []
# #     [unique.append(item) for item in reversed(lst) if item not in unique]
# #     return tuple(unique)


# # # Тесты
# # print(sieve([1, 2, 3, 3, 2]))











# # def del_from_tuple(tpl, elem):
# #     lst = list(tpl)
# #     if elem in tpl:
# #         lst.remove(elem)
# #     return tuple(lst)


# # print(del_from_tuple((1, 2, 3), 1))


# #####9
# # def to_set(element):
# #     st = set(element)
# #     return st, len(st)

# # print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))



# months = {
#         1: 'Январе',
#         2: 'Феврале',
#         3: 'Марте',
#         4: 'Апреле',
#         5: 'Мае',
#         6: 'Июне',
#         7: 'Июле',
#         8: 'Августе',
#         9: 'Сентябре',
#         10: 'Октябре',
#         11: 'Ноябре',
#         12: 'Декабре'
#     }


# def season_events(number_of_month):
#    if not isinstance(number_of_month, int) and 1 <= number_of_month <= 12:
#         print('Требуется ввести реальный номер месяца')
#         return
#    if number_of_month in range(3, 6):
#     print(f'Вы родились в {months[number_of_month]}. Птицы пели прекрасные песни')
#    elif number_of_month in range(6, 9):
#            print(f'Вы родились в {months[number_of_month]}. Солнце светило ярче чем когда-либо')
#    elif number_of_month in range(9, 12):
#      print(f'Вы родились в {months[number_of_month]}. Урожай был невероятным')
#    else:
#         print(f'Вы родились в {months[number_of_month]}. За окном падал белый снег')

# season_events(7)





nick = input()
secret_list = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']

while nick not in secret_list:
    print('Тут ничего нет. Еще есть вопросы?')
    nick = input()
else:
	print(f'Ты – свой. Приветствую, любезный {nick}!')
