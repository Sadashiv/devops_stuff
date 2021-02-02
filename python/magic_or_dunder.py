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
        #return '{} {}'.format(e1.first, e1.last)

    def apply_rise(self):
        self.amount =  int(self.amount * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}', '{}'".format(self.first, self.last, self.native, self.amount)

    def __str__(self):
        return "{}, {}".format(self.first, self.last)
    def __add__(self, other):
        return self.amount + other.amount

e1 = Employee('Sadashiv', 'Biadagi', 'Babalad', 1000)
e2 = Employee('Ramesh', 'Badagi', 'Babalad', 1200)

print(e1)
print(repr(e1))
print(str(e1))
print(e1.__repr__())
print(e1.__str__())

print(1+2)
print(int.__add__(1,2))
print(str.__add__('a','b'))
print(e1+e2)
