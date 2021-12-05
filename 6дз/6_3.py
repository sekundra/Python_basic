# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    # конструктор класса
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


Manager = Position('Ivan', 'Ivanov', 'Manager', 2340, 12)
print(f'{Manager.name} {Manager.surname} - {Manager.position}\n{Manager._income}')
print(f'Worker name: {Manager.get_full_name()}')
print(f'Worker income: {Manager.get_total_income()}')
Janitor = Position('Petr', 'Petrov', 'Janitor', 3, 0.5)
print(f'{Janitor.name} {Janitor.surname} - {Janitor.position}\n{Janitor._income}')
print(f'Worker name: {Janitor.get_full_name()}')
print(f'Worker income: {Janitor.get_total_income()}')
