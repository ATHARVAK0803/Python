#oop concepts 
'''1) class :- it is a concept to describe a object.
                class contains data members (class variables)
    2)object :- it is an instance of a class.
                it is runtime entity'''
'''
* the  init method in python is a constructor.
it is autamatically called when an obbject is created from a calss 
it is used to initialize the odject"s attributes
'''
'''
class Car:
    wheels=4
    def display(self):
        print("This car has 4 wheels")

honda=Car()
honda.display()


class Person:
    name="Ram"
    age = 56
    def info(self):
        print("Your name is ",self.name,"And age is ",self.age)

p=Person()
print(p.name)
p.info()
'''
'''
class car :
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model 

myCar=car("toyota","v9")
print(myCar.brand)

'''
'''
#Example

class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def showInfo(self):
        print("Your name is",self.name,"your grade is",self.grade)
obj=Student("atharva","O grade")
obj.showInfo();
'''


#Wap to calculate the area of rectanagle
'''
class Rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

# Creating an instance of the class
r = Rect(30, 5)

# Calling the 'area' method
print(r.area())
'''
'''
 class Rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area (self):
        ans=self.l*self.b
        print("The area is",ans)
r=Rect(30,5)
r.area()
'''
class Rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b
        
    def area(self):
        ans = self.l * self.b
        print("The area is", ans)
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
r = Rect(length, breadth)
r.area()
