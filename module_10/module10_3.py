# Блокировки потоков для доступа к общим данным"
# Цель задания:
# Практически применить знания о механизмах блокировки потоков в Python, используя класс Lock из модуля threading.
#
# Задание:
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
#
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег. Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации общего ресурса.
#
# Пример работы:
# def deposit_task(account, amount):
#     for _ in range(5):
#         account.deposit(amount)
#
# def withdraw_task(account, amount):
#     for _ in range(5):
#         account.withdraw(amount)
#         account = BankAccount()
#
# deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
# withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))
#
# deposit_thread.start()
# withdraw_thread.start()
#
# deposit_thread.join()
# withdraw_thread.join()
#
# Вывод в консоль:
# Deposited 100, new balance is 1100
# Deposited 100, new balance is 1200
# Deposited 100, new balance is 1300
# Deposited 100, new balance is 1400
# Deposited 100, new balance is 1500
# Withdrew 150, new balance is 1350
# Withdrew 150, new balance is 1200
# Withdrew 150, new balance is 1050
# Withdrew 150, new balance is 900
# Withdrew 150, new balance is 750

import threading


class BankAccount:
    def __init__(self, name, balance, lock, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.name = name
        self.balance = balance
        self.lock = lock

    def withdraw(self, amount1):
        with self.lock:
            self.amount1 = amount1
            self.balance -= self.amount1
            print(f'Withdrew {self.amount1}, new balance is {self.balance}')

    def deposit(self, amount2):
        with self.lock:
            self.amount2 = amount2
            self.balance += self.amount2
            print(f'Deposited {self.amount2}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


lock = threading.Lock()
account = BankAccount('101102', 1000, lock=lock)

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()