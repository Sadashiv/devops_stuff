student = {"name": 'Sadashiv', 'surname': "Badagi", 'Details':['Babalad', 'Vijayapur']}
student['dist'] = 'Vijayapur'
student['name'] = 'Sada'
print(student)
print(student.get('name'))
student.update({'name': 'Ramesh'})
details = student.pop('surname')
print('{} Student details'.format(details))
del student['Details']
print(student)
print(student.get('name'))
print(student.get('surname', 'Not found'))
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, value)
