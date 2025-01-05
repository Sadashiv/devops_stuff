import time

n = 1000000
def outer_dec(fun):
    def inner_dec():
        print("before the decorator")
        start_time = time.time()
        fun()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        print("after the decorator")
    return inner_dec

@outer_dec
def fun_one():
    return [str(num) for num in range(n)]

print(fun_one())

def fun_two():
    return list(map(str, range(n)))
print(fun_two())

import timeit
stmt = '''
fun_two(100)
'''

setup = '''
def fun_two(n):
    return list(map(str, range(n)))
'''
print(timeit.timeit(stmt, setup, number=10))

fr = open('fileone.txt', 'w')
fr.write("FILE ONE")
fr.close()
fr = open('filetwo.txt', 'w')
fr.write("FILE TWO")
fr.close()

import zipfile

comp_file = zipfile.ZipFile('compressed.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('compressed.zip', 'r')
zip_obj.extractall('extracted_content')
#shutil.make_archive
#shutil.unpack_archive

