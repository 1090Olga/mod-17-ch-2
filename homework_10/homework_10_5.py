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
                        print(f'Недостаточно товара {key}. Имеется: {self.data[key]}; запрашивается: {value}.')
                else:
                    print(f'Товара {key} нет на складе.')
            case _:
                print(func, '– неизвестный запрос.')

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