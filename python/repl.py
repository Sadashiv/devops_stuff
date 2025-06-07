fr = open('class.py', 'r')
fw = fr.readlines()
fr.close()
fa = open('class.py', 'a')
for k in fw:
    if 'add' in k:
        fa.write(k.replace('add', 'kkkk'))
fa.close()
