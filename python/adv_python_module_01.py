from collections import Counter

coll = [1,1,1,1,1,2,2,2,2,2,2,2,2,'s','s','s','s','s']
print(Counter(coll))
print(type(Counter(coll)))
print(Counter(coll)[1])

sent = "Hello Sadashiv how are you you are"
print(Counter(sent))
print(Counter(sent.upper().split()))

letters = "aaaaaaaaaaaabbbbbbbbbbbbbbbbccccccccccccccccccdddddddddddddddddddddddddddddddddd"
c = Counter(letters)
print(dir(c))
print(c.most_common())
print(c.most_common(2))
print(c)
print(list(c))

from collections import defaultdict
a = {'name': 'Sadashiv'}
print(a['name'])
#print(a['surname']) Normal dicctionary throws error,
#defaultdict will not throws error by assigning the value
d = defaultdict(lambda: 'defaultvalue')
d['surname'] = 'Badagi'

print(d['surname'])

print(d['some key'])
print(d)

print("-------------------nametuple-----------------")
mytuple = (1,2,3)
print(mytuple[0])

from collections import namedtuple
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
mudhol = Dog(age=5, breed="Mudhol Breed", name='Mudhol Dog')

print(mudhol) #similar to normal tuple but it's named here
print(type(mudhol))

print(mudhol[0], mudhol.name)

import datetime
print(datetime.time())
mytime = datetime.time(13,1,2,3) #hour minute seconds micorseconds
print(mytime.hour)
today = datetime.date.today()
print(today)
print(today.year, today.month, today.day)

print(today.ctime())
from datetime import datetime
mydatetime = datetime(2024,12, 15, 14, 20, 1)
print(mydatetime)
mydatetime = mydatetime.replace(year=2025)
print(mydatetime)

from datetime import date
date1 = date(2025, 12, 15)
date2 = date(2024, 12, 14)
result = date1 - date2
print(result.days)

datetime1 = datetime(2025, 12, 15, 22, 14, 59)
datetime2 = datetime(2024, 12, 15, 12, 10, 59)

resultdt = datetime1 - datetime2
print(resultdt)


