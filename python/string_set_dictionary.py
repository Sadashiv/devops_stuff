string = """ 
Strings are arrays of bytes representing Unicode characters.
Strings are immutable.
"""
print string

#String Operations details
str = "Hello Python"
str1 = "World"
print "String operations are started"
print str.capitalize()
print str.center(20)
print str.count('o')
print str.decode()
print str.encode()
print str.endswith('Python')
print str.expandtabs(12)
print str.find('P')
print str.format()
print str.index('y')
print str.isalnum()
print str.isalpha()
print str.isdigit()
print str.islower()
print str.isspace()
print str.istitle()
print str.isupper()
print str.lower()
print str.ljust(5)
print str.lstrip()
print str.partition('P')
print str.rfind('o')
print str.replace('o','r')
print str.rindex('o')
print str.rjust(20)
print str.rpartition('P')
print str.rsplit('P')
print str.rstrip('P')
print str.split('P')
print str.splitlines()
print str.startswith('Hello')
print str.strip()
print str.swapcase()
print str.title()
print str.upper()
print str.zfill(20)
print str.join(str1)
print str[0]
print str[6]
print str[-1]
print str[:]
print str[2:]
print str[:6]
print str[2:7]
print str[2:-2]
print "String operations are completed"
print ""
print "Sets details are started from here"
set_1 = """
A set is an unordered collection of items.
Every element is unique and must be immutable.
"""
print set_1 

#set Operations details
print "Sets operations are started"
s = {1,2,3,4,3,2}
print s
set1 = {1,3}
set1.add(2)
print set1
set1.update([2,3,4])
print set1
set1.update([4,5], {1,6,8})
print set1
set1.discard(6)
print set1
set1.remove(8)
print set1
set2 = {"HelloWorld"}
print set2
set2.clear()
print set2 
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A|B)
print(A.union(B))
print(B.union(A))
print(A&B)
print(A.intersection(B))
print(B.intersection(A))
print(A-B)
print(B-A)
print(A.difference(B))
print(B.difference(A))
print(A^B)
print(B^A)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
print "Sets operations are completed"
print ""
print "Dictionary details are started from here"
Dictionary = """
Python dictionary is an unordered collection of items.
a dictionary has a key:value pair.
"""
print Dictionary

#Dictionary Operations details
print "Dictionary operations are started"
dict = {'name':'Ramesh', 'age':28}
print dict.copy()
print dict.fromkeys('name')
print dict.fromkeys('age')
print dict.fromkeys('name','age')
print dict.get('name')
print dict.has_key('name')
print dict.has_key('Ramesh')
print dict.items()
for i in dict.iteritems():
    print i
for i in dict.iterkeys():
    print i
for i in dict.itervalues():
    print i
print dict.keys()
print dict.values()
print dict.viewitems()
print dict.viewkeys()
print dict.viewvalues()
dict['name'] = 'Ram'
print dict
dict['age'] = 29
print dict
dict['address'] = 'Bijapur'
print dict
dict1 = {1:1, 2:4, 3:9, 4:16, 5:25}
print dict1.pop(4)
print dict1.popitem()
print dict1[5]
print dict1.clear()
print "Dictionary operations are completed"