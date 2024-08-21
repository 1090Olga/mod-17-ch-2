# Декораторы
def is_prime(func):
    def wrapper(*args):
        sum_ = func(*args)
        res = f'Сумма чисел {args} = {sum_}\n'
        check = 'составное' if sum(not (sum_ % x) for x in range(2, int(sum_**0.5) + 1)) else 'простое'
        return res + f'{sum_} – {check} число\n' + '-' * 30
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


numbers_tuple = ((2, 3, 6), (1, 2, 3), (4, 5, 8), (7, 6, 9))
for numbers in numbers_tuple:
    print(sum_three(*numbers))