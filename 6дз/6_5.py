# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationary:
    # конструктор класса
    def __init__(self, title):
        self.title = title

    # методы класса
    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки с помомщью ручки {self.title}')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки с помомщью карандаша {self.title}')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки с помомщью маркека {self.title}')


Pen = Pen('Parker')
print(f'Ручка {Pen.title}')
Pen.draw()
Pencil = Pencil('Stabilo')
print(f'\nКарандаш {Pencil.title}')
Pencil.draw()
Handle = Handle('ErichKrause')
print(f'\nМаркер {Handle.title}')
Handle.draw()
