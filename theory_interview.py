2,3,10,5,6,1
print the right side one greater number.
how to every monthsecond friday for 5hrs

Python runs .pyc file faster than .py
python program checks the timestamp with .py and .pyc
if .py got modified then, compile to bytecode .pyc
instead of module we can import file, but the import will not reload the code modified in other terminal.

Python's import loads a Python module into its own namespace,
import mod
a = mod.method

from loads a Python module into the current namespace,
from mod import *
b = method
help(S.replace)

reverse string
a = 'sada'
b = a[::-1]

raw string
a= open(r'a.txt','r')
r helps to make the path communication for windows and linux

r+
rb+ - open the file for reading and writing at the begining of file.

''.join([`x` for x in xrange(101)])
''.join([`x` for x in xrange(101)])

Note that the (`) is a backquote not a regiular single quote ('), and we can use str(x) instead. Also, since the xrange() is replaced with range in Python 3.x, we should use range() instead for compatibility.

os.path.realpath('path') will give the absloute path exist or not

Dictionaries provide very fast key lookup, unordered set of key value.

differance between dirname and basename, if / there at the will get /home/user

>>> x = 5
>>> while x > 0:
	print('blah!' * x)
	x -= 1

f(*args) => pass n number of arguments or else just call function
f(**args) => The ** is similar but it only works for keyword arguments and 
The keyword arguments is a special name=value 
**args collets and converts as dictionary.

increment or decrement the arguments by using the **args

lambda => function doen't have return statement and looping compare to normal function.

lambda's body is a single expression, 
def f(x, y, z): return x + y + z
f = lambda x, y, z: x + y + z
The map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object and returns a list containing all the function call results
>>> a = map(lambda x:x+1, [5])
>>> b = reduce(lambda x:x+1, [5])
>>> c = filter(lambda x:x+1, [5])
>>> print a,b,c
[6] 5 [5]

b = list(filter(lambda x:x<0,range(-5,5)))

"Decoration is a way to specify management code for functions and classes." ... 
Decorators allow you to inject or modify code in functions or classes. Sounds a bit like Aspect-Oriented Programming (AOP)

@myDecorator
def aFunction():
    print "inside aFunction"
When the compiler passes over this code, aFunction() is compiled and the resulting function object is passed to the myDecorator code, which does something to produce a function-like object that is then substituted for the original aFunction().

class myDecorator(object):

    def __init__(self, f):
        print "inside myDecorator.__init__()"
        f() # Prove that function definition has completed

    def __call__(self):
        print "inside myDecorator.__call__()"

@myDecorator
def aFunction():
    print "inside aFunction()"

print "Finished decorating aFunction()"

aFunction()
When you run this code, you see:

inside myDecorator.__init__()
inside aFunction()
Finished decorating aFunction()
inside myDecorator.__call__()

def foo(): pass
foo = staticmethod(foo)
With the addition of the @ decoration operator, you now get the same result by saying:

@staticmethod
def foo(): pass


class entryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__

@entryExit
def func1():
    print "inside func1()"

@entryExit
def func2():
    print "inside func2()"

func1()
func2()
The output is:

Entering func1
inside func1()
Exited func1
Entering func2
inside func2()
Exited func2

When to use list comphrehension

The map calls are roughly twice as fast as equivalent for loops. List comprehensions are usually slightly faster than map calls. This speed difference is largely due to the fact that map and list comprehensions run at C language speed inside the interpreter.

[X**2 for x in range(10)]

Set
unodered one,set.update(muiltiple) set.add('1')
union and intersection

>>> from sets import Set
>>> a =set([1,2])
>>> b = Set([2,3])
>>> a =Set([1,2])
>>> c = a | b
>>> c
Set([1, 2, 3])
>>> a & b
Set([2])


Dictionary in python is implemented using the hash
>>> keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>> hash = {k:v for k, v in zip(keys, values)}
>>> hash
{'a': 1, 'c': 3, 'b': 2}



 

i
def func():
   print "func()"

funcObj = func
funcObj()

def count(f):
    def inner(*args, **kargs):
        inner.counter += 1
        return f(*args, **kargs)
    inner.counter = 0
    return inner

@count
def my_fnc():
    pass

if __name__ == '__main__':
    my_fnc()
    my_fnc()
    my_fnc()

    print 'my_fnc.counter=',my_fnc.counter
==>3
when we call the my_fnc it's get called the count function



>>> for i, season in enumerate(['Spring', 'Summer', 'Fall', 'Winter']):
...     print(i, season)

List comprehension

>>> words = 'The quick brown fox jumps over the lazy dog'.split()
>>> print words
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
>>> 
>>> stuff = [[w.upper(), w.lower(), len(w)] for w in words]
printing {x2:x in (0...10)

os.path.dirname(os.getcwd())
'/home'
>>> os.path.basename(os.getcwd())
'user'
>>> 

for dirpath,dirs,files in os.walk(os.getcwd()):
print basedir, dirs=>print nested folders files=> print all the files


glob.glob(os.path.join(os.getcwd(), '*.py'))
subprocess.call()
Setting the shell argument to a true value causes subprocess to spawn an intermediate shell process, and tell it to run the command,
 command will be executed erlier checking for the shell

Unpacking sequence into seprate varibales.
c = (1,2,3,4)
q,w,e,r = c
print q, w, e, r

Unpacking actually works with any object that happens to be iterable, not just tuples or
lists. This includes strings, files, iterators, and generators. 
s = 'Hello'
d,f,g,hj,l = s
print  d,f,g,hj,l

Unpacking the elements from interables of Arbitary Length
details = ('Sadashiv,'Badagi', '99014979776','9538253250')
name,surname,*mobile_no = details #Python3

_ to skip the unpacking.

>>> from collections import deque
>>> a = deque(maxlen=3)
>>> q = deque(maxlen=3)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3], maxlen=3)
>>> q.append(4)
>>> q
deque([2, 3, 4], maxlen=3)
dir(q)
We can use list but using deque is for more elegent and runs a lot faster.

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
heap = list(nums)
heapq.heapify(heap)
The most important feature of a heap is that heap[0] is always the smallest item and runs faster.
heapq.heappop(heap) --> pop smallest item from heapq

page:27


get current user home directory ==> os.path.expanduser('~')

range => returns an list
xrange => returns and iterator light weight and faster.


>>> for x in range(5):
...  print x**3
... 
0
1
8
27
64
>>> [ x**3 for x in range(5)]
[0, 1, 8, 27, 64]


>>> # Generator expression makes an iterable
>>> (x ** 3 for x in range(5))
<generator object <genexpr> at 0x000000000315F678>
With the generator expression, to make list comprehension, we can just wrap it with list() call:

>>> list(x ** 3 for x in range(5))
[0, 1, 8, 27, 64]


Monkey patching - runtime editing the code
We have a module called m.py like this:

# m.py
class MyClass:
    def f(self):
        print "f()"
Then, if we run the monkey-patch testing like this:

>>> import m
>>> def monkey_f(self):
	print "monkey_f()"

	
>>> m.MyClass.f = monkey_f
>>> obj = m.MyClass()
>>> obj.f()
monkey_f()

>>> dup_list = [1,2,3,4,4,4,5,1,2,7,8,8,10]
>>> unique_list = list(set(dup_list))
>>> print unique_list
[1, 2, 3, 4, 5, 7, 8, 10]


Name the functional approach that Python is taking.
Python provides the following:

map(aFunction, aSequence)
filter(aFunction, aSequence)
reduce(aFunction, aSequence)
lambda
list comprehension


Passing the n number of arguments

>> def print_all(*args):
	for x in enumerate(args):
		print x
		
>>> print_all('A','b','b','a')
(0, 'A')
(1, 'b')
(2, 'b')
(3, 'a')
>>> 
The keyword arguments is a special name=value syntax in function calls that specifies passing by name. It is often used to provide configuration options.

>>> def kargs_function(**kargs):
	for k,v in kargs.items():
		print (k,v)

>>> kargs_function(**{'uno':'one','dos':'two','tres':'three'})
('dos', 'two')
('tres', 'three')
('uno', 'one')
>>>
>>> kargs_function(dos='two', tres='three', uno='one')
('dos', 'two')
('tres', 'three')
('uno', 'one')

Iterators in Python are used to iterate over a group of elements, containers, like list. For a container to support iterator, it must provide __iter__().

1. iterator.__iter__() :
    It returns the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements.

2. iterator.__next__() :
    It returns the next item from the container. If there are no further items, raise the StopIteration exception.

Generators are way of implementing iterators. Generator function is a normal function except that it contains yield expression in the function definition making it a generator function. This function returns a generator iterator known as generator.

http://www.questionscompiled.com/python-interview-questions.html

Slicing in Python is a mechanism to select a range of items from Sequence types like strings, list, tuple, etc. 


If the base class is present in other module, the syntax for derivation changes to:

class DeriveClass( module.BaseClass):

http://career.guru99.com/top-25-python-interview-questions/


What are the tools that help to find bugs or perform static analysis?

PyChecker is a static analysis tool that detects the bugs in Python source code and warns about the style and complexity of the bug. Pylint is another tool that verifies whether the module meets the coding standard.

What are Python decorators?

A Python decorator is a specific change that we make in Python syntax to alter functions easily.

pass by value -> point to the different refrance in memory
pass by refrance => point ot the same refrance


What is namespace in Python?

In Python, every name introduced has a place where it lives and can be hooked for. This is known as namespace. It is like a box where a variable name is mapped to the object placed.  Whenever the variable is searched out, this box will be searched, to get corresponding object.

with used in python clean.
with open('filename', 'mode') as f:
    f.readlines()
    f.read()


with open('filename', 'mode') as f:
try:
   do some operation
finally:
   failure operation

The yield enables a function to comeback where it left off when it is called again. This is the critical difference from a regular function. A regular function cannot comes back where it left off. The yield keyword helps a function to remember its state.

def foo_with_yield():
    yield 1
    yield 2
    yield 3

# iterative calls
for yield_value in foo_with_yield():
    print yield_value,

def foo_with_yield():
    yield 1
    yield 2
    yield 3

x=foo_with_yield()
print x
print next(x)
print x
print next(x)
print x
print next(x)

In short, a generator looks like a function but behaves like an iterator.

The primary difference between generator and normal functions is that a generator yields a value, rather than returns a value. The yield suspends the function and sends a value back to the caller while retains enough state to enable the function immediately after the last yield run.

Genrators executes faster

>>> # Fibonacci version 2
>>> def fibonacci(max):
    a, b = 0, 1            (1)
    while a < max:
        yield a            (2)
        a, b = b, a + b    (3) 

>>> for n in fibonacci(500):
	print(n, end=' ')

Generator expressions are a memory-space optimization. They do not require the entire result list to be constructed all at once while the square-bracketed list comprehension does. They may also run slightly slower in practice, so they are probably best used only for very large result sets.


Generator: Functions vs. Expressions
Function
>>> G = (c * 5 for c in 'Python')
>>> list(G)
['PPPPP', 'yyyyy', 'ttttt', 'hhhhh', 'ooooo', 'nnnnn']

Expression
>>> def repeat5times(x):
	for c in x:
		yield c * 5

		
>>> G = repeat5times('Python')
>>> list(G)
['PPPPP', 'yyyyy', 'ttttt', 'hhhhh', 'ooooo', 'nnnnn']
>>> 
