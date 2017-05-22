'''
May 2017
@author: Burkhard A. Meier
'''

import MySQLdb as mysql 
conn = mysql.connect(user=<adminUser>, password=<adminPwd>, host='127.0.0.1') 
print(conn)  
conn.close() 
