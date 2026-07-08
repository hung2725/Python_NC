import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",          # Thay user MySQL của bạn
        password="Hung2725",           # Thay mật khẩu MySQL nếu có
        database="quanly_hoadon",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.Cursor
    )
print("Kết nối thành công:", get_connection())
