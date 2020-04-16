list = """
The List is dynamic and tuple has static characteristics.
The tuple is faster than list because of static in nature.

#Difference between lists and tuples.
List are mutable
Tuple are immutable.
List iteration is slower and is time consuming.
Tuple iteration is faster.
List is useful for insertion and deletion operations.
Tuple is useful for read only operations like accessing elements.
List consumes more memory.
Tuples consumes less memory.
List provides many in-built methods.
Tuples have less in-built methods.
List operations are more error prone.
Tuples operations are safe.
"""
print list

#List details
list = ['p','r','o','b','e']
print "List operation are started"
print list
list.append('s')
print list
print list.count('s')
list.extend([2])
print list
list.extend([3,4,5])
print list
print list.index('r')
print list[0]
print list[3]
print list[-2]
list.pop()
print list
list.pop(7)
print list
print list[:]
print list[1:]
print list[:4]
print list[1:5]
list.remove(2)
print list
list.insert(5,'s')
print list
list[5] = 'q'
print list
del list[5]
print list
print "List operation are completed"
print ""

#Tuple details
tuple = ('p','r','o','b','e')
print "Tuple operation are started"
print tuple
print tuple.count('p')
print tuple.index('r')
print "Tuple operation are completed"
