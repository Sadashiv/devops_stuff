#Given string print even string which has highest even string
initial = 0
get_even = {}
test = "Timellll to write great codell"
def get_even_largest_string():
    for kk in test.split(' '):
        if len(kk)%2 == 0:
            initial = len(kk)
            get_even[initial]=kk
    print(get_even)
    key_lst=sorted(get_even.values(), reverse=True)[-1]
    print(key_lst)
    #values_lst=get_even.values()
    #get_key=sorted(key_lst)[-1]
    #get_value=sorted(values_lst)
    #print(get_key)
    if key_lst == 0:
        return None
    else:
        print("Get the even largest string: %s" %key_lst)
get_value = get_even_largest_string()
#print(get_value)

initial = 0
get_even = {}
test = "Timellll to write great codell"
for kk in test.split(' '):
    if len(kk)%2 == 0:
        initial = len(kk)
        get_even[initial]=kk
print(get_even)
lst=get_even.keys()
lst.sort()
#print(lst)
get_key = lst[-1]
print(get_even.get(get_key))
