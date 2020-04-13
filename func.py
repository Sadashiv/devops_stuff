x = 'global x'

def local_global():
#    global x
    x = 'local x'
    print(x)
    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)

local_global()
print(x)
