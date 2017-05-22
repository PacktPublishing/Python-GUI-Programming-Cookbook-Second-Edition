'''
May 2017
@author: Burkhard A. Meier
'''

import MySQLdb as mysql 

# create dictionary to hold connection info
dbConfig = {
    'user': <adminUser>,        # your user name
    'password': <adminPwd>,     # your password
    'host': '127.0.0.1',
    }

conn = mysql.connect(**dbConfig) 
print(conn)  
conn.close() 
