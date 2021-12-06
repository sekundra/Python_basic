#  Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
#  этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
#  и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#  Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):
    # конструктор класса
    @abstractmethod
    def __init__(self, name='Some clothes'):
        self.name = name

    # методы класса
    @abstractmethod
    def fabric_amt(self):
        return f'It just an abstract method'


class Coat(Clothes):
    # конструктор класса
    def __init__(self, name, v):
        Clothes.__init__(self, name)
        self.size = v

    # методы класса
    @property
    def fabric_amt(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    # конструктор класса
    def __init__(self, name, h):
        Clothes.__init__(self, name)
        self.size = h

    # методы класса
    @property
    def fabric_amt(self):
        return self.size*2 + 0.3


coat = Coat('Burberry', 48)
suit = Suit('Hugo Boss', 174)
tp = (coat, suit)
for el in tp:
    print(f'{el.__class__.__name__} {el.name} of size {el.size} takes {round(el.fabric_amt, 2)}m of fabric')
