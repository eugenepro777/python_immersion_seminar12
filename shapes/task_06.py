"""
Задание №6
    Изменяем класс прямоугольника.
    Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Validator:
    def __init__(self, min_v, max_v):
        self.min_v = min_v
        self.max_v = max_v

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if self.min_v is not None and value < self.min_v:
            raise ValueError(f"{value} < границы {self.min_v}")
        if self.max_v is not None and value > self.max_v:
            raise ValueError(f"{value} > границы {self.max_v}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print('hi')
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        print('delete')
        del instance.__dict__[self.name]


class Rectangle:
    """Класс для создания прямоугольников"""

    length = Validator(10, 20)
    width = Validator(10, 20)

    # __slots__ = ('_length', '_width')

    def __init__(self, length=0, width=0):
        """
        Конструктор класса
        :param length: длина
        :param width: ширина
        """
        self.length = length
        self.width = width

    def __add__(self, other):
        """
        Сложение двух прямоугольников и создание нового прямоугольника
        :param other: Длина и ширина другого прямоугольника
        :return: Новый прямоугольник
        """
        result = self.calculate_perimeter + other.calculate_perimeter
        return Rectangle(result)

    def __sub__(self, other):
        """
        Вычитание двух прямоугольников и создание нового прямоугольника.
        При вычитании из меньшего большего прямоугольника получим прямоугольник с нулевыми сторонами
        :param other: Длина и ширина другого прямоугольника
        :return: Новый прямоугольник
        """
        result = abs(self.calculate_perimeter - other.calculate_perimeter)
        return Rectangle(result)

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'

    def __eq__(self, other):
        return self.calculate_area == other.calculate_area

    def __ne__(self, other):
        return not self.calculate_area == other.calculate_area

    def __gt__(self, other):
        return self.calculate_area > other.calculate_area

    def __ge__(self, other):
        return self.calculate_area >= other.calculate_area

    def __lt__(self, other):
        return self.calculate_area < other.calculate_area

    def __le__(self, other):
        return self.calculate_area <= other.calculate_area

    @property
    def calculate_perimeter(self):
        """
        Для вычисления периметра прямоугольника
        :return: Периметр прямоугольника
        """
        rectangle_perimeter = 2 * (self.length + self.width)
        return rectangle_perimeter

    @property
    def calculate_area(self):
        """
        Для вычисления площади прямоугольника
        :return: Площадь прямоугольника/квадрата
        """
        if self.length == 0:
            return self.width ** 2
        elif self.width == 0:
            return self.length ** 2
        return self.length * self.width


if __name__ == '__main__':
    r1 = Rectangle(10, 20)
    r2 = Rectangle(10, 20)
    print(r1.width)
    del r1.width
    print(r1.__dict__)
    # r3 = Rectangle(4)
    # r4 = r1 + r2
    # print(r1)
    # print(r1.width)
    # print(r1.length)
    # r1.length = 11
    # r1.width = 7
    # print(r1)
    # print(r1.calculate_area)
    # print(r1.calculate_perimeter)
