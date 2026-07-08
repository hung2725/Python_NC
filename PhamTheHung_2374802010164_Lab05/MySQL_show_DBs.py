import pymysql
import GuiDBConfig as guiConf

GUIDB = 'GuiDB'

# unpack dictionary credentials
conn = pymysql.connect(**guiConf.dbConfig)

cursor = conn.cursor()

# show all databases
cursor.execute("SHOW DATABASES")
print(cursor.fetchall())

conn.close()
