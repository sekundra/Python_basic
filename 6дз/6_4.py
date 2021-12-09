# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    # конструктор класса
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    # методы класса
    def go(self):
        print(f'{self.name} is on the go!')

    def stop(self):
        print(f'{self.name} has stopped!')

    def turn(self, direction: str):
        print(f'{self.name} has turned {direction}!')

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Current speed of {self.name} is {self.speed}. Speed limit for TownCar exceeded!')
        else:
            print(f'Current speed of {self.name} is {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            return f'Current speed of {self.name} is {self.speed}. Speed limit for WorkCar exceeded!'
        else:
            print(f'Current speed of {self.name} is {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


FirstCar = TownCar(100, 'Red', 'Mazda')
print(f'FirstCar is {FirstCar.__class__.__name__} {FirstCar.color} {FirstCar.name} with speed {FirstCar.speed}, '
      f'police flag is {FirstCar.is_police}')
FirstCar.go()
FirstCar.turn('Left')
FirstCar.stop()
FirstCar.show_speed()

SecondCar = SportCar(350, 'Black', 'Ferrari')
print(f'\nSecondCar is {SecondCar.__class__.__name__} {SecondCar.color} {SecondCar.name} with speed {SecondCar.speed}, '
      f'police flag is {SecondCar.is_police}')
SecondCar.go()
SecondCar.turn('Right')
SecondCar.stop()
SecondCar.show_speed()

ThirdCar = WorkCar(30, 'White', 'Ford')
print(f'\nThirdCar is {ThirdCar.__class__.__name__} {ThirdCar.color} {ThirdCar.name} with speed {ThirdCar.speed}, '
      f'police flag is {ThirdCar.is_police}')
ThirdCar.go()
ThirdCar.turn('Right')
ThirdCar.stop()
ThirdCar.show_speed()

FourthCar = PoliceCar(150, 'Striped', 'Mercedes')
print(f'\nFourthCar is {FourthCar.__class__.__name__} {FourthCar.color} {FourthCar.name} with speed {FourthCar.speed}, '
      f'police flag is {FourthCar.is_police}')
FourthCar.go()
FourthCar.turn('Right')
FourthCar.stop()
FourthCar.show_speed()
print()
