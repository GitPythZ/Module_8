class Car():
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif vin_number not in range(1000000, 9999999 + 1):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True

    def __is_valid_numbers(self, numbers):
        lst_numbers = []
        for num in numbers:
            lst_numbers.append(num)
        check_lst = [x.isdigit() for x in lst_numbers]
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        elif check_lst[1] is not True and check_lst[2] is not True and check_lst[3] is not True:
            raise IncorrectCarNumbers("Ошибка в номере! В номере машины на 2, 3 и 4 месте должны быть цифры")
        elif check_lst[0] is True and check_lst[4] is True and check_lst[5] is True:
            raise IncorrectCarNumbers("Ошибка в номере! В номере 1, 5 и 6 знак должны быть буквами")
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, vin_message):
        self.vin_message = vin_message


class IncorrectCarNumbers(Exception):
    def __init__(self, car_num_message):
        self.car_num_message = car_num_message


try:
    first = Car('Toyota', 1000000, 'f123gg')
except IncorrectVinNumber as exc:
    print(exc.vin_message)
except IncorrectCarNumbers as exc:
    print(exc.car_num_message)
else:
    print(f'{first.model} успешно создан!')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.vin_message)
except IncorrectCarNumbers as exc:
    print(exc.car_num_message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.vin_message)
except IncorrectCarNumbers as exc:
    print(exc.car_num_message)
else:
    print(f'{third.model} успешно создан')

try:
    c4 = Car('Baltiyec', 7654321, '1ABV13')
except IncorrectVinNumber as exc:
    print(exc.vin_message)
except IncorrectCarNumbers as exc:
    print(exc.car_num_message)
else:
    print(f'{c4.model} успешно создан!')

try:
    c5 = Car('BMW', 1234567, '123456')
except IncorrectVinNumber as exc:
    print(exc.vin_message)
except IncorrectCarNumbers as exc:
    print(exc.car_num_message)
else:
    print(f'{c5.model} успешно создан!')
