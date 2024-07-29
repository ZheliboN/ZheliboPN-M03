#Входные данные (применение функции):

def calculate_structure_sum(data_structure):
    sum_result = 0
    count_element = len(data_structure)
    if count_element == 0:
        return 0
    else:
        for element in data_structure:
            if isinstance(element,tuple):
                sum_result+=calculate_structure_sum(element)
            elif isinstance(element, list):
                sum_result += calculate_structure_sum(element)
            elif isinstance(element, dict):
                key_list = element.keys()
                sum_result += calculate_structure_sum(key_list)
                value_list = element.values()
                sum_result += calculate_structure_sum(value_list)
            elif isinstance(element, set):
                sum_result +=calculate_structure_sum(element)
            elif isinstance(element, str):
                sum_result += len(element)
            elif isinstance(element, int):
                sum_result += element
            elif isinstance(element, float):
                sum_result += element
        return sum_result


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = 0
result = calculate_structure_sum(data_structure)
print(f'Результат вычисления суммы структуры {data_structure} с помощью рекурсии:')
print(result)

