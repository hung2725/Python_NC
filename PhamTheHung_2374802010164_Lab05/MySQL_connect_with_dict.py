'''
Created on May 29, 2019
Ch07
@author: Burkhard A. Meier
'''

import mysql.connector 

# create dictionary to hold connection info
dbConfig = {
    'user': 'root',         # your user name
    'password': '123456',     # your password
    'host': '127.0.0.1',
    }

conn = mysql.connector.connect(**dbConfig) 
print(conn)  
conn.close() 
