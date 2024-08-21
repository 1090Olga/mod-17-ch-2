# "Итераторы"
class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start: int, stop: int, step: int = 1):
        if step == 0:
            raise StepValueError
        self.start = start
        self.stop = stop
        self.step = step

    def __str__(self):
        return str(self.pointer)

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        if self.step > 0 and self.pointer > self.stop - self.step:
            raise StopIteration
        if self.step < 0 and self.pointer < self.stop - self.step:
            raise StopIteration
        self.pointer += self.step
        return self


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iterators = (Iterator(-5, 1),
             Iterator(6, 15, 2),
             Iterator(5, 1, -1),
             Iterator(10, 1)
             )

for iterator in iterators:
    for i in iterator:
        print(i, end=' ')
    print()