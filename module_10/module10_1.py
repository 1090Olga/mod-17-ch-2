# "Создание потоков".
# Цель задания:
#
# Освоить механизмы создания потоков в Python.
# Практически применить знания, создав и запустив несколько потоков.
#
# Задание:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.
#
# Примечание:
# Используйте методы: start() для старта потока,
# join() для заморозки дальнейшей интерпретации,
# пока процессы не завершаться.
# Для установки интервала в 1 секунду используйте функцию sleep()
# из модуля time, предварительно импортировав его.
#
# Входные данные:
# Нет
# Выходные данные:
# 1
# a
# 2
# b
# 3
# c
# ......
# 10
# j
# import threading
# import time
#
# def numbers():
#     for elem in range(1, 11):
#         print(elem)
#         time.sleep(1)
# def alfavit():
#     for i in 'abcdefghij':
#         print()
#         time.sleep(1)
# thread1 = threading.Thread(target=numbers)
# thread2 = threading.Thread(target=alfavit)
#
# thread1.start()
# thread2.start()
#
#
#
# thread1.join()
# thread2.join()

import threading
import time

def numbers():
    for elem in range(1, 11):
        print(elem)
        time.sleep(1)

def alfavit():
    for i in 'abcdefghij':
        print(i)
        time.sleep(1)
thread1 = threading.Thread(target=numbers)
thread2 = threading.Thread(target=alfavit)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

