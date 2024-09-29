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
    mazda = Car('Mazda', 1123940, 'f123gg')
except IncorrectVinNumber as e_1:
    print(e_1.vin_message)
except IncorrectCarNumbers as e_2:
    print(e_2.car_num_message)
else:
    print(f'{mazda.model} успешно создан!')

try:
    c2 = Car('FastCar', 1123940, 'o54dd')
except IncorrectVinNumber as e_1:
    print(e_1.vin_message)
except IncorrectCarNumbers as e_2:
    print(e_2.car_num_message)
else:
    print(f'{c2.model} успешно создан!')

try:
    c3 = Car('BestMotors', 'wow', 'o132xx')
except IncorrectVinNumber as e_1:
    print(e_1.vin_message)
except IncorrectCarNumbers as e_2:
    print(e_2.car_num_message)
else:
    print(f'{c3.model} успешно создан!')

try:
    c4 = Car('BestMotors', 7654321, '1ABV13')
except IncorrectVinNumber as e_1:
    print(e_1.vin_message)
except IncorrectCarNumbers as e_2:
    print(e_2.car_num_message)
else:
    print(f'{c4.model} успешно создан!')

try:
    c5 = Car('BestMotors', 1234567, '123456')
except IncorrectVinNumber as e_1:
    print(e_1.vin_message)
except IncorrectCarNumbers as e_2:
    print(e_2.car_num_message)
else:
    print(f'{c5.model} успешно создан!')