from my_exceptions import RectangleLowerNullError, RectangleNotNumberError


class Rectangle:
    '''Класс прямоугольник, с методами расчета периметра и площади фигуры.'''

    def __init__(self, a: float, b: float = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self.a + self.b)

    def area(self):
        '''Метод расчета площади прямоугольника.'''
        return self.a * self.b

    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        '''Переопределенный дандер метод вычетания двух прямоугольников.'''
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса'''
        return f'Прямоугольник {self.a} x {self.b}'


if __name__ == '__main__':
    try:
        a = float(input('Введите сторону a прямоугольника: '))
    except ValueError:
        raise RectangleNotNumberError('a')
    try:
        b = float(input('Введите сторону b прямоугольника: '))
    except ValueError:
        raise RectangleNotNumberError('b')
    if a <= 0 or b <= 0:
        raise RectangleLowerNullError(a, b)
    else:
        rect_1 = Rectangle(a, b)

    print('Все ок')
