# Lập Trình Python Nâng Cao - Thực Hành

**Môn học:** Lập trình Python Nâng Cao  
**Mã lớp:** 251_71ITSE31003_0103  
**Sinh viên:** Phạm Thế Hùng - 2374802010164  


---

## Mục lục

1. [Tổng quan cấu trúc](#tổng-quan-cấu-trúc-thư-mục)
2. [Cách cài Python và dùng chung](#cách-cài-python-và-các-thao-tác-chung)
3. [Lab006 - Thực hành Flask trên lớp](#lab006---thực-hành-flask-trên-lớp)
4. [Lab 01 - Tkinter cơ bản](#lab-01---tkinter-cơ-bản)
5. [Lab 02 - Tkinter nâng cao](#lab-02---tkinter-nâng-cao)
6. [Lab 03 - Tkinter Spinbox/ProgressBar/Menu](#lab-03---tkinter-spinboxprogressbarmenu)
7. [Lab 04 - Tkinter OOP](#lab-04---tkinter-oop)
8. [Lab 05 - Kết nối MySQL](#lab-05---kết-nối-mysql)
9. [Lab 06 - Quản lý cửa hàng](#lab-06---quản-lý-cửa-hàng-tkinter--mysql--pdf--biểu-đồ)
10. [Lab 07 - Flask Web 4 chương](#lab-07---flask-web-cơ-bản-4-chương)
11. [Lab 08 - Flask Blog](#lab-08---flask-blog-sqlalchemy--migrate--docker)
12. [Lab 09 - Flask Blog nâng cao](#lab-09---flask-blog-nâng-cao-auth--login--upload--docker)
13. [KTT1 - Kiểm tra giữa kỳ 1](#ktt1---kiểm-tra-giữa-kỳ-1)
14. [KTT2 - Kiểm tra giữa kỳ 2](#ktt2---kiểm-tra-giữa-kỳ-2)
15. [Lưu ý quan trọng](#lưu-ý-quan-trọng)

---

## Tổng quan cấu trúc thư mục

```
D:\Hoc_Tap\HK251\LT_Python_NC\TH\
├── Lab006/                               # Thực hành Flask cơ bản (trên lớp)
├── PhamTheHung_2374802010164_Lab01/      # Tkinter cơ bản (GUI)
├── PhamTheHung_2374802010164_Lab02/      # Tkinter nâng cao
├── PhamTheHung_2374802010164_Lab03/      # Tkinter - Spinbox, ProgressBar, Tab, Menu
├── PhamTheHung_2374802010164_Lab04/      # Tkinter OOP
├── PhamTheHung_2374802010164_Lab05/      # Kết nối MySQL với Python
├── PhamTheHung_2374802010164_Lab06/      # Quản lý cửa hàng (Tkinter + MySQL + PDF)
├── PhamTheHung_2374802010164_Lab07/      # Flask Web cơ bản (4 chương)
├── PhamTheHung_2374802010164_Lab08/      # Flask Blog (SQLAlchemy + Migrate + Docker)
├── PhamTheHung_2374802010164_Lab09/      # Flask Blog nâng cao (Auth + Login + Docker)
├── KTT1/                                 # Kiểm tra giữa kỳ 1
├── KTT2/                                 # Kiểm tra giữa kỳ 2 (chưa hoàn thiện)
└── README.md                             # File hướng dẫn này
```

---

## Cách cài Python và các thao tác chung

### Bước 0: Cài Python (nếu chưa có)

1. Vào https://www.python.org/downloads/ tải Python 3.11+
2. Khi cài, **nhớ tick** "Add Python to PATH"
3. Kiểm tra:
```powershell
python --version
pip --version
```

### Bước 1: Di chuyển đến thư mục lab

Mỗi lab nằm trong thư mục riêng. Dùng lệnh `cd` để vào:

```powershell
# Ví dụ: vào Lab 01
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab01

# Hoặc vào Lab 06
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab06
```

### Bước 2: Tạo và kích hoạt môi trường ảo (khuyến nghị)

```powershell
# Tạo venv (chỉ làm 1 lần)
python -m venv venv

# Kích hoạt (PowerShell)
venv\Scripts\Activate.ps1

# Nếu báo lỗi "execution policy", chạy dòng này trước:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Kích hoạt (CMD - Command Prompt)
venv\Scripts\activate.bat

# Khi thấy xuất hiện (venv) ở đầu dòng là đã kích hoạt thành công
```

### Bước 3: Cài thư viện

```powershell
# Cài từ requirements.txt (nếu có)
pip install -r requirements.txt

# Hoặc cài trực tiếp
pip install pymysql reportlab matplotlib flask
```

### Bước 4: Chạy file Python

```powershell
python Bai01.py
python main.py
python run.py
```

### Bước 5: Tắt venv (khi không dùng nữa)

```powershell
deactivate
```

---

## Lab006 - Thực hành Flask trên lớp

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\Lab006\`

### Mô tả
Các bài thực hành Flask cơ bản trên lớp, từ Hello World đến route động và template.

### Cấu trúc file
| File | Chức năng | Port |
|------|-----------|------|
| `bai2(hello).py` | Flask Hello World đơn giản | 5050 |
| `bai4(app).py` | Flask + HTML inline + datetime | 5000 |
| `bai5.py` | Flask 2 route: `/` và `/monhoc` | 5050 |
| `bai6.py` | Flask route động: `/monhoc/<tenmon>` | 5050 |
| `bai7.py` | Flask + render_template + route `/sinhvien/<int:namhoc>` | 5050 |

### Cách chạy chi tiết

#### Bài 2: Hello World
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\Lab006
python "bai2(hello).py"
```
- Mở trình duyệt: http://localhost:5050
- Kết quả: Hiện chữ "Xin chào!"

#### Bài 4: Trang chủ có link + HTML
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\Lab006
python "bai4(app).py"
```
- Mở trình duyệt: http://localhost:5000
- Kết quả: Hiện link Van Lang University + "Xin chào! Tan sinh vien nam 2026"

#### Bài 5: Thêm route /monhoc
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\Lab006
python bai5.py
```
- http://localhost:5050 → Trang chủ
- http://localhost:5050/monhoc → "Day la trang mon hoc!"

#### Bài 6: Route động
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\Lab006
python bai6.py
```
- http://localhost:5050/monhoc/Python → "Day la trang mon hoc PYTHON"
- http://localhost:5050/monhoc/Flask → "Day la trang mon hoc FLASK"

#### Bài 7: Route động + Template
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\Lab006
python bai7.py
```
- http://localhost:5050/monhoc/Python → Hiển thị qua template `hello_template.html`
- http://localhost:5050/sinhvien/2025 → "Day la trang sinh vien nam 2025"

> **Lưu ý:** Bài 7 có lỗi trùng tên hàm `learn()` và `subjects()` (định nghĩa 2 lần). Hàm sau sẽ ghi đè hàm trước. Đây là bài tập mẫu có chủ ý.

---

## Lab 01 - Tkinter cơ bản

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab01\`

### Mô tả
Làm quen với Tkinter: tạo cửa sổ, label, entry, button, combobox, checkbox, radiobutton, scrolledtext.

### Yêu cầu
Không cần cài thêm gì. Tkinter có sẵn trong Python.

### Cách chạy
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab01

# Bài 1: Cửa sổ đơn giản nhất
python Bai01.py
# Kết quả: Cửa sổ trống tiêu đề "Phạm Thế Hùng - GUI"

# Bài 6: Entry + Button + Combobox
python Bai06.py
# Kết quả: Ô nhập tên, nút Click Me!, Combobox chọn số

# Bài 11: Tổng hợp tất cả widget
python Bai11.py
# Kết quả: Cửa sổ có Entry, Button, Combobox, Checkbutton, Radiobutton, ScrolledText
```

### Các bài chi tiết
| File | Widget chính | Test thế nào |
|------|-------------|-------------|
| Bai01.py | Cửa sổ | Chạy lên thấy cửa sổ trống |
| Bai02.py | Label | Thấy chữ "A Label" |
| Bai03.py | Button + Entry | Gõ tên → nhấn "Click Me!" → thấy "Hello [tên]" |
| Bai04.py | Combobox | Chọn số từ dropdown |
| Bai05.py | Checkbutton | Tick/bỏ tick các ô |
| Bai06.py | Radiobutton | Chọn màu → nền cửa sổ đổi màu |
| Bai07.py | ScrolledText | Ô text có thanh cuộn |
| Bai08.py | Resizable | Cửa sổ không co giãn được |
| Bai09.py | Spinbox | Nút lên/xuống chọn số |
| Bai10.py | Progressbar | Thanh tiến trình |
| Bai11.py | Tất cả | Tổng hợp đầy đủ |

---

## Lab 02 - Tkinter nâng cao

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab02\`

### Mô tả
Gồm 20 bài từ cơ bản đến nâng cao với Tab, LabelFrame, Notebook, Menu bar, Style tùy chỉnh.

### Cách chạy
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab02

# Chạy bài tổng hợp cuối cùng (đầy đủ nhất)
python Bai20.py
```

Kết quả: Cửa sổ có 2 tab:
- **Tab 1**: Entry + Combobox + Button + ScrolledText
- **Tab 2**: Checkbutton (Disabled/UnChecked/Enabled), Radiobutton (đổi màu nền), Menu bar (File > New/Exit, Help > About)

Test:
- Gõ tên → nhấn "Click Me!" → hiện "Hello [tên] [số]"
- Chọn Radiobutton → khung "Labels in a Frame" đổi màu (Blue/Gold/Red)
- Tick "UnChecked" → "Enabled" bị vô hiệu hóa
- File > Exit → thoát

---

## Lab 03 - Tkinter Spinbox/ProgressBar/Menu

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab03\`

### Mô tả
Spinbox, ProgressBar, Canvas vẽ hình, Messagebox (hộp thoại thông báo), Menu bar.

### Cách chạy
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab03

# Bài tổng hợp đầy đủ nhất (3 tab)
python Bai9.py
```

Kết quả: Cửa sổ có 3 tab:
- **Tab 1**: Entry + Combobox + **2 Spinbox** (chọn số, ghi vào ScrolledText) + ScrolledText
- **Tab 2**: Checkbutton, Radiobutton đổi màu, **ProgressBar** với 4 nút điều khiển:
  - "Run Progressbar" → chạy từ 0→100%
  - "Start Progressbar" → chạy liên tục
  - "Stop immediately" → dừng ngay
  - "Stop after second" → dừng sau 1 giây
- **Tab 3**: Canvas hình cam (2 ô màu cam)

Test Messagebox:
- Help > About → hiện hộp thoại "askyesnocancel" (3 nút: Yes/No/Cancel)
- Kết quả in ra console (True/False/None)

### Các bài khác
| File | Chức năng |
|------|-----------|
| Bai1.1.py | Tab + LabelFrame + Entry + Checkbutton + Radiobutton + Menu + Messagebox |
| Bai1.2.py | Thêm Spinbox vào Tab 1 |
| Bai1.3.py | Thêm ProgressBar |
| Bai1.4.py | Canvas vẽ hình ở Tab 3 |
| Bai2.1.py | Messagebox showinfo |
| Bai2.2.py | Messagebox showwarning |
| Bai3.py | Messagebox showerror |
| Bai4.py | Messagebox askyesnocancel |
| Bai5.1-5.5.py | Các biến thể ProgressBar |

---

## Lab 04 - Tkinter OOP

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab04\`

### Mô tả
Chuyển code Tkinter sang lập trình hướng đối tượng (OOP). Sử dụng class, ToolTip, biến Tkinter (DoubleVar, StringVar).

### Cách chạy
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab04

# Bài tổng hợp đầy đủ nhất
python Bai6.py
```

Kết quả: Cửa sổ OOP với:
- **Tab 1**: Entry + Combobox + 2 Spinbox + ScrolledText (tất cả đều có ToolTip)
- **Tab 2**: Checkbutton, Radiobutton, ProgressBar (4 nút), Menu bar
- Khi rê chuột vào các widget → hiện tooltip màu vàng

Test OOP:
```python
# Trong code, class OOP() chứa tất cả
# __init__() tạo cửa sổ và gọi create_widgets()
# click_me() là phương thức của class
```

### Các bài khác
| File | Chức năng |
|------|-----------|
| Bai1.1.py | DoubleVar + phép tính |
| Bai1.2.py | StringVar + get/set |
| Bai1.3.py | Các biến Tkinter |
| Bai1.4.py | Biến Tkinter nâng cao |
| Bai2.py | OOP đầu tiên (class + method) |
| Bai3.1.py | OOP + Spinbox |
| Bai3.2.py | OOP + ProgressBar |
| Bai3.3.py | OOP + Notebook + Menu |
| Bai4.py | OOP + Global CONST |

---

## Lab 05 - Kết nối MySQL

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab05\`

### Mô tả
Kết nối Python với MySQL qua thư viện pymysql: tạo database, tạo bảng, thêm/sửa/xóa dữ liệu (CRUD).

### Yêu cầu
```powershell
pip install pymysql
```

### Bước 1: Cấu hình MySQL

Mở file `GuiDBConfig.py`, sửa thông tin:
```python
dbConfig = {
    'user': 'root',
    'password': 'Hung2725',   # ← Sửa thành password MySQL của bạn
    'host': '127.0.0.1',       # localhost
}
```

> **Cần có MySQL Server đang chạy** (ví dụ: khởi động XAMPP > MySQL > Start)

### Bước 2: Chạy từng bước

#### A. Kiểm tra kết nối
```powershell
python MySQL_connect.py
```
- Kết quả: `<pymysql.connections.Connection object at 0x...>` → Thành công
- Lỗi: `Can't connect to MySQL server on '127.0.0.1'` → MySQL chưa chạy

#### B. Xem danh sách database
```powershell
python MySQL_show_DBs.py
```
- Kết quả: Danh sách các database trong MySQL

#### C. Tạo database GuiDB
```powershell
python MySQL_create_DB.py
```
- Kết quả: "Database 'GuiDB' created successfully."

#### D. Kiểm tra database đã tạo
```powershell
python MySQL_show_DBs.py
```
- Kiểm tra thấy 'GuiDB' trong danh sách

#### E. Chạy CRUD (tạo bảng, thêm dữ liệu, xem, xóa)
```powershell
python GUI_MySQL_class.py
```
Chương trình sẽ tự động:
1. Tạo bảng `Books` và `Quotations`
2. Thêm dữ liệu mẫu
3. Hiển thị dữ liệu
4. Xóa dữ liệu

Bạn có thể bỏ comment các dòng trong `if __name__ == '__main__':` để test từng chức năng:
- `mySQL.showDBs()` - xem danh sách DB
- `mySQL.createGuiDB()` - tạo DB
- `mySQL.dropGuiDB()` - xóa DB
- `mySQL.createTables()` - tạo bảng
- `mySQL.insertBooks(title, page, quote)` - thêm sách
- `mySQL.showBooks()` - xem sách
- `mySQL.showData()` - xem tất cả dữ liệu
- `mySQL.updateGOF_commit()` - sửa dữ liệu
- `mySQL.deleteRecord()` - xóa dữ liệu

#### F. Mở GUI Tkinter + MySQL
```powershell
python GUI_MySQL.py
```
- Cửa sổ GUI có tab "MySQL" và "Widgets"
- Tab MySQL: Nhập Book Title, Page, Quote → Insert Quote → lưu vào MySQL
- Tab Widgets: Checkbutton, Radiobutton, Combobox, Spinbox, ScrolledText, File browser

### Cấu trúc database (tự động tạo)
```sql
CREATE TABLE Books (
    Book_ID INT AUTO_INCREMENT PRIMARY KEY,
    Book_Title VARCHAR(25),
    Book_Page INT
);
CREATE TABLE Quotations (
    Quote_ID INT AUTO_INCREMENT PRIMARY KEY,
    Quotation VARCHAR(250),
    Books_Book_ID INT,
    FOREIGN KEY (Books_Book_ID) REFERENCES Books(Book_ID)
);
```

---

## Lab 06 - Quản lý cửa hàng (Tkinter + MySQL + PDF + Biểu đồ)

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab06\`

### Mô tả
Ứng dụng quản lý cửa hàng tạp hóa hoàn chỉnh: quản lý khách hàng, sản phẩm, lập hóa đơn (xuất PDF), thống kê doanh thu (biểu đồ).

### Yêu cầu
```powershell
pip install pymysql reportlab matplotlib
```

### Bước 1: Tạo database

Mở phpMyAdmin (http://localhost/phpmyadmin) hoặc MySQL CLI, chạy:

```sql
CREATE DATABASE IF NOT EXISTS minimart CHARACTER SET utf8mb4;
USE minimart;

CREATE TABLE loaisanpham (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tenloai VARCHAR(100)
);

CREATE TABLE sanpham (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100),
    dongia FLOAT,
    loai_id INT,
    FOREIGN KEY (loai_id) REFERENCES loaisanpham(id)
);

CREATE TABLE khachhang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100),
    sdt VARCHAR(20),
    diachi VARCHAR(200)
);

CREATE TABLE hoadon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngaylap DATE,
    khachhang_id INT,
    tongtien FLOAT,
    FOREIGN KEY (khachhang_id) REFERENCES khachhang(id)
);

CREATE TABLE chitiethoadon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hoadon_id INT,
    sanpham_id INT,
    soluong INT,
    dongia FLOAT,
    thanhtien FLOAT,
    FOREIGN KEY (hoadon_id) REFERENCES hoadon(id),
    FOREIGN KEY (sanpham_id) REFERENCES sanpham(id)
);
```

> Có thể chạy trực tiếp file `DataBase.sql`:
> ```powershell
> mysql -u root -p < DataBase.sql
> ```

### Bước 2: Cấu hình kết nối

Mở file `db.py`, sửa dòng:
```python
password="Hung2725",   # ← Sửa password MySQL của bạn
```

### Bước 3: Chạy chương trình

```powershell
cd "D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab06"
python main.py
```

### Hướng dẫn sử dụng

#### Màn hình chính
- Tiêu đề: "PHẦN MỀM QUẢN LÝ CỬA HÀNG"
- Menu "Chức năng" gồm:
  - **Quản lý khách hàng**
  - **Quản lý sản phẩm**
  - **Lập hóa đơn**
  - **Thống kê doanh thu**
  - **Thoát**

#### 1. Quản lý khách hàng
1. Click menu **Chức năng > Quản lý khách hàng**
2. Nhập: Tên, SĐT, Địa chỉ
3. Click **Thêm** → khách hàng được lưu vào MySQL
4. Click vào dòng trong bảng → dữ liệu hiện lên ô nhập
5. Sửa thông tin → click **Sửa**
6. Chọn dòng → click **Xóa** → xác nhận → xóa

#### 2. Quản lý sản phẩm
1. Click menu **Chức năng > Quản lý sản phẩm**
2. Nhập: Tên, Đơn giá, Loại
3. **Thêm/Sửa/Xóa** tương tự khách hàng
4. Loại sản phẩm tự động được tạo nếu chưa có

#### 3. Lập hóa đơn
1. Click menu **Chức năng > Lập hóa đơn**
2. Tab "Lập hóa đơn":
   - Chọn khách hàng từ dropdown
   - Chọn sản phẩm từ dropdown
   - Nhập số lượng
   - Click **Thêm sản phẩm** → sản phẩm xuất hiện trong bảng
   - Lặp lại để thêm nhiều sản phẩm
   - Click **Lưu & Xuất Hóa Đơn (PDF)** → tự động mở file PDF
3. Tab "Lịch sử hóa đơn":
   - Xem danh sách hóa đơn đã lưu
   - Click vào hóa đơn → xem chi tiết bên dưới

#### 4. Thống kê doanh thu
1. Click menu **Chức năng > Thống kê doanh thu**
2. Cửa sổ mới hiện biểu đồ đường doanh thu 30 ngày gần nhất
3. Click **Đóng** để thoát

### File PDF
Hóa đơn được xuất ra file `hoadon_X.pdf` (X là mã hóa đơn) và tự động mở lên.

> Nếu báo lỗi font, hãy đảm bảo file `DejaVuSans.ttf` nằm cùng thư mục với `hoadon.py`.

---

## Lab 07 - Flask Web cơ bản (4 chương)

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab07\`

### Mô tả
Học Flask qua 4 chương từ cơ bản đến nâng cao.

### Yêu cầu
```powershell
pip install Flask python-dotenv
pip install flask-bootstrap flask-moment flask-wtf
```

### Chapter 1 - Flask cơ bản

**File:** `Chapter1/hello.py`

**Cách chạy:**
```powershell
cd "D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab07\Chapter1"
# Nếu có venv:
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python hello.py
```

**Test:**
- http://localhost:5000 → Hello World + tên sinh viên
- http://localhost:5000/user/Hung → "Hello, Hung!"

### Chapter 2 - Request & Response

**File:** `Chapter2/hello.py`

**Cách chạy:**
```powershell
cd "D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab07\Chapter2"
python hello.py
```

**Test:**
- http://localhost:5000/user/Hung → Hello Hung
- http://localhost:5000/info → Hiển thị thông tin request (IP, browser, URL)
- http://localhost:5000/redirect → Tự động redirect về /
- http://localhost:5000/set_session/Hung → Set session
- http://localhost:5000/get_session → Đọc session

### Chapter 3 - Templates (Jinja2)

**File:** `Chapter3/hello.py`

**Cách chạy:**
```powershell
cd "D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab07\Chapter3"
python hello.py
```

**Test:**
- http://localhost:5000 → Trang chủ
- http://localhost:5000/user/Hung → Hiện "Hello, Hung!" với Bootstrap
- http://localhost:5000/variables/Hung → Biến Jinja2
- http://localhost:5000/loops → Vòng lặp for
- http://localhost:5000/conditionals → Câu điều kiện
- http://localhost:5000/dates → Định dạng thời gian (Flask-Moment)

### Chapter 4 - Forms & Upload

**File:** `Chapter4/hello.py`

**Cách chạy:**
```powershell
cd "D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab07\Chapter4"
python hello.py
```

**Test:**
- http://localhost:5000/contact → Form liên hệ (tên, email, nội dung)
- http://localhost:5000/upload → Upload file

### Chạy file tổng hợp (hello.py gốc)

```powershell
cd "D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab07"
python hello.py
```

http://localhost:5000 → Hello World + `/user/<name>` route động

---

## Lab 08 - Flask Blog (SQLAlchemy + Migrate + Docker)

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab08\`

### Mô tả
Blog cá nhân với Flask + SQLAlchemy ORM (SQLite) + Flask-Migrate + Docker.

### Yêu cầu
```powershell
cd "D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab08"
pip install -r requirements.txt
```
> File `requirements.txt` gồm: Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-WTF, v.v.

### Cách chạy lần đầu (đầy đủ từ A-Z)

#### Bước 1: Set biến môi trường

```powershell
$env:FLASK_APP="run.py"
$env:FLASK_ENV="development"
```

#### Bước 2: Khởi tạo database

```powershell
flask db init
```
→ Tạo thư mục `migrations/` chứa cấu hình Alembic.

```powershell
flask db migrate -m "Initial migration"
```
→ Tạo file migration từ models.

```powershell
flask db upgrade
```
→ Chạy migration để tạo bảng trong database.

#### Bước 3: Chạy ứng dụng

```powershell
python run.py
```

Mở trình duyệt: http://localhost:5000

### Hướng dẫn sử dụng

#### Trang chủ (http://localhost:5000)
- Danh sách bài viết, phân trang (5 bài/trang)
- Click tiêu đề → xem chi tiết

#### Tạo bài viết (http://localhost:5000/create)
- Nhập tiêu đề (≥5 ký tự)
- Nhập nội dung (≥10 ký tự)
- Click "Đăng bài"
- Slug tự động tạo từ tiêu đề

#### Chi tiết bài viết (http://localhost:5000/post/<slug>)
- Xem nội dung bài viết
- Viết bình luận
- Xem danh sách bình luận

### Database
- File: `blog.db` (SQLite, tự động tạo)
- Bảng: `user`, `post`, `comment`

### Nếu cần migrate thêm

Khi thay đổi model (thêm cột, sửa bảng):
```powershell
flask db migrate -m "Mô tả thay đổi"
flask db upgrade
```

### Docker

#### Build image
```powershell
docker build -t blogcanhan:latest .
```

#### Chạy container
```powershell
docker run -d -p 5000:5000 blogcanhan:latest
```
Mở http://localhost:5000

#### Đóng gói để gửi người khác
```powershell
docker save -o blogcanhan.tar blogcanhan:latest
```

#### Người nhận chạy
```powershell
docker load -i blogcanhan.tar
docker run -p 5000:5000 blogcanhan:latest
```

### Xử lý lỗi migration
Nếu gặp lỗi khi migrate, xóa thư mục `migrations/` và chạy lại:
```powershell
Remove-Item -Recurse -Force migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## Lab 09 - Flask Blog nâng cao (Auth + Login + Upload + Docker)

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab09\`

### Mô tả
Blog cá nhân nâng cao với:
- **Flask-Login**: Đăng ký/đăng nhập/đăng xuất
- **Blueprint**: Tách route thành `main` và `auth`
- **Upload ảnh**: Cho bài viết và avatar
- **About page**: Cập nhật bio, email, phone, address
- **Tìm kiếm bài viết**
- **Docker** đóng gói

### Yêu cầu
```powershell
cd "D:\Hoc_Tap\HK251\LT_Python_NC\TH\PhamTheHung_2374802010164_Lab09"
pip install -r requirements.txt
```
> File `requirements.txt` gồm: flask, flask_sqlalchemy, flask_migrate, flask_login, flask_wtf, email_validator, python-slugify

### Cách chạy lần đầu

#### Bước 1: Set biến môi trường
```powershell
$env:FLASK_APP="run.py"
$env:FLASK_ENV="development"
```

#### Bước 2: Khởi tạo database
```powershell
# Tạo thư mục migrations
flask db init

# Tạo migration đầu tiên
flask db migrate -m "Initial migration"

# Chạy migration
flask db upgrade
```

#### Bước 3: Chạy ứng dụng
```powershell
python run.py
```
Mở http://localhost:5000

### Các chức năng chi tiết

#### 1. Đăng ký tài khoản
- Vào http://localhost:5000/auth/register
- Nhập: Username, Email, Password, Confirm Password
- Click "Đăng ký"
- Thành công → redirect về trang đăng nhập

#### 2. Đăng nhập
- Vào http://localhost:5000/auth/login
- Nhập username và password
- Click "Đăng nhập"

#### 3. Trang chủ (http://localhost:5000/)
- Xem danh sách bài viết (phân trang 5 bài/trang)
- Bài viết hiện tiêu đề, nội dung rút gọn, tác giả, ngày đăng

#### 4. Tạo bài viết (http://localhost:5000/create) - Cần đăng nhập
- Nhập tiêu đề
- Nhập nội dung
- Upload ảnh (JPG/PNG/GIF) hoặc nhập URL ảnh
- Click "Đăng bài"
- Slug tự động tạo từ tiêu đề

#### 5. Chi tiết bài viết (http://localhost:5000/post/<id>)
- Xem nội dung đầy đủ
- Viết bình luận (cần đăng nhập)
- Xem danh sách bình luận

#### 6. Blog (http://localhost:5000/blog) - Cần đăng nhập
- Danh sách bài viết dạng grid (6 bài/trang)

#### 7. About (http://localhost:5000/about) - Cần đăng nhập
- Lần đầu: Form để nhập bio, upload ảnh, email, phone, address
- Các lần sau: Hiển thị thông tin đã lưu
- Click "Lưu" để cập nhật

#### 8. Contact (http://localhost:5000/contact) - Cần đăng nhập
- Trang liên hệ

#### 9. Tìm kiếm (http://localhost:5000/search?q=xxx)
- Tìm bài viết theo tiêu đề

#### 10. Đăng xuất
- http://localhost:5000/auth/logout

### Database
- File: `instance/blog.db` (SQLite)
- Bảng: `user`, `post`, `comment`, `profile`

### Nếu cần migrate thêm (khi sửa model)
```powershell
flask db migrate -m "Add phone and address to User"
flask db upgrade
```

### Docker
```powershell
# Build
docker build -t myproject:latest .

# Chạy
docker run -d -p 5000:5000 myproject:latest

# Đóng gói
docker save -o myproject.tar myproject:latest
```

### Xử lý lỗi
```powershell
# Lỗi migration → xóa thư mục migrations và chạy lại
Remove-Item -Recurse -Force migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## KTT1 - Kiểm tra giữa kỳ 1

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\KTT1\`

### Mô tả
Ứng dụng Quản lý & Thanh toán Hóa đơn bán hàng với giao diện ttkbootstrap.

### Yêu cầu
```powershell
pip install pymysql reportlab matplotlib ttkbootstrap
```

### Bước 1: Tạo database

Chạy file `DataBase.sql`:
```sql
CREATE DATABASE IF NOT EXISTS quanly_hoadon;
USE quanly_hoadon;

CREATE TABLE khachhang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100),
    diachi VARCHAR(255),
    sdt VARCHAR(20)
);

CREATE TABLE mathang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tenhang VARCHAR(100),
    dongia FLOAT,
    donvi VARCHAR(20),
    soluong INT
);

CREATE TABLE hoadon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngaylap DATE,
    khachhang_id INT,
    tongtien FLOAT,
    FOREIGN KEY (khachhang_id) REFERENCES khachhang(id)
);

CREATE TABLE chitiethoadon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hoadon_id INT,
    mathang_id INT,
    soluong INT,
    dongia FLOAT,
    thanhtien FLOAT,
    FOREIGN KEY (hoadon_id) REFERENCES hoadon(id),
    FOREIGN KEY (mathang_id) REFERENCES mathang(id)
);
```

### Bước 2: Cấu hình

Mở `db.py`, sửa password MySQL:
```python
password="Hung2725",
```

### Bước 3: Chạy
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\KTT1
python main.py
```

### Hướng dẫn sử dụng

Giao diện chính có 5 nút:

1. **Quản lý Khách hàng** (Xanh lá):
   - Thêm: Nhập tên, địa chỉ, SĐT → click "Thêm"
   - Xóa: Chọn dòng trong bảng → click "Xóa"

2. **Quản lý Mặt hàng** (Xanh dương):
   - Thêm: Nhập tên hàng, đơn giá, đơn vị, số lượng tồn → click "Thêm"
   - Xóa: Chọn dòng → click "Xóa"

3. **Lập Hóa đơn** (Vàng):
   - Chọn khách hàng từ dropdown
   - Chọn sản phẩm, nhập số lượng, click "Thêm sản phẩm"
   - Click "Lưu & Xuất Hóa Đơn (PDF)" → tự động mở PDF

4. **Thống kê** (Vàng):
   - Chọn năm (2025)
   - Click "Xem biểu đồ" → hiện biểu đồ cột doanh thu theo tháng

5. **Thoát** (Đỏ): Đóng ứng dụng

---

## KTT2 - Kiểm tra giữa kỳ 2

**Thư mục:** `D:\Hoc_Tap\HK251\LT_Python_NC\TH\KTT2\`

### Mô tả
Chưa có giao diện GUI. Hiện chỉ có file cấu hình database (giống cấu trúc Lab 06).

### Cấu trúc
```
KTT2/
├── DataBase.sql   # Script tạo database (giống Lab 06)
└── db.py          # Kết nối MySQL
```

### Yêu cầu
```powershell
pip install pymysql
```

### Cách chạy
```powershell
cd D:\Hoc_Tap\HK251\LT_Python_NC\TH\KTT2
python -c "import db; print('OK')"
```

Cấu hình database giống Lab 06: database `minimart`, các bảng `loaisanpham`, `sanpham`, `khachhang`, `hoadon`, `chitiethoadon`.

---

## Lưu ý quan trọng

### 1. Password MySQL
Trong tất cả các file `db.py` và `GuiDBConfig.py`, password mặc định là `Hung2725`. Nếu MySQL của bạn dùng password khác, **phải sửa lại trước khi chạy**, nếu không sẽ báo lỗi kết nối.

Các file cần sửa:
- `Lab05/GuiDBConfig.py`
- `Lab06/db.py`
- `Lab006/` (không dùng MySQL)
- `KTT1/db.py`
- `KTT2/db.py`

### 2. MySQL chưa chạy
Nếu gặp lỗi:
```
Can't connect to MySQL server on '127.0.0.1' (10061)
```
→ Khởi động MySQL Server (XAMPP > MySQL > Start)

### 3. Port conflict
- Lab 06 dùng port 5050
- Lab 07-09 dùng port 5000
- Nếu port đã được dùng, sửa `app.run(port=XXXX)` trong code

### 4. Font PDF (Lab 06)
Cần file `DejaVuSans.ttf` trong cùng thư mục với `hoadon.py` để xuất PDF tiếng Việt. File này đã có sẵn.

Nếu báo lỗi font:
- Download từ: https://dejavu-fonts.github.io/
- Hoặc dùng font khác, sửa dòng `font_path` trong `hoadon.py`

### 5. Icon `pyc.ico`
Nếu không tìm thấy file icon, chương trình vẫn chạy được. Có thể comment hoặc xóa dòng:
```python
# win.iconbitmap("pyc.ico")
```

### 6. Kích hoạt venv
Nếu gặp lỗi `ModuleNotFoundError`, chưa kích hoạt venv hoặc chưa cài thư viện:
```powershell
# Kích hoạt venv (nếu có)
.\venv\Scripts\Activate.ps1

# Hoặc cài trực tiếp
pip install <tên_thư_viện>
```

### 7. Docker (Lab 08, 09)
Cần cài Docker Desktop trước: https://www.docker.com/products/docker-desktop/

### 8. Flask Debug Mode
Khi chạy với `debug=True`, code tự động reload khi sửa file.
Tắt debug khi deploy: `debug=False`

### 9. Migrations lỗi (Lab 08, 09)
Nếu gặp lỗi khi migrate, xóa thư mục `migrations/` và chạy lại từ đầu:
```powershell
Remove-Item -Recurse -Force migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 10. Thứ tự chạy lab
Nên chạy theo thứ tự từ Lab 01 → Lab 09 để kiến thức đi từ cơ bản đến nâng cao:
1. **Lab 01-04**: Tkinter GUI Desktop (cơ bản → OOP)
2. **Lab 05**: Kết nối MySQL
3. **Lab 06**: Ứng dụng tổng hợp (Tkinter + MySQL + PDF)
4. **Lab 006, 07**: Flask cơ bản
5. **Lab 08**: Flask + Database
6. **Lab 09**: Flask nâng cao
