#Функция с параметрами по умолчанию:
#Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по
# умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a = 1, b = 'строка', c = True):
    # Функция должна выводить эти параметры.
    print(f'Параметр a = {a}, параметр b = {b}, параметр с = {c}')


print('Вызов без аругментов:')
#Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()
#Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print('Вызов print_params(b = 25):')
print_params(b = 25)
print('Вызов print_params(c = [1,2,3]:')
print_params(c = [1,2,3])
#2.Распаковка параметров:
#Создайте список values_list с тремя элементами разных типов.
values_list = ['строка', 2, False]
#Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = {'a' : 2, 'b' : 'Проверка', 'c' : False}
#Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print('Вызов print_params(*values_list):')
print_params(*values_list)
#Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print('Вызов print_params(**values_dict):')
print_params(**values_dict)
#3.Распаковка + отдельные параметры:
#Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [54.32, 'Строка' ]
#Проверьте, работает ли print_params(*values_list_2, 42)
print('Вызов print_params(*values_list_2, 42):')
print_params(*values_list_2, 42)