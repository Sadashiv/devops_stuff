class Employee(object):
    raise_amount = 1.04
    num_of_emp = 0
    def __init__(self, first, last, native, amount):
        self.first = first
        self.last = last
        self.native = native
        self.amount = amount
        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        #return '{} {}'.format(dev1.first, e1.last)

    def apply_rise(self):
        self.amount =  int(self.amount * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, native, amount, prog_lang):
        super().__init__(first, last, native, amount)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, native, amount, employees=None):
        super().__init__(first, last, native, amount)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def display_emps(self):
        for emp in self.employees:
            print("--->", emp.fullname())

dev_1 = Developer('Sadashiv', 'Badagi', 'Babalad', 1000, 'Python')
dev_2 = Developer('Ramesh', 'Badagi', 'Babalad', 1200, 'Java')

mgr_1 = Manager('Gangadhar', 'Badagi', 'Babalad', 2000, [dev_1])
print(dev_1.first)
print(dev_2.prog_lang)
#print(help(Developer))
print(dev_1.amount)
dev_1.apply_rise()
print(dev_1.amount)

print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Manager))
print("Manager details")
print(mgr_1.first)
mgr_1.add_emp(dev_1)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)
mgr_1.display_emps()

print("\n---> Inheritance for Animal  class example")
class Animal():
    def __init__(self):
        print("Animal created")
    def who_am_i(self):
        print("I am animal")
    def eat(self):
        print("I am eating")

myanimal = Animal()
print(myanimal)

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    #override older method
    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print("Bow bow!")
mydog = Dog()
print(mydog)
mydog.who_am_i()
mydog.bark()

class Dogs():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} speaks bow bow"
class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name } speaks meow meow"

dogs = Dogs('Mudhol Huland')
cat = Cat('Mudhol Felix')
print(dogs.speak())
print(cat.speak())
for pet in [dogs,cat]:
    print(type(pet))
    print(type(pet.speak()), pet.speak() )

def pet_speak(pet):
    print(pet.speak())
pet_speak(dogs)
pet_speak(cat)
