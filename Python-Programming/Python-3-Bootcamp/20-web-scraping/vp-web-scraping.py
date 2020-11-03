# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:12:05 2020

@author: vivek
"""

'''
html - basic structure and content of a webpage
css - design and style of a webpage
javascript - used to define the interactive elements of a webpage
'''

import requests

result=requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
print(result.text) # the output is a large text string

# grabbing a tag
# now we will convert this giant string into a soup
import bs4
soup=bs4.BeautifulSoup(result.text,"lxml")
soup.select('title') # [<title>Jonas Salk - Wikipedia</title>]

para_list=soup.select('p') # soup.select returns a list of paragraphs
para_list[1].getText()

# grabbing a class
# other select options
soup.select('div') # all elements with div tag
soup.select('#some_id') # elements containing id=some_id
soup.select('.some_class') # elements containing class=some_class
soup.select('div span') # any elements named span within a div element
soup.select('div > span') # any elements named span directly within the div element, with nothing else in between

indx=soup.select('.toctext')
indx[0].text

for item in soup.select('.toctext'):
    print(item.text)

# grabbing an image
res=requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup=bs4.BeautifulSoup(res.text,'lxml')
# we look for the link under the tag src
computer_image=soup.select('.thumbimage')[0]
computer_image['src']
image_link=requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg') # note we added https:
image_link.content # how computer sees the image
f=open('my_computer_image.jpg','wb') # wb - write binary mode
f.write(image_link.content)  # write image_link.content to the file
f.close()

# in jupyter notebook we can use the following to import the image into our notebook
<img src="//upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg">



# practical example 1
# get title of every book with 2 star rating
import requests
import bs4

# empty list to store titles of books with 2 star rating
books_with_two_stars=[]

# for loop to go over the 20 pages of book catelogue 
for i in range(1,51):
    base_url=f'http://books.toscrape.com/catalogue/page-{i}.html'
    
    # get info about all books on the page, as a list of book-details
    bks=requests.get(base_url) # grab the data on the page
    soup = bs4.BeautifulSoup(bks.text,'lxml') # read it using bs4
    pod=soup.select('.product_pod') # use bs4 select method to get all info about books from the page data

    # recurse over each book in the list of books on the page
    # method 1: for bk in pod:
    # method 2: recurse using length of list 'pod'
    # we can check how many books are in the pod list 
    ln=len(pod)  # Out[33]: 20
    for j in range(0,ln):
        # check if the book item from pod has a rating of two - two methods:
        # method 1: quick and dirty way to see if star-rating Two is in the pod[0]
        # 'star-rating Two' in str(pod[0]) # Out[35]: False
        # 'star-rating Three' in str(pod[0]) # Out[36]: True
        # method 2: using the bs4 select method - if we get an empty list back then the rating is not 2, we can use this logic
        if len(pod[j].select('.star-rating.Two')) != 0: # the spance between rating and Two needs to be filled with a dot    
            # getting the title of the book
            # pod[0].select('a') # we get a list of 2 items, the first is the image of the book and the second is the title of the book
            books_with_two_stars.append(pod[j].select('a')[1]['title']) # with [1] we grab the second item in the list, and with ['title'] we grab the title of the book


# practical example 2




import pandas as pd

# Example: Reading the data from Wikipedia
url='https://en.wikipedia.org/wiki/Cricket_World_Cup'
tables = pd.read_html(url)
print("There are : ",len(tables)," tables")
print("Take look at table 0")
print(tables[0])

# Example: To scrape a particular table using match as a parameter
URL = "https://en.wikipedia.org/wiki/Cricket_World_Cup"
tables = pd.read_html(URL,match="Performance details")
print("There are : ",len(tables)," tables")
print("Take look at table 0")
tables[0]

'''
formatting output: Useful attributes  
1. header    : The row to use to make as the column header.
2. index_col : The column to use to create the index
3. skiprows  : Number of rows to skip after parsing column integer
'''

# You can also target a specific table in another way
pandas.read_html(URL,attrs = {'html_tag' : 'value'})
# we can directly target an HTML tag corresponding to the required table by inspecting the table.
# After inspecting find the related tag exclusive to that table, here we can see that class:'wikitable' is a tag that identifies this table
#By using this line of code we can hit the target table directly
pandas.read_html(URL,attrs = {'class' : 'wikitable'})




