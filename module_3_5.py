#Пункты задачи:
#Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):
    # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    str_number = str(number)
    # 4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться
    # взять срез str_number[1:].
    if len(str_number) > 1:
        # Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый
        # символ из str_number в числовом представлении(int).
        first = int(str_number[0])
        # Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую
        # цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
        first = int(str_number[0])
        # Проверяем последнюю цифру на равенство 0, если она равна ноль, то предыдущее произведение будет умножено на 0
        if first ==0:
            first = 1
        return first


digits = 40203
result = get_multiplied_digits(digits)
print(f'Произведение значимых цифр числа {digits}:',result)
digits = 300070
result = get_multiplied_digits(digits)
print(f'Произведение значимых цифр числа {digits}:',result)