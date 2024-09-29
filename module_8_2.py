# Задача "План перехват":
def personal_sum(*numbers):
    """
    Функция считает сумму чисел коллекции numbers.
    Обрабатывает ошибку TypeError, при встрече с данным отличными от int;
    Считает кол-во некорректных типов в коллекции;
    Возвращает кортеж, содержащий сумму чисел и счетчик ошибок;
    """
    result = 0
    incorrect_data = 0
    try:
        for num in numbers:
            result += num
    except TypeError:
        incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    numbers_len = []
    try:
        for num in numbers:
            if isinstance(num, int):
                numbers_len.append(num)
    except TypeError:
        pass
    try:
        return personal_sum(*numbers)[0] / len(numbers_len)
    except ZeroDivisionError:
        return f"На ноль делить нельзя"
    except TypeError:
        return "Incorrect data type in <numbers>"


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
