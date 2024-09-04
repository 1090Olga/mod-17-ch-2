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
