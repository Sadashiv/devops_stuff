n=12345

def countDigit(n):
    count = 0
    while n != 0:
        print(n)
        n //= 10
        count +=1
    return count
#    for i in n:
#        print(i)

print(countDigit(n))

