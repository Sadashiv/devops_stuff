"""List of interview questions:
============================
"""
"""Print squarute of a number without using built in function
Ex: (2)**1/2
"""
for sq in range(10):
 sqs = sq**(0.5)
 print sqs

"""Sort out the dictionary with key and value"""
dct = {"z":1, "b":3, "1":2}
for keyshort in sorted(dct.iterkeys()):
 print keyshort

for valuesort in sorted(dct.itervalues()):
 print valuesort

