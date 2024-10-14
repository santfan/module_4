# Список для проверки функций сортировки
nums = [1, 7, 22, 30, 2, 17, 9]

# Функция сортировки пузырьковым методом
def buble_sort(list_):
    # Флаг оптимизации
    flag = True
    while flag:
        flag = False
        for i in range(len(list_) - 1):
            # Условие сортировки в данном случае ПО ВОЗРАСТАНИЮ
             if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                flag = True

# Функци сортировки методом выборки.
# Сортировку сделаем так же по возрастанию
def selection_sort(list_):
    # Считаем что первый взятый элемент самый маленький
    for i in range(len(list_)):
        lower_el = i
        # Проверим оставшийся список
        for j in range(i + 1, len(list_)):
            # Если число с индексом j меньше чем число оставшегося списка
            if list_[j] < list_[lower_el]:
                # Заменим меньшее число
                lower_el = j
        # Поменяем местами
        list_[i], list_[lower_el] = list_[lower_el], list_[i]

# Функция сортировки методом подстановки
def insertion_sort(list_):
    for i in range(1, len(list_)):
        # Установим значение маркера, обзначающий самое большое число
        key = list_[i]
        j = i - 1
        while list_[j] > key and j >= 0:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key


insertion_sort(nums)
print(nums)



