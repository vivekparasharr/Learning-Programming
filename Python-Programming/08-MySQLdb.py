
# mysql from python can be downloaded here
# https://sourceforge.net/projects/mysql-python/files/
# Make sure that the version you download match with the Python version
# Next, obtain your host name, user and password.
# In some cases, your host name would be 'localhost' for local instances.
# You can see the user name in MySQL Workbench, by going to the Database tab, and then selecting Manage Connections
# Then, look for the Username for you instance. 


import MySQLdb

# syntax
# establish connection
db = MySQLdb.connect(host='your host name',  # your host name is often 'localhost'
                     user='your username',            
                     passwd='your password',  
                     db='your database')        
cur = db.cursor()

# to apply SQL
cur.execute('SELECT * FROM your table')
for row in cur.fetchall():
    print row

db.close()


# Example
# create the test_database
CREATE DATABASE test_database
# create the names_table
CREATE TABLE test_database.names_table (First_Name varchar(20), 
Last_Name varchar(20), Age varchar(3))
# add the records into the names_table
INSERT INTO test_database.names_table (First_Name, Last_Name, Age)
VALUES
('Jon', 'Snow',22),
('Maria', 'Smith',34),
('Emma', 'Jones',51),
('Bill', 'Yu',63),
('Jack', 'Green',27)
# check that the data is indeed stored in the names_table
SELECT * FROM test_database.names_table


# Update values in MySQL table using Python
cur.execute('''
            UPDATE test_database.names_table
            SET Last_Name = 'Smith-Jackson',
                Age = 35
            WHERE First_Name = 'Maria'        
            ''')
db.commit()



