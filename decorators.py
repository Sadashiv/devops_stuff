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
