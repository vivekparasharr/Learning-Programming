
import pandas as pd

# Step 1: Create a DataFrame
df = pd.DataFrame({'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]})

# Step 2: Create a Database
import sqlite3
conn = sqlite3.connect('/Users/vivekparashar/Desktop/TestDB1.db')
c = conn.cursor()

# create the 'CARS' table
c.execute('CREATE TABLE CARS (Brand text, Price number)')
conn.commit()

# Step 3: Save from Pandas DataFrame to SQL
df.to_sql('CARS', conn, if_exists='replace', index = False)

# Access data from SQL database to see if it worked
# Recurse over data using for loop
c.execute('''  
SELECT * FROM CARS
          ''')
for row in c.fetchall():
    print (row)

# Pull  data into a dataframe
c.execute('''  
SELECT * FROM CARS
          ''')
df2 = pd.DataFrame(c.fetchall(), columns=['Brand','Price'])    
print(df2)

# Drop the table
c.execute('DROP TABLE CARS') # drop table

c.close() # close connection




##################################################
# How to Create a Database in Python using sqlite3
##################################################

import sqlite3
import pandas as pd
from pandas import DataFrame

# Create conneciton
conn = sqlite3.connect('TestDB.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create database structure (empty tables)
# Create table - CLIENTS
c.execute('''CREATE TABLE CLIENTS
             ([generated_id] INTEGER PRIMARY KEY,[Client_Name] text, [Country_ID] integer, [Date] date)''')
# Create table - COUNTRY
c.execute('''CREATE TABLE COUNTRY
             ([generated_id] INTEGER PRIMARY KEY,[Country_ID] integer, [Country_Name] text)''')
# Create table - DAILY_STATUS
c.execute('''CREATE TABLE DAILY_STATUS
             ([Client_Name] text, [Country_Name] text, [Date] date)''')
conn.commit()
# Note that the syntax to create new tables should only be used once in the code (unless you dropped the table/s at the end of the code). 
# The [generated_id] column is used to set an auto-increment ID for each record
# When creating a new table, you can add both the field names as well as the field formats (e.g., Text)


# Import the data into pandas
read_clients = pd.DataFrame({'Client_Name': ['Jon Smith','Bill Martin','Maria Blue','Rita Yu','Jack Mo'],
                        'Country_ID': [1,2,3,4,5],
                        'Date': [14012019,14012019,14012019,14012019,14012019]})
read_clients.to_sql('CLIENTS', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'CLIENTS' 
read_country = pd.DataFrame({'Country_ID': [1,2,3,4,5,6,7,8,9,10],
'Country_Name': ['Japan','US','Canada','Brazil','UK','Spain','China','Italy','Peru','Russia']})
read_country.to_sql('COUNTRY', conn, if_exists='replace', index = False) # Replace the values from the csv file into the table 'COUNTRY'

# When reading the csv:
# - Place 'r' before the path string to read any special characters, such as '\'
# - Don't forget to put the file name at the end of the path + '.csv'
# - Before running the code, make sure that the column names in the CSV files match with the column names in the tables created and in the query below
# - If needed make sure that all the columns are in a TEXT format
c.execute('''
INSERT INTO DAILY_STATUS (Client_Name,Country_Name,Date)
SELECT DISTINCT clt.Client_Name, ctr.Country_Name, clt.Date
FROM CLIENTS clt
LEFT JOIN COUNTRY ctr ON clt.Country_ID = ctr.Country_ID
          ''')
c.execute('''
SELECT DISTINCT *
FROM DAILY_STATUS
WHERE Date = (SELECT max(Date) FROM DAILY_STATUS)
          ''')
#print(c.fetchall())

df = DataFrame(c.fetchall(), columns=['Client_Name','Country_Name','Date'])
print (df) # To display the results after an insert query, you'll need to add this type of syntax above: 'c.execute(''' SELECT * from latest table ''')

df.to_sql('DAILY_STATUS', conn, if_exists='append', index = False) # Insert the values from the INSERT QUERY into the table 'DAILY_STATUS'
# export_csv = df.to_csv (r'C:\Users\Ron\Desktop\Client\export_list.csv', index = None, header=True) # Uncomment this syntax if you wish to export the results to CSV. Make sure to adjust the path name
# Don't forget to add '.csv' at the end of the path (as well as r at the beg to address special characters)


# Run the code for a Subsequent Date
read_clients = pd.DataFrame({'Client_Name': ['Ron Green', 'Jeff Long', 'Carrie Lan', 'Marry Sig', 'Ben Baker'],
                            'Country_ID': [3,8,3,5,9],
                            'Date': [15012019, 15012019, 15012019, 15012019, 15012019]})   
read_clients.to_sql('CLIENTS', conn, if_exists='append', index = False)
read_country = pd.DataFrame ({'Country_ID': [1,2,3,4,5,6,7,8,9,10,11,12],
                            'Country_Name': ['Japan','US','Canada','Brazil','UK','Spain','China','Italy','Peru','Russia','Mexico','Germany']})
read_country.to_sql('COUNTRY', conn, if_exists='replace', index = False)

c.execute('''
INSERT INTO DAILY_STATUS (Client_Name,Country_Name,Date) 
SELECT DISTINCT clt.Client_Name, ctr.Country_Name, clt.Date
FROM CLIENTS clt
LEFT JOIN COUNTRY ctr ON clt.Country_ID = ctr.Country_ID
          ''')
c.execute('''
SELECT DISTINCT *
FROM DAILY_STATUS
WHERE Date = (SELECT max(Date) FROM DAILY_STATUS)
          ''')

df = DataFrame(c.fetchall(), columns=['Client_Name','Country_Name','Date'])
print (df)

df.to_sql('DAILY_STATUS', conn, if_exists='append', index = False)
# export_csv = df.to_csv (r'C:\Users\Ron\Desktop\Client\export_list.csv', index = None, header=True)



