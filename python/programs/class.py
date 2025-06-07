class Airthop(object):
    """ """
    def __init__(self, num11, num22):
        self.num1 = num11
        self.num2 = num22
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2

class Inherit(Airthop):
    pass
    def add(self):
        return self.num1 + self.num2 +10

obj = Airthop(num11 = 1, num22 = 2)
print(obj)
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())
obj2 = Inherit(num11 = 5, num22 = 6)
print(obj2.add())

class Dog():
    #Class object atribute
    #Same for any object of class
    species = "mammal"
    def __init__(self, breed, name, spots):
        #Attributes we take in the argument
        #Assign it using self.atribute_name
        print(f"--->{breed}")
        self.breed = breed
        self.name = name
        self.spots = spots
    #Opetaions/Actions ---> methods
    def bark(self, number):
        print(f"Bow Bow! my name is {self.name} and number is {number}")

my_dog = Dog(breed = 'sighthound', name = 'Mudhol Hound', spots='Mudhol')
print(my_dog.breed, my_dog.name, my_dog.spots)
print(my_dog.species)
my_dog.bark(10)

class Circle():
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius
        #self.area = radius * radius * self.pi
        self.area = radius * radius * Circle.pi
    def get_cirumferance(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)
print(my_circle.get_cirumferance())
print(my_circle.area)
