# Домашнее задание №1
class Matrix:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for i in range(len(self.list_1)):
            for k in range (len(self.list_2)):
                matrix[i][k] = self.list_1[i][k] + self.list_2[i][k]

        return str('\n'.join(['\t'.join([str(k) for k in i]) for i in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(k) for k in i]) for i in matrix]))


test_matrix = Matrix([
            [2, 3, 5],
            [2, 5, 2],
            [6, 1, 1],
        ],[
            [5, 7, 8],
            [2, 3, 9],
            [1, 1, 1],
        ]
)

print(test_matrix.__add__())

# Домашнее задание №2
class Textile:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_coat_square(self):
        return self.width / 6.5 + 0.5

    def get_jacket_square(self):
        return self.height * 2 + 0.3

    @property
    def get_full_square(self):
        return str(f'Общая площадь ткани \n'
                   f' {(self.get_coat_square()) + (self.get_jacket_square())}')


class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.get_coat_square())

    def __str__(self):
        return f'Площадь, требуемая для пальто {self.square_c}'


class Jacket(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.get_jacket_square())

    def __str__(self):
        return f'Площадь, требуемая на костюм {self.square_j}'

coat = Coat(5, 9)
jacket = Jacket(2, 3)
print(coat)
print(jacket)
print(coat.get_full_square)
print(jacket.get_full_square)
print(jacket.get_coat_square())
print(jacket.get_jacket_square())

# Домашнее задание №3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Результат отрицательный')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(12)
cells2 = Cell(3)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(12))
print(cells1.make_order(3))
print(cells1 / cells2)