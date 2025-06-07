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

