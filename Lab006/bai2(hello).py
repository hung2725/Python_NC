from flask import Flask

# Khởi tạo ứng dụng Flask. Tên biến ở đây là 'ungdung'
ungdung = Flask(__name__)

# Định nghĩa Route ('/') và View Function (hàm xử lý)
@ungdung.route('/')
def hello():
    # Trả về chuỗi "Xin chào!" khi người dùng truy cập trang chủ
    return 'Xin chào!'

# Lệnh chạy ứng dụng khi tệp được thực thi trực tiếp
if __name__ == "__main__":
    # Bật Debug mode
    ungdung.run(port=5050, debug=True)