# Class variables =   Share among all instance of a class
#                     Define outside of a constructor
#                     Allow you to share data among all objects from that class

class Student:
    
    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student('Spongebob', 30)
student2 = Student('Patrick', 28)
student3 = Student('Squidward', 25)


print(student1.name)
print(student1.age)
print(Student.class_year)
print(Student.num_students)


print(f'my Graduating class of {Student.class_year} has {Student.num_students} students')
print(student1.name)
print(student2.name)
print(student3.name)