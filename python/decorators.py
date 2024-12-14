class Employee(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last

    #@property will make method as attribute to access
    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        #return '{} {}'.format(dev1.first, e1.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleted name!")
        self.first = None
        self.last = None

emp_1 = Employee('Sadashiv', 'Badagi')

emp_1.fullname = 'Ramesh Badagi'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)

def hello():
    return "Hello!"

greet = hello
print(greet())
print(hello())
del hello
print(greet())
#print(hello())

def main(name="Sadashiv"):
    print("The main() function has been executed")
    def welcome():
        return "\t This is the welcome() function inside main"
    def greet():
        return "\t This is the greet() function inside main "
    #print(welcome())
    #print(greet())
    #print("This is the end of greet function")
    print("Hi, i am going to return function")
    if name == 'Sadashiv':
        return greet
    else:
        return welcome

mynewfunc = main("Sadashiv")
print(mynewfunc())

def cool():

    def super_cool():
        return "I am super cool!"
    return super_cool
some_func = cool()
print(some_func)
print(some_func())


def hello():
    return "Hello Sadahsiv!"

def greet_person(some_other_func):
    print("Other code runs here!")
    print(some_other_func())

print(greet_person(hello))

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code before the original function")
        original_func()
        print("Some extra code after the original function")

    return wrap_func


def func_needs_decorator():
    print("I want to be decorated")

decorated_func = new_decorator(func_needs_decorator)
print(decorated_func())

@new_decorator
def func_needs_decorator_at():
    print("I want to be decorated")

print(func_needs_decorator_at())

