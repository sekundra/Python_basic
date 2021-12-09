# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

from time import sleep


class TrafficLight:
    # атрибуты класса
    def __init__(self):
        print("I'm a TrafficLight")
        self.__color = ''

    # методы класса
    def running(self, times):
        colors = (('Red', 7), ('Yellow', 2), ('Green', 5))
        for i in range(times):
            if i > 0:
                self.__color = 'Yellow'
                print(f'Light is: {self.__color}')
                sleep(2)
            for color in colors:
                self.__color = color[0]
                print(f'Light is: {self.__color}')
                sleep(color[1])


n = int(input('Enter how many times to show light changing cycle:'))
light = TrafficLight()
light.running(n)
