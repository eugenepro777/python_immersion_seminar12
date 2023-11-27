from sys import getsizeof
"""
Задание №4
    Доработайте класс прямоугольник из прошлых семинаров.
    Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
    Используйте декораторы свойств.
    Задание №5
    Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""


class Rectangle:
    """Класс для создания прямоугольников"""

    __slots__ = ('_length', '_width')

    def __init__(self, length=0, width=0):
        """
        Конструктор класса
        :param length: длина
        :param width: ширина
        """
        self._length = length
        self._width = width

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
        return f'Rectangle({self._length}, {self._width})'

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
        rectangle_perimeter = 2 * (self._length + self._width)
        return rectangle_perimeter

    @property
    def calculate_area(self):
        """
        Для вычисления площади прямоугольника
        :return: Площадь прямоугольника/квадрата
        """
        if self._length == 0:
            return self._width ** 2
        elif self._width == 0:
            return self._length ** 2
        return self._length * self._width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError(f'Значение длины должно быть положительным числом')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError(f'Значение ширины должно быть положительным числом')


if __name__ == '__main__':
    r1 = Rectangle(5, 4)
    print(getsizeof(r1.__slots__))
    r2 = Rectangle(5, 2)
    r3 = Rectangle(4)
    r4 = r1 + r2
    print(r1)
    print(r1.width)
    print(r1.length)
    r1.length = 11
    r1.width = 7
    print(r1)
    print(r1.calculate_area)
    print(r1.calculate_perimeter)
