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
 
try: 
    cursor.execute("CREATE DATABASE {} \
                    DEFAULT CHARACTER SET 'utf8'".format(GUIDB)) 
 
except mysql.Error as err:                                          # @UndefinedVariable
    print("Failed to create DB: {}".format(err)) 
 
conn.close() 