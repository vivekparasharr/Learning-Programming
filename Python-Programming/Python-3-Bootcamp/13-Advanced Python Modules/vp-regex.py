# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 09:23:22 2020

@author: vivek
"""

import re # regex library


# how to search text using re

text="The agent's phone number is 408-555-1234. Call (on phone) soon!"

'phone' in text # basic way of searching
re.search('phone',text) # re way of searching returns location (called span) of pattern
re.search('not-in-text',text) # searching this returns nothing

match=re.search('phone',text) # in case of multiple matches, we only get back first match
match.span()
match.start()
match.end()

matches=re.findall('phone',text) # just returns back the string of all matches, not the match object
len(matches) # how many matches there were

# iterator can be used to get back the actual match object
for match in re.finditer('phone',text):
    print(match) # match object
    print(match.span()) # match location/span
    print(match.group()) # matched text


# how to search patterns
'''
character identifiers:
\d - digit
\w - alphanumeric
\s - whitespace
\D - non digit
\W - non alphanumeric
\S - non whitespace

quantifiers:
+ pattern occurs one or more times
{3} exactly three times
{2,4} two to four times
{3,} three or more times
* zero or more times
? once or none
'''

r'(\d\d\d)-\d\d\d-\d\d\d\d' # regex for phone number (555)-555-5555
r'(\d{3})-\d{3}-\d{4}' # same as above but uses {qualtifiers}

match=re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)

# compile+group functions together can be used to extract a sub pattern text from a pattern 
# compile function is used to club a lot of sub patterns together to form a big pattern
# the sub patterns can later be called separately
# syntax - re.compile(r'(pattern1)-(p2)-(p3)'), here we are combining three patterns

phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
match=re.search(phone_pattern, text)
match.group() # '408-555-1234'
match.group(1) # '408'
match.group(2) # '555'
match.group(3) # '1234'


'''
operators
| - can be used to search multiple patterns
() - example, r'app(le|lication|ly) can use () and pipe in combination to search apple, application and apply using the same pattern
[] - used to exclude pattern from text and return the text without the parts that match the pattern. this is a good way to get rid of puctuation from a text

wildcards
. - if you search for r'.at', you will be returned cat, hat, pat, etc. (whatever is there in your text before .at)
^ - the pattern starts with a number
$ - the pattern ends with a number
'''
text='there are 2 numbers inside this 1 sentence'
matches=re.findall(r'[^\d]+',text)
clean=' '.join(matches) # can be used to rejoin different strings in a list based on whitespace
clean.split(' ') # can be used to split the text string

# exclusion example
text='this is a string! but it has punctuation. how can we remove it?'
clean_list=re.findall(r'[^!.? ]+',text) # can be used to get rid of punctuation
' '.join(clean_list) # 'this is a string but it has punctuation how can we remove it'

# inclusion example
text='only find the hyphen-words in this text-string'
re.findall(r'[\w]+',text) # ['only', 'find', 'the', 'hyphen', 'words', 'in', 'this', 'text', 'string']
re.findall(r'[\w]+-[\w]+',text) # ['hyphen-words', 'text-string']


