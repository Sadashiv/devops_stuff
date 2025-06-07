def sada(n):
    for i in range(n):
        print(i**2)

sada(10)
[print(x**2) for x in range(10)]
[print(x) for x in range(10) if x%2 == 0 ]
[print(x**2) for x in range(10) if x%2 == 0 ]
[print(x**2) for x in range(10) if x%2 != 0 ]

coordinates = []
for x in range(3):
    for y in range(3):
        coordinates.append((x, y))
print(coordinates)

lcoord = [(x,y) for x in range(3) for y in range(3)]
print(lcoord)

lc = [f"Even number: {x}" if x%2==0  else f"Odd number: {x}" for x in range(10)]
print(lc)
