import csv

data = open('sada.csv')
csv_data = csv.reader(data)
date_lines = list(csv_data)
print(date_lines[1][2])

file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a', 'b', 'c'])
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6']])
file_to_output.close()


import PyPDF2

f = open('top-25-python-interview-questions.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(f)
print(pdf_reader.pages)
page_one = pdf_reader.pages[1]
page_one_text = page_one.extract_text()
print(page_one_text)
f.close()

f = open('top-25-python-interview-questions.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
page_one = pdf_reader.pages[1]
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)
pdf_output = open("Brand_New_Doc.pdf", "wb")
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()
