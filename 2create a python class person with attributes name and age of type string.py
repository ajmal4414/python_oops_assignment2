"""
2.create a python class person with attributes name and age of type string
1.create a display() method that displays the name and age of an onject created via the person class
2.create a child class student which inherits from the person class and which alse has a section attribute
3.create a method displaystudent() that displays the name,age and section of an object created via the student
class
4.create a student object via an instantiation on the student class and then test the displaystudent method

"""

class person:
    def __init__(self,name,age):
        self.Name=name
        self.Age=age

    def Display(self):
        print("Name of the person is:",self.Name)
        print("Age of the person is:",self.Age)
class Student(person):
    def __init__(self,name,age,section):
        person.__init__(self,name,age)
        self.Section=section

    def DisplayStudent(self):
        print("Student Name:",self.Name)
        print("Student Age:",self.Age)
        print("Student section:",self.Section)

A=person("tom",20)
A.Display()

S=Student("john",22,"python")
S.DisplayStudent()