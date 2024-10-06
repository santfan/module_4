# Из модуля fake_math импортирем функцию divide.
# Так как в следующем модуле фнукция нвзывается так же.
# Импортируем функции с разными псевдонимами.
# Из модуля fake_math пседоним div_1
from fake_math import divide as div_1
# Из модуля true_math пседоним div_2
from true_math import divide as div_2

# Вызовим фунцию из модуля fake_math
print(div_1(15, 0))
# Вызовим фунцию из модуля true_math
print(div_2(12, 4))