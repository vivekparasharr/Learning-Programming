
################## Create and access an MS Access database
# https://datatofish.com/ms-access-2016-tutorials/

import pyodbc
import pandas as pd

# connect Python to MS Access
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Ron\Desktop\testdb.accdb;')

# SQL query in Python
SQL_Query = pd.read_sql_query(
'''select
product_name,
product_price_per_unit,
units_ordered,
((units_ordered) * (product_price_per_unit)) AS revenue
from tracking_sales''', conn)

# Assign the fields into the DataFrame
df = pd.DataFrame(SQL_Query, columns=['product_name','product_price_per_unit','units_ordered','revenue'])


# Insert rows into an Access database
# if you try to insert multiple records within the same cursor.execute(”’ ”’) block, you’ll get an error 
# workaround is to insert a single record per cursor.execute(”’ ”’) block
cursor.execute('''
                    INSERT INTO names_table (First_Name, Last_Name, Age)
                    VALUES('Mike', 'Jordan',55)
                  ''')
cursor.execute('''
                    INSERT INTO names_table (First_Name, Last_Name, Age)
                    VALUES('Mia', 'Mogran',66)
                  ''')
conn.commit()


