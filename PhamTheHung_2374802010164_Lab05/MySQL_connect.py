import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="Hung2725",
)
print(conn)
conn.close()
