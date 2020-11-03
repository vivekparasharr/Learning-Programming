
import pyodbc 

# connect to database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# select from an existing table
cursor.execute('SELECT * FROM TestDB.dbo.People')
conn.commit()

# drop table
cursor.execute('DROP TABLE TestDB.dbo.People')
conn.commit()

# create table
cursor.execute('''
               CREATE TABLE People
               (
               Name nvarchar(50),
               Age int,
               City nvarchar(50)
               )
               ''')
conn.commit()

# insert rows into an existing table
cursor.execute('''
                INSERT INTO TestDB.dbo.People (Name, Age, City)
                VALUES
                ('Jade',20,'London'),
                ('Mary',47,'Boston'),
                ('Jon',35,'Paris')  
                ''')
conn.commit()

# Update Records in SQL Server 
cursor.execute('''
                UPDATE TestDB.dbo.Person
                SET Age = 29,City = 'Montreal'
                WHERE Name = 'Jon'
                ''')
conn.commit()


# Import a CSV File to SQL Server using Python
# https://datatofish.com/import-csv-sql-server-python/


