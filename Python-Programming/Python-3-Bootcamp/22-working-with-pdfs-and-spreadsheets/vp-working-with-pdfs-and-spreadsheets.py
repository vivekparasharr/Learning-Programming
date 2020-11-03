# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 18:45:26 2020

@author: vivek
"""

# working with pdfs and spreadsheets

# reading csv

import csv
data = open('example.csv')
csv_data = csv.reader(data)
data_lines = list(csv_data)

data = open('example.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

data_lines[:2] # show first three rows of data (first row has column names)
'''
[['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city'],
 ['1',
  'Joseph',
  'Zaniolini',
  'jzaniolini0@simplemachines.org',
  'Male',
  '163.168.68.132',
  'Pedro Leopoldo']]
'''

# Let's format our printing just a bit
for line in data_lines[:5]:
    print(line)
'''
['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']
['1', 'Joseph', 'Zaniolini', 'jzaniolini0@simplemachines.org', 'Male', '163.168.68.132', 'Pedro Leopoldo']
['2', 'Freida', 'Drillingcourt', 'fdrillingcourt1@umich.edu', 'Female', '97.212.102.79', 'Buri']
['3', 'Nanni', 'Herity', 'nherity2@statcounter.com', 'Female', '145.151.178.98', 'Claver']
['4', 'Orazio', 'Frayling', 'ofrayling3@economist.com', 'Male', '25.199.143.143', 'Kungur']
'''

# Let's imagine we wanted a list of all the emails
all_emails = []
for line in data_lines[1:15]: # we only get first 15 emails
    all_emails.append(line[3])
'''
['jzaniolini0@simplemachines.org', 'fdrillingcourt1@umich.edu', 'nherity2@statcounter.com', 'ofrayling3@economist.com', 'jmurrison4@cbslocal.com', 'lgamet5@list-manage.com', 'dhowatt6@amazon.com', 'kherion7@amazon.com', 'chedworth8@china.com.cn', 'hgasquoine9@google.ru', 'ftarra@shareasale.com', 'abathb@umn.edu', 'lchastangc@goo.gl', 'cceried@yale.edu']
'''

# What if we wanted a list of full names?
full_names = []

for line in data_lines[1:15]:
    full_names.append(line[1]+' '+line[2])
'''
['Joseph Zaniolini',
 'Freida Drillingcourt',
 'Nanni Herity',
 'Orazio Frayling',
 'Julianne Murrison',
 'Lucy Gamet',
 'Dyana Howatt',
 'Kassey Herion',
 'Chrissy Hedworth',
 'Hyatt Gasquoine',
 'Felicdad Tarr',
 'Andrew Bath',
 'Lucais Chastang',
 'Car Cerie']
'''

# writing to csv

# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'. 
file_to_output = open('to_save_file.csv','w',newline='')
# This will also overwrite any exisiting file with the same name, so be careful with this!

csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()

# write to an existing csv
f = open('to_save_file.csv','a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new','new','new'])
f.close()



# Working with PDF Files

# pip install PyPDF2

import PyPDF2

# reading a pdf

f = open('Working_Business_Proposal.pdf','rb')  # Notice we read it as a binary with 'rb'
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
page_one_text
f.close()

# Adding to PDFs
# We can not write to PDFs using Python because of the differences between the single string type of Python, and the variety of fonts, placements, and other parameters that a PDF could have.
# What we can do is copy pages and append pages to the end.

f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open("Some_New_Doc.pdf","wb")
pdf_writer.write(pdf_output)
f.close()


# Let's try to grab all the text from this PDF file
f = open('Working_Business_Proposal.pdf','rb')
# List of every page's text.
# The index will correspond to the page number.
pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)
for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text.append(page.extractText())



# Task One: Grab the Google Drive Link from .csv File

data = open('Exercise_Files/find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

# We can see its along the diagonal, which means the values are at the index position that matches the row's number order. So the 1st letter is the 1st item in the 1st row, the 2nd letter is the 2nd item in the 2nd row, the 3rd item is the 3rd letter in the 3rd row and so on. We can use enumerate to track the row number and simply index off the data_lines.
# Method One
link_list = []
for row_num,data in enumerate(data_lines):
    link_list.append(data[row_num])
''.join(link_list) # 'https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q'

# Method Two
link_str = ''
for row_num,data in enumerate(data_lines):
    link_str+=data[row_num]
link_str # 'https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q'

    
# Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.¶
f = open('Exercise_Files/Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfFileReader(f)
pdf.numPages

# Phone Number Matching - Lot's of ways to do this, but you had to figure out the phone number was in format ###.###.####
import re
pattern = r'\d{3}'
all_text = ''
for n in range(pdf.numPages):    
    page = pdf.getPage(n)
    page_text = page.extractText()   
    all_text = all_text+' '+page_text
for match in re.finditer(pattern,all_text):
    print(match)

# Once you know the correct pattern:
import re
pattern = r'\d{3}.\d{3}.\d{4}'
for n in range(pdf.numPages):    
    page  = pdf.getPage(n)
    page_text = page.extractText()
    match = re.search(pattern,page_text)    
    if match:
        print(match.group())
        
        







