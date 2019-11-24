class Employee(object):
    pass

e1 = Employee()
e2 = Employee()
print(e1, e2)

e1.first = 'Sadashiv'
e1.last = 'Badagi'
e1.native = 'Babalad'
print(e1.first, e1.last, e1.native)

#self.first = e1.first are equilent

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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #Alternative to constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, native, amount = emp_str.split('-')
        return cls(first, last, native, amount)

    #Staticmethod doesn't take class or instant as argument is similar to normal function
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

e1 = Employee('Sadashiv', 'Biadagi', 'Babalad', 1000)
e2 = Employee('Ramesh', 'Badagi', 'Babalad', 1200)
#print(e1.fullname())
#print(e2.fullname())
e1.fullname()
print(Employee.fullname(e1))
#e.fullname() will be passed as Employee.fullname(e1)
print("*"*50)
print(e1.raise_amount)
print(e1.amount)
e1.apply_rise()
print(e1.amount)
print(e1.__dict__)
print(Employee.__dict__)
#Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)
print(Employee.num_of_emp)
Employee.set_raise_amount(1.06)
print(Employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)
e1.set_raise_amount(1.07)
print(Employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)

#
emp_str_1 = 'Sadashiv-Badagi-Babalad-70000'
first, last, native, amount = emp_str_1.split('-')
new_emp_1 = Employee(first, last, native, amount)
print(new_emp_1.first)
print(new_emp_1.last)

#Alternative constructor
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.native)

import datetime
my_date = datetime.date(2019, 11, 24)

print(Employee.is_workday(my_date))
