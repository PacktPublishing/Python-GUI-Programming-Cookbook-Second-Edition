'''
May 2017
@author: Burkhard A. Meier
'''

import MySQLdb as mysql 
import Ch07_Code.GuiDBConfig as guiConf 

GUIDB = 'GuiDB' 
 
# unpack dictionary credentials  
conn = mysql.connect(**guiConf.dbConfig) 
 
cursor = conn.cursor() 

cursor.execute("SHOW DATABASES") 
print(cursor.fetchall()) 
 
conn.close() 