from funcs_sort import buble_sort, selection_sort, insertion_sort

data_1 = [9, 7, 4, 5, 6, 7, 1, 2]
data_2 = [9, 7, 4, 5, 6, 7, 1, 2, 10, 1]
data_3 = [9, 7, 4, 5, 6, 7, 1, 2, 1, 2, 3]

insertion_sort(data_1)
print(data_1)
insertion_sort(data_2)
print(data_2)
insertion_sort(data_3)
print(data_3)

buble_sort(data_1)
print(data_1)
buble_sort(data_2)
print(data_2)
buble_sort(data_3)
print(data_3)

selection_sort(data_1)
print(data_1)
selection_sort(data_2)
print(data_2)
selection_sort(data_3)
print(data_3)
