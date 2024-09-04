# "Многопроцессное программирование"

# Задание:
# Моделирование программы для управления данными о движении товаров на складе и эффективной обработки запросов на обновление информации в многопользовательской среде.
# Представим, что у вас есть система управления складом, где каждую минуту поступают запросы на обновление информации о поступлении товаров и отгрузке товаров.
# Наша задача заключается в разработке программы, которая будет эффективно обрабатывать эти запросы в многопользовательской среде, с использованием механизма мультипроцессорности для обеспечения быстрой реакции на поступающие данные.
# Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:
# Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
# Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
# Есть 2 действия: receipt - получение, shipment - отгрузка.
# а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить значение ключа, если позиция уже была в словаре)
# б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).
# 3.Метод run - принимает запросы и создаёт для каждого свой параллельный процесс, запускает его(start) и замораживает(join).
# Пример работы:
# # Создаем менеджера склада
# manager = WarehouseManager()
# # Множество запросов на изменение данных о складских запасах
# requests = [
#   ("product1", "receipt", 100),
#   ("product2", "receipt", 150),
#   ("product1", "shipment", 30),
#   ("product3", "receipt", 200),
#   ("product2", "shipment", 50)
# ]
# # Запускаем обработку запросов
# manager.run(requests)
# # Выводим обновленные данные о складских запасах
# print(manager.data)
# Вывод на консоль:
# {"product1": 70, "product2": 100, "product3": 200}
import multiprocessing as mp
class WarehouseManager:
    def __init__(self, manager_dict):
        self.data = manager_dict

    def process_request(self, request):
        key, func, value = request
        match func:
            case 'receipt':
                if key in self.data:
                    self.data[key] += value
                else:
                    self.data[key] = value
            case 'shipment':
                if key in self.data:
                    if self.data[key] - value >= 0:
                        self.data[key] -= value
                    else:
                        print(f'Недостаточно товара {key}. В наличии: {self.data[key]}; нужно: {value}.')
                else:
                    print(f'Товара {key} нет на складе.')
            case _:
                print(func, '– неизвестный товар.')

    def run(self, requests):
        with mp.Pool(processes=4) as pool:
            pool.map(self.process_request, requests)


if __name__ == '__main__':
    # Создаем менеджера для хранения данных
    manager = mp.Manager()
    manager_dict = manager.dict()

    # Создаем менеджера склада
    manager = WarehouseManager(manager_dict)

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product1", "shipment", 70),
        ("product3", "receipt", 200),
        ("product3", "shipment", 2000),
        ("product2", "shipment", 50),
        ("product4", "shipment", 50),
        ("product2", "go", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print('-' * 50)
    print(manager.data)