"""
What are generators in Python?

There is a lot of overhead in building an iterator in Python; we have to implement a class with __iter__() and __next__() method,
keep track of internal states, raise StopIteration when there was no values to be returned etc.

This is both lengthy and counter intuitive. Generator comes into rescue in such situations.

Python generators are a simple way of creating iterators. All the overhead we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
Iterators in Python are used to iterate over a group of elements, containers, like list. For a container to support iterator,
it must provide __iter_#

1. iterator.__iter__() :
    It returns the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements.

2. iterator.__next__() :
    It returns the next item from the container. If there are no further items, raise the StopIteration exception.

Generators are way of implementing iterators. Generator function is a normal function except that it contains yield
expression in the function definition making it a generator function. This function returns a generator iterator known as generator.
"""

"""
How to create a generator in Python?
It is fairly simple to create a generator in Python. It is as easy as defining a normal function with yield statement
instead of a return statement.

If a function contains at least one yield statement (it may contain other yield or return statements),
it becomes a generator function. Both yield and return will return some value from a function.

The difference is that, while a return statement terminates a function entirely, yield statement pauses the function
saving all its states and later continues from there on successive calls.
"""

def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a=my_gen()
next(a)
next(a)
next(a)
#next(a)

# Using for loop
#for item in my_gen():
#    print(item)
"""
One interesting thing to note in the above example is that, the value of variable n is remembered between each call.

Unlike normal functions, the local variables are not destroyed when the function yields. Furthermore,
the generator object can be iterated only once.

To restart the process we need to create another generator object using something like a = my_gen().
"""

"""
Why generators are used in Python?
There are several reasons which make generators an attractive implementation to go for.

1. Easy to Implement
Generators can be implemented in a clear and concise way as compared to their iterator class counterpart.
Following is an example to implement a sequence of power of 2's using iterator class.
"""
class PowTwo:
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n += 1
        return result
#This was lengthy. Now lets do the same using a generator function.

def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
#Since, generators keep track of details automatically, it was concise and much cleaner in implementation.

"""
2. Memory Efficient
A normal function to return a sequence will create the entire sequence in memory before returning the result.
This is an overkill if the number of items in the sequence is very large.

Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time.
"""

"""
Python Generator Expression
Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.

Same as lambda function creates an anonymous function, generator expression creates an anonymous generator function.

The syntax for generator expression is similar to that of a list comprehension in Python.
But the square brackets are replaced with round parentheses.

The major difference between a list comprehension and a generator expression is that while list comprehension
produces the entire list, generator expression produces one item at a time.

They are kind of lazy, producing items only when asked for. For this reason, a generator expression is much more memory efficient
than an equivalent list comprehension.

"""
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
(x**2 for x in my_list)


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10)) #This stores in the memory

def create_cubes_with_yield(n):
    for x in range(n):
        yield x**3
for kk in create_cubes_with_yield(10):
    print(kk)
print(list(create_cubes_with_yield(10)))

def gen_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b

for number in gen_fibonacci(10):
    print(number)

def simple_gen():
    for i in range(3):
        yield i
for num in simple_gen():
    print(num)
g = simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
#print(next(g))

name="Sadashiv"
#print(next(name))

s_iter = iter(name)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
