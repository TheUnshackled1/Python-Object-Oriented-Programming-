# Inheritance = Allows a class  inherit attributes and method from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name 
        self.is_alive = True
    def eat(self):
        print(f'{self.name} is eating')
    def sleep(self):
        print(f'{self.name} is sleeping')
    
class Dog(Animal):
    def speak(self):
        print("ARFF")

class Cat(Animal):
    def speak(self):
        print('MEOW')

class Mouse(Animal):
    def speak(self):
        print('SQUEK')


dog = Dog('Scooby')
cat = Cat('Garfield')
mouse = Mouse('Mickey')

print(cat.name)
print(cat.is_alive)
cat.sleep()



cat.speak()