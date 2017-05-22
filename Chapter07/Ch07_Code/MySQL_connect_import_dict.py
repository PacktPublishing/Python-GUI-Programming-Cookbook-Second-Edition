'''
May 2017
@author: Burkhard A. Meier
'''

import MySQLdb as mysql 
import Ch07_Code.GuiDBConfig as guiConf 

# unpack dictionary credentials  
conn = mysql.connect(**guiConf.dbConfig) 
print(conn) 