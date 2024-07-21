#Вам необходимо написать 3 функции:

#Функция count_calls подсчитывающая вызовы остальных функций.
#Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
def count_calls():
    global calls
    calls += 1
    return calls

#Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре.
#Создать функцию string_info с параметром string и реализовать логику работы по описанию.
def string_info(string:str):
    count_calls()
    return ((len(string),string.upper(),string.lower()))

#Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
#Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
def is_contains(string:str, list_to_search:list):
    in_list = False
    count_calls()
    for i in range(len(list_to_search)):
        string_in_list = str(list_to_search[i])
        if string.upper() == string_in_list.upper():
            in_list = True
            break
    return in_list


#Создать переменную calls = 0 вне функций.
calls = 0
#Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
print(string_info('Пространство имён'))
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(is_contains('пРосТраНство', ['Пространство', 'имён'])) #пРосТраНство ~ Пространство
#Вывести значение переменной calls на экран(в консоль).
print(f'ФУНКЦИИ ВЫЗВАНЫ ВСЕГО {calls} РАЗ')
