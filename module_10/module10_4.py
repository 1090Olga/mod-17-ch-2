"Очереди для обмена данными между потоками."
# Задание:
# Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи и уходящих после завершения приема.
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и уходят. Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.
# Создайте 3 класса:
# Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола, is_busy(bool) - занят стол или нет.
# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов, в случае наличия стола - начинает обслуживание посетителя (запуск потока), в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)
# Пример работы:
# # Создаем столики в кафе
# table1 = Table(1)
# table2 = Table(2)
# table3 = Table(3)
# tables = [table1, table2, table3]
# # Инициализируем кафе
# cafe = Cafe(tables)
# # Запускаем поток для прибытия посетителей
# customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
# customer_arrival_thread.start()
# # Ожидаем завершения работы прибытия посетителей
# customer_arrival_thread.join()
# Вывод на консоль (20 посетителей [ограничение выставить в методе customer_arrival]):
# Посетитель номер 1 прибыл
# Посетитель номер 1 сел за стол 1
# Посетитель номер 2 прибыл
# Посетитель номер 2 сел за стол 2
# Посетитель номер 3 прибыл
# Посетитель номер 3 сел за стол 3
# Посетитель номер 4 прибыл
# Посетитель номер 4 ожидает свободный стол
# Посетитель номер 5 прибыл
# Посетитель номер 5 ожидает свободный стол
# ......
# Посетитель номер 20 прибыл
# Посетитель номер 20 ожидает свободный стол
# Посетитель номер 17 покушал и ушёл.
# Посетитель номер 20 сел за стол N.
# Посетитель номер 18 покушал и ушёл.
# Посетитель номер 19 покушал и ушёл.
# Посетитель номер 20 покушал и ушёл.

import time
import queue
from threading import Thread, Lock

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Customer(Thread):
    def __init__(self, number, table, cafe):
        super().__init__()
        self.number = number
        self.table = table
        self.cafe = cafe

    def run(self):
        time.sleep(5)
        with self.cafe.lock:
            print(f'Посетитель номер {self.number} покушал за столиком и ушёл.')
            self.table.is_busy = False
            self.cafe.check_queue()

class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables
        self.customers = []
        self.lock = Lock()

    def customer_arrival(self):
        for people in range(1, 21):
            time.sleep(1)
            print(f'Посетитель номер {people} прибыл.')
            self.serve_customer(people)

    def serve_customer(self, people):
        with self.lock:
            for table in self.tables:
                if not table.is_busy:
                    self.seat_customer(people, table)
                    break
            else:
                self.queue.put(people)
                print(f'Посетитель номер {people} ожидает свободный стол.')

    def seat_customer(self, people, table):
        customer = Customer(people, table, self)
        self.customers.append(customer)
        print(f'Посетитель номер {people} сел за стол {table.number}.')
        table.is_busy = True
        customer.start()

    def check_queue(self):
        if not self.queue.empty():
            next_customer = self.queue.get()
            for table in self.tables:
                if not table.is_busy:
                    self.seat_customer(next_customer, table)
                    break

tables_list = [Table(1), Table(2), Table(3)]
cafe = Cafe(tables_list)

customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()

for customer_ in cafe.customers:
    customer_.join()
