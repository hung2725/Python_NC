import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Hung2725",     # sửa nếu bạn có mật khẩu MySQL
        database="minimart",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.Cursor
    )

print(f"Kết nối MySQL thành công {get_connection()}")