
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.


from itertools import count
from itertools import cycle


def number_generator(start_number, step, stop_value):
    """ Итератор, генерирующий целые числа, начиная с указанного:
    параметр 1 - start_number -  начальное значение генератора
    параметр 2 - step - шаг
    параметр 3 - stop_value - когда закончить генерацию
     """
    result = []
    for el in count(start_number, step):
        if el > stop_value:
            print(result)
            break
        else:
            result.append(el)
            print(el)


print('------------------------- Вывод результата первой части -------------------------\n')
number_generator(3, 7, 300)


def repeating_list(repeat_list, enough):
    """ Итератор, генерирующий целые числа, начиная с указанного:
    параметр 1 - repeat_list - повторяемый список
    параметр 2 - enough - когда остановиться, через сколько итераций
     """
    i = 0
    iteration = cycle(repeat_list)
    while i < enough:
        print(next(iteration))
        i += 1


print('\n------------------------- Вывод результата второй части -------------------------\n')
repeating_list([1, 2, 3, 4], 17)
