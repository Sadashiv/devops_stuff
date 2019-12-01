import collections
import copy
#Reverse a list using reverse method
lst=[1,2,3,4]
lst.reverse()
print(lst)
for i in reversed(lst):
    print(i)
#print("Reverse of list using the reverse method: " a.reverse())

#Removing the duplicate elements from list
dup_list = [1,2,3,4,4,4,5,1,2,7,8,8,10]
unique_list = list(set(dup_list))
print(unique_list)

#Immutable/Hashable -> Floats, Integers, tuples, strings anf frozenset
#mutable/Non-Hashable -> Dictionaries, sets, lists
# Check if a float is hashable
print(isinstance(0.125, collections.Hashable))


lsts = [1,2,3,10,5,6,7,8,9]
lsts.sort(reverse=True)
print(lsts)
print(lsts[:10])
print(lsts[1:])
print(lsts[1:10:2])
print(len(lsts))

print(lsts.__iter__)
lsts.append([100,101]) #append method will take it as single object and put it in the list
print(lsts)
lst.extend([100,101]) #Extend adds each element of iterable to the list one at a time method take it as list,tuple, dict or string
print(lst)
lst.insert(0, lsts) #Insert at particular place
print(lst)

#Copy list
newlst = lst[:]
print(newlst)
newlst=copy.copy(lst)
print(newlst)
#if your list contains objects and you want to copy those as well, you can use
newlst=copy.deepcopy(lst)
print(newlst)
newlst=copy.deepcopy(lst)
print(newlst)

#List comprehension is, basically speaking, a way of elegantly constructing your lists.
[print(i*i) for i in range(10)]
[print(i*i) for i in range(10) if i%2==0]
print(lst, lst.count('100'))

#Split python into evenly sized chunks
y=zip(*[iter(lst)]*4)
print(list(y))

#Sum a lists
list1=[1, 2, 3]
list2=[4, 5, 6]
from operator import add
print(list(map(add, list1, list2)))

#Create flat list out of lists
# Your initial list of lists
list = [[1,2],[3,4],[5,6]]

# Flatten out your original list of lists with `sum()`
print(sum(list, []))

name = ['Sada', 'Badagai', 'Babalad']

name_sorted = sorted(name)
print(name_sorted)
print(name.index('Sada'))
print('Sada' in name)
for index, details in enumerate(name): #start position can be set enumerate(name, start=1)
    print(index, details)

print(','.join(name))
print(' - '.join(name))
print(' - '.join(name).split('- '))

#Mutable
name2 = name
print(name)
print(name2)

name[0] = 'Ramesh'
print(name)
print(name2)

#Immutable
tup1 = ('Sada', 'Badagai', 'Babalad')
tup2 = tup1
print(tup1)
print(tup2)
#tup1[0] = 'Ramesh'
#print(tup1)
#print(tup2)

#sets are unordered
name_set = {'Sada', 'Badagai', 'Babalad'}
print(name_set)
name_set = {'Sada', 'Badagai', 'Babalad', 'Sada'}
print(name_set)
empty_set = {}
print(type(empty_set))
empty_set = set({})
empty_set = set()
print(type(empty_set))


name1_set = {'Sada', 'Badagai', 'Babalad'}
name2_set = {'Ramesh', 'Badagai', 'Babalad'}
print(name1_set.intersection(name2_set))
print(name1_set.difference(name2_set))
print(name1_set.union(name2_set))
