# Dùng Python 3.11 làm nền
FROM python:3.11-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Copy toàn bộ project vào container
COPY . .

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng 5000 cho Flask
EXPOSE 5000

# Lệnh chạy Flask app khi container khởi động
CMD ["python", "run.py"]
