import pymysql
import GuiDBConfig as guiConf

GUIDB = 'GuiDB'

# unpack dictionary credentials  
conn = pymysql.connect(**guiConf.dbConfig)

cursor = conn.cursor()

try:
    cursor.execute(f"CREATE DATABASE {GUIDB} DEFAULT CHARACTER SET 'utf8'")
    print(f"Database '{GUIDB}' created successfully.")
except pymysql.MySQLError as err:
    print(f"Failed to create DB: {err}")

conn.close()
