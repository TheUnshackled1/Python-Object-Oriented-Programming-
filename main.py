from car import Car

car1 = Car("Toyota", 2020, "Red", False)
car2 = Car("Mustang", 2010, "Blue", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print('==============')

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car2.describe()