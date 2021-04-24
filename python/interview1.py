import os
"""List of interview questions:
============================
"""
"""Print square root of a number without using built in function
Ex: (2)**1/2
"""
for sq in range(5):
 sqs = sq**(0.5)
 print(sqs)

"""Sort out the dictionary with key and value"""
dct = {"z":1, "b":3, "1":2}
for keyshort in sorted(dct.keys()):
 print(keyshort)

for valuesort in sorted(dct.values()):
 print(valuesort)

#Dunder/Magic methods
#Binary operators
"""
+  object.__add__(self, other)
-  object.__sub__(self, other)
*  object.__mul__(self, other)
// object.__floordiv__(self, other)
"""

#Extended assignments
"""
+= object.__iadd__(self, other)
-= object.__isub__(self, other)
*= object.__imul__(self, other)
/= object.__idiv__(self, other)
"""

#Unary operators
"""
-       object.__neg__(self)
+       object.__pos__(self)
abs()   object.__abs__(self)
"""

#Comparison operators
"""
<   object.__lt__(self, other)
<=  object.__le__(self, other)
==  object.__eq__(self, other)
"""

#Convert python 2 code to 3
print("Convert code from python 2 to 3")
print("2to3-2.7 interview.py")
print("2to3-2.7 -w interview.py")
print("2to3-2.7 python/interview.py -w python/")
#file or folder conversion
print("__cmp__ method no more exist in python3 ")

print("\nPython is dynamically type language Ex: a=10, name='Sadashiv'")
print("Python is strongly typed as the interpreter keeps track of all variables types.\
        It's also very dynamic as it rarely uses what it knows to limit variable usage.\
        In Python, it's the program's responsibility to use built-in functions like\
        isinstance() and issubclass() to test variable types and correct usage")

print("\What is in ORM ?")
print("\n-->Django ORM provides an elegant and powerful way to interact with the database.\
         ORM stands for Object Relational Mapper. It is just a fancy word describing how\
         to access the data stored in the database in Object Oriented fashion.\
         Databases records into objects execute common queries not replace SQL")


print("High order functions ?")
print("-->Functions that take a function as an argument or return a function.")
print("map, fiter and reduce are the high level finctions")
def add(x,y):
    return x + y

#reduce(add, [1,2,3,4])

def greater_than_5(x):
    return x > 5

script_path = os.path.dirname(os.path.abspath( __file__ ))
print(script_path)
#filter(greater_than_5, range[10])
fr = open('%s/class.py' %script_path, 'r')
fw = fr.readlines()
fr.close()
fa = open('../class.py', 'a')
for k in fw:
    if 'add' in k:
        fa.write(k.replace('add', 'kkkk'))
fa.close()

#Find upper, lower and space count in give string
var="Sun RISES in the morning"
lower_char = 0
upper_char = 0
for char in var:
    if char.islower():
        lower_char += 1
    elif char.isupper():
        upper_char += 1

print("Total upper charters: ", upper_char)
print("Total lower charters: ", lower_char)
print("Total space: ", len(var.split(" ")) - 1)

#Find upper, lower and space count in give string without using inbuilt function
def upperlower(var):
    upper = 0
    lower = 0
    space = 0
    for char in var:
        if (ord(str(char)) >= 97 and ord(str(char)) <= 122):
            lower += 1
        elif (ord(str(char)) >= 65 and ord(str(char)) <= 90):
            upper += 1
        elif char.isspace():
            space += 1
    print('Total upper charters: %s' %upper,
          'Total lower charters: %s' %lower,
          'Total space in a given string: %s' %space)

upperlower(var)
#Count the length of string
var_num="0123456789"
num_count = 0
for num in var_num:
    num_count += 1

print("Total count/length of:", var_num, num_count)

#>>> var_num=01234567

#>>> var_num=012345678
#  File "<stdin>", line 1
#    var_num=012345678

numvar=01234567
print("Input of num: %s and ouput of string is: %s " %(numvar, str(numvar)))


count = 0
number = 12345678
while (number > 0):
    print("Original number: %s" %number)
    number = number//10
    print("After the number//10: %s" %number)
    count = count + 1
print("Total count/length of give number: %s" %count)
