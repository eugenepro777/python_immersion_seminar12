"""
Задание №1.
    Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
    Экземпляр должен запоминать последние k значений.
    Параметр k передаётся при создании экземпляра.
    Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""


class Factorial:
    def __init__(self, k):
        self.k = k
        self.result_dict = {}

    def __call__(self, value):
        if value < 0:
            raise ValueError('Факториал только для положительных чисел')
        if value in self.result_dict:
            return self.result_dict[value]
        result = 1 if value == 0 else value * self.__call__(value - 1)
        self.result_dict[value] = result
        if len(self.result_dict) > self.k:
            self.result_dict.pop(next(iter(self.result_dict)))
        return result

    def __str__(self):
        return f'Factorial(k={self.k}, values={self.view_latest_values()})'

    def view_latest_values(self):
        return self.result_dict.copy()


if __name__ == '__main__':

    f1 = Factorial(5)
    for i in range(1, 11):
        result = f1(i)
        print(f'Факториал от {i}: {result}')
    print(f1)
    print(f1.view_latest_values())
