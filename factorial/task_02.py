import json

"""
Задание №2.
    Доработаем задачу 1.
    Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            pass
        with open('cached_values.json', 'w', encoding='utf-8') as file:
            json.dump(self.result_dict, file, indent=2)
        print(f'Файл сохранен')

    def view_latest_values(self):
        return self.result_dict.copy()


if __name__ == '__main__':

    f1 = Factorial(5)

    with f1 as factorial:
        for i in range(1, 11):
            result = f1(i)
            print(f'Факториал от {i}: {result}')
