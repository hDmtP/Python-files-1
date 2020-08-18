
import pyodbc
conn = pyodbc.connect(
    'Driver = {SQL Server};'
    'Server = RON\SQLEXPRESS;'
    'Database = TestDB;'
    'Trusted_Connection = yes;'
)

cursor = conn.cursor()
cursor.execute('SELECT * from TestDB.dbo.Person')

for row in cursor:
    print(row)
    
'''    
import pypyodbc
import pyodbc
cnxnMS = pyodbc.connect("""DRIVER={SQL Server};SERVER='www.xmlsoccer.com';UID='me';PWD='pass';DATABASE='me'""")  
'''
'''
import pyodbc

conn = pyodbc.connect('DSN=mynewdsn;Trusted_Connection=yes;')
'''