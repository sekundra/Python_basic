# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class WrongAmount(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, name='Warehouse'):
        self.name = name
        self.stock = {}
        self.in_use = {}

    def acceptance(self, equipment, amount):
        if equipment.eq_type in self.stock.keys():
            self.stock[equipment.eq_type] += amount
        else:
            self.stock[equipment.eq_type] = amount

    def transfer(self, equipment, amount, department):
        try:
            amount = float(amount)
            if amount < 0 or amount % 1 > 0:
                raise WrongAmount(f'amount of equipment to transfer must be positive integer!')
        except (WrongAmount, ValueError):
            print(f'amount of equipment to transfer must be positive integer!')
        else:
            amount = int(amount)
            if not (equipment.eq_type in self.stock.keys()) or self.stock[equipment.eq_type] == 0:
                print(f"Can't transfer {amount} {equipment.eq_type} to {department}, it is out of stock!")
            else:
                self.stock[equipment.eq_type] -= min(amount,self.stock[equipment.eq_type])
                if department in self.in_use.keys():
                    if equipment.eq_type in self.in_use[department].keys():
                        self.in_use[department][equipment.eq_type] += amount
                    else:
                        self.in_use[department][equipment.eq_type] = amount
                else:
                    self.in_use[department] = {equipment.eq_type: amount}
                print(f"{amount} {equipment.eq_type} successfully transferred to {department}")


class Equipment:
    def __init__(self, brand, is_color: bool, weight, eq_type):
        self.brand = brand
        self.is_color = is_color
        self.weight = weight
        self.eq_type = eq_type


class Printer(Equipment):
    def __init__(self, brand, is_color, weight, tech_type):
        Equipment.__init__(self, brand, is_color, weight, eq_type='Printer')
        self.tech_type = tech_type


class Scanner(Equipment):
    def __init__(self, brand, is_color, weight, speed):
        Equipment.__init__(self, brand, is_color, weight, eq_type='Scanner')
        self.speed = speed


class Copier(Equipment):
    def __init__(self, brand, is_color, weight, max_listnum):
        Equipment.__init__(self, brand, is_color, weight, eq_type='Copier')
        self.max_listnum = max_listnum


printer = Printer('brother', False, 10, 'Laser')
scanner = Scanner('HP', True, 3, 5)
copier = Copier('Xerox', True, 80, 120)
print(f'{printer.eq_type} is {printer.brand}, color flag is {printer.is_color}, technical type is {printer.tech_type}')
print(f'{scanner.eq_type} is {scanner.brand}, color flag is {scanner.is_color}, scan speed is {scanner.speed} '
      f'sec per page')
print(f'{copier.eq_type} is {copier.brand}, color flag is {copier.is_color}, max page capacity is {copier.max_listnum}')

# приемка товара на склад по категориям
warehouse = Warehouse()
warehouse.acceptance(printer, 3)
warehouse.acceptance(scanner, 8)
warehouse.acceptance(scanner, 2)
warehouse.acceptance(copier, 4)
print(f'Equipment in stock: {warehouse.stock}')

# выдача товара в подразделения
warehouse.transfer(printer, 3, 'HR')
warehouse.transfer(scanner, 2, 'Security')
print(f'Equipment in use by departments: {warehouse.in_use}')
print(f'Equipment in stock: {warehouse.stock}')
warehouse.transfer(printer, 3, 'Security')
warehouse.transfer(copier, 2, 'Security')
print(f'Equipment in use by departments: {warehouse.in_use}')
print(f'Equipment in stock: {warehouse.stock}')

# проверка допустимых значений в поле amount
warehouse.transfer(printer, -3, 'Security')
warehouse.transfer(copier, 2.5, 'Security')
warehouse.transfer(copier, "2", 'Security')
warehouse.transfer(copier, "asd", 'Security')

