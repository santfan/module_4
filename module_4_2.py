# Создадаим функцию test_function
def test_function():
  # Внутри функции создадим другую функцию inner_function
  def inner_function():
    # Пока у этой функции нет никаких других задач кроме как вывод сообщения
    print('Я внутри функции inner_function')

# теперь попробуем вызвать функцию inner_function находясь в функции test_function
def test_function():
  def inner_function():
    print('Я внутри функции inner_function')
  # Вызов функции inner_function
  inner_function()

test_function()

# Получим вывод сформированной функцией inner_function
# Теперь попробуем вызвать функцию inner_function из глобального пространства имен
inner_function()

# Получим сообщение об ошибке. Так как функция inner_function находится
# Внутри локального пространства имен функции test_function