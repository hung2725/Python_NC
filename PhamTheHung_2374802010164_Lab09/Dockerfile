# Chọn image Python
FROM python:3.11-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy file requirements
COPY requirements.txt .

# Cài đặt dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ project vào container
COPY . .

# Expose port (Flask mặc định là 5000)
EXPOSE 5000

# Lệnh chạy app
CMD ["python", "run.py"]
