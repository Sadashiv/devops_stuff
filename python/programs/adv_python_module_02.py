import math
print(dir(math))
value = 4.35
print(math.ceil(value))
print(round(4.5)) #number is even then it will print float first even number
print(round(5.5)) #number is odd then it print the odd number
from math import pi

print(pi)
print(math.pi)
#numpy
print(math.e)
print(math.sin(100))
print(math.degrees(pi/2))
print(math.radians(180))

import random
print(random.randint(0,100))

print(random.seed(101))
print(random.randint(0, 100))
print(random.choice(range(0,20)))
print(random.choices(population = range(0,20), k=10))
print(random.sample(population = range(0,20), k=10))
mylist = list(range(0, 30))
print(mylist)
print(random.shuffle(mylist))

print(random.uniform(a=0, b=100))
print(random.gauss(mu=0, sigma=1))

sent = "my phone number is 9538253250"
print('phone' in sent)
import re
pattern = 'phone'
match  = re.search(pattern, sent)
print(match)
print(match.span())

sent = "my phone is, my phone is"
print(re.findall('phone', sent))
for match in re.finditer('phone', sent):
    print(match.span())


sent = "my phone number is 9538253250"
phone = re.search('9538253250', sent)
print(phone)
phone = re.search(r"\d\d\d\d\d\d\d\d\d\d", sent)
print(phone)
print(phone.group())
# * occurs zero or more time
# ? one or none
phone = re.search(r"\d{10}", sent)
print(phone.group())
print(re.compile(r"(123)-(456)-(7890)"))
results = re.search(phone.group(), sent)
print(results.group())
print(results.group()[0])
#qualifiers d w s, D W S

print(re.search(r"cat|dog", "the cat is here"))
print(re.findall(r"at", "the cat in the hat went in splat"))
print(re.findall(r".at", "the cat in the hat went in splat"))
print(re.findall(r"...at", "the cat in the hat went in splat"))

print(re.findall(r"^\d", "1 is a number"))
print(re.findall(r"$\d", "number is 2"))
