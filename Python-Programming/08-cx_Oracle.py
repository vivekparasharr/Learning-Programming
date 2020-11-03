
pip install cx_Oracle

# Next, retrieve the connection information. 
# Method 1
# You can do that by locating your tnsnames.ora file on your computer (e.g., type tnsnames.ora in the Windows search bar):
# Now, open your tnsnames.ora file and look for your desired connection.
# It should look like the info below (I highlighted in colors the 3 elements that you usually need to look for before you can establish a connection between Python and your Oracle database):
### (ADDRESS = (PROTOCOL = TCP)(HOST = Host Name)(PORT = Port Number))
### (SERVICE_NAME = Service Name)

# Method 2
# For example, you can run the following query in Oracle to get the Service Name:
select sys_context('userenv','service_name') from dual
# You may also run the following query in Oracle to get the list of users:
select username from dba_users


# Connect Python to Oracle using cx_Oracle connect
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number', service_name='Service Name') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'User Name', password='Personal Password', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute('select * from database.table') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()
