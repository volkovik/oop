class Car:
    def __init__(self, brand, model, year, color, price):
        self._brand = brand
        self._model = model
        self._year = year
        self._color = color
        self._price = price

    def get_info(self):
        return f'{self._brand} {self._model} {self._year} {self._color} ${self._price}'

    def change_brand(self, new_brand):
        self._brand = new_brand

    def change_model(self, new_model):
        self._model = new_model

    def change_year(self, new_year):
        self._year = new_year

    def change_color(self, new_color):
        self._color = new_color


car1 = Car('BMW', 'X5', 2020, 'black', 100000)
car2 = Car('Audi', 'A6', 2019, 'white', 80000)
car3 = Car('Mercedes', 'GLE', 2018, 'red', 90000)

print('Информация о машинах:')
print(car1.get_info())
print(car2.get_info())
print(car3.get_info())

car1.change_brand('Toyota')
car2.change_model('A8')
car3.change_year(2021)

print('\nИнформация о машинах после изменения:')
print(car1.get_info())
print(car2.get_info())
print(car3.get_info())
