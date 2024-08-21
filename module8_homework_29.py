# "Списковые, словарные сборки"
# Цель работы
# Освоить механизмы работы встроенных функций map и filter. Закрепить их различия и узнать, как передавать пользовательскую функцию, как аргумент в функции map и filter.
# Задание
# Дан список целых чисел, примените функции map и filter так, чтобы в конечном списке оставить нечётные квадраты чисел
# Примечание
# Не забывайте, что встроенные функции map и filter возвращают генератор, сами операции преобразования не выполняются.
# Входные данные
# [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
# Выходные данные
# [1, 25, 49, 121, 1225, 7921]
class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__is_valid_vin(vin)
        self.__vin = vin
        self.__is_valid_numbers(numbers)
        self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) and 1000000 <= vin_number <= 9999999:
            return True
        else:
            raise IncorrectVinNumber

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) and len(numbers) == 6:
            return True
        else:
            raise IncorrectCarNumbers


class IncorrectVinNumber(Exception):
    def __init__(self):
        self.message = 'Некорректный тип vin номер'


class IncorrectCarNumbers(Exception):
    def __init__(self):
        self.message = 'Некорректный тип данных для номеров'


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')