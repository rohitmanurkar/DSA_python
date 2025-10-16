
""" starting with classes and objects understand how we create it with default constructor """
class human:
    age = 10
    name = "John"

h1=human()
#print(h1.age)

"""Now in python for construction we define a method called __init__() which is called automatically when we create an object of that class"""
class phone:
    #we cant create a static variable in python as in python their is no static keyword so to create a static variable what we do
    #let's see
    phonecnt = 0
    def __init__(self, brand, price):# this is a constructor
        self.brand = brand # this is how we create instance variable in python using self as we dont have this keyword in python
        self.price = price
        phone.phonecnt += 1 #this is how we create a static variable in python

p1 = phone("Apple", 1000)# creating an object of class phone

# accessing instance variable
# print(p1.brand)
# print(p1.price)
# print(f"using class phonecnt is {p1.phonecnt}") # accessing static variable
# # we can also access static variable using object but its not a good practice
# # Accessing it via an instance will also work, but modification via an instance
# # will create a new instance variable, not modify the class variable.
# print(f"using object which is not good practice{p1.phonecnt}")

""" We can also create multiple constructors and can call multiple constructor while creating a single object  by the following methods in python
In Python, unlike languages like Java or C++, you cannot have multiple constructors in the same class (i.e., multiple `__init__` methods).
However, there are several Pythonic ways to achieve similar behavior — to create objects in multiple ways.

Let's go over the main techniques 


1. Use Default Arguments in `__init__`

This is the simplest way to mimic multiple constructors.

```
class Person:
    def __init__(self, name=None, age=None):
        if name is not None and age is not None:
            self.name = name
            self.age = age
        elif name is not None:
            self.name = name
            self.age = 0
        else:
            self.name = "Unknown"
            self.age = 0

p1 = Person("Alice", 25)
p2 = Person("Bob")
p3 = Person()
```

Explanation:
By using optional parameters and conditional logic, you can simulate different ways to construct an object.


2. Use `@classmethod` as Alternative Constructors

This is the most common and Pythonic method.

```p
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, info_str):
        name, age = info_str.split("-")
        return cls(name, int(age))

    @classmethod
    def newborn(cls, name):
        return cls(name, 0)

p1 = Person("Alice", 25)
p2 = Person.from_string("Bob-30")
p3 = Person.newborn("Charlie")
```
Explanation:
Each `@classmethod` provides an alternative constructor — a different way to create an instance of the same class.

 3. Use Static Methods or Factory Functions

Sometimes, you might prefer standalone functions (or static methods) for constructing objects in flexible ways.

```
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def from_diameter(diameter):
        return Circle(diameter / 2)

c1 = Circle(5)
c2 = Circle.from_diameter(10)
```

# Summary

| Method             | Description               | Example                             |
| ------------------ | ------------------------- | ----------------------------------- |
| Default arguments  | Simplest approach         | `def __init__(self, a=None)`        |
| Class methods      | Most common & clean       | `@classmethod def from_string(...)` |
| Static methods     | For factory-like creation | `Circle.from_diameter()`            |
| `__new__` override | Advanced customization    | For special cases                   |


"""
#----------------------------------------------------------------------------------------------------------
""" Lets Move Ahead and see the pillers of OOPS in python 
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
"""
#--------------------------------------------------------------------------------------------------------------------------------------------
# 1. Inheritance
"""Inheritance defination : It is a mechanism where one class(child) derives attributes and behaviors from another class(parent)
Real world Example :
A library class has common attributes like books and methods for borrowing and returning books.
A  DigitalLibrary class can inherit from Library and add attributes like digitalBooks and methods for downloading books.

Types of INHERITANCE:
1. SINGLE INHERITANCE
2. MULTIPLE INHERITANCE 
3. HIRARCHICAL INHERITANCE
4. MULTI LEVEL INHERITANCE 
5. HYBRID INHERITANCE
"""

""" 1. SINGLE INHERITANCE
    REAL WORLD EXAMPLE :
    Imagine a SMARTLOCK system. A BASICLOCK class can extend the SMARTLOCK class to add features
    like add notification and remote access
"""

class basiclock:
    def __init__ (self, brand):
        self.brand = brand
    """
    once we create a constructor the default constructor is gone
    """

    def lock(self):
        print("This is a basic locksystem to lock")

    def unlock(self):
        print("This is a basiclock system to unlock ")

class smartlock(basiclock): #This is the syntax for inheritance of the class here smartlock is inheriting basic lock
    
    def __init__(self):
        super().__init__("hk")
    """
    when we dont have a default constructor of parent class we have to access the available constructor to complete the object creation 
    """
    def remote_acess(self):
        print("Accessing Remotly")

s1 = smartlock()
# s1.lock() # since lock method is in basiclock and smartlock is inheriting it so it will perform lock
# s1.remote_acess()

""""2. HIRARCHICAL INHERITANCE
    Real World Example : A VEHICLE class can has subclasses as CAR and BIKE which inherit common attributes
"""

class vehicle:
    def start(self):
        print("vehicle is starting")

#chlid class
class car(vehicle):
    def drive(self):
        print("Diving the car")

#another child class of vehicle 

class bike(vehicle):
    def drive(self):
        print("Driving the vehicle")
        
    
c1 = car()
b1 = bike()

c1.start() # start is a function in vehicle class which is inherited by car class
c1.drive()
b1.start() # Start is a function in vehicle which is also inherited by the bike class also
b1.drive() 





