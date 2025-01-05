def myfunc(*args):
    print(args)

myfunc(1)
myfunc(1,2,3,4)

def myfunkwargs(**kwargs):
    print(kwargs)
    print(kwargs['fruit'])
    print(kwargs['leaf'])

myfunkwargs(fruit='apple', leaf="spinch")
