from flask import Flask, render_template # Bắt buộc phải import render_template
import datetime 

ungdung = Flask(__name__)

# --- Bài 4: Trang chủ ('/') ---
@ungdung.route('/')
def hello():
    tentruong = 'Đại học Van Lang!' 
    lienket = '<a href="https://www.vanlanguni.edu.vn">' + tentruong + '</a><br>'
    
    chuoi = lienket 
    nam = datetime.date.today().year 

    # Đã sửa lỗi: 'Xin' in đậm, 'chao!' in đậm và in nghiêng
    chuoi = chuoi + '<b>Xin </b><b><i>chao!</i></b> Tan sinh vien nam ' + str(nam) + '!'
    
    return chuoi

# --- Bài 5: Trang tĩnh '/monhoc' ---
@ungdung.route('/monhoc', strict_slashes=False)
def learn():
    return "Day la trang mon hoc!"

# --- Bài 7: SỬA HÀM SUBJECTS (Dùng Template) ---
@ungdung.route('/monhoc/<tenmon>')
def subjects(tenmon):
    """Xử lý route /monhoc/<tenmon> và hiển thị qua template."""
    # Truyền biến 'tenmon' sau khi in hoa vào template với tên 'name'
    return render_template('hello_template.html', name=tenmon.upper())

# --- Bài 6: Định tuyến Động Sinh viên ---
@ungdung.route('/sinhvien/')
@ungdung.route('/sinhvien')
def students_index():
    """Xử lý route tĩnh /sinhvien/ (tránh lỗi TypeError)"""
    return "Trang chi muc Sinh Vien. Vui long nhap nam hoc vao URL, vi du: /sinhvien/2025" 

@ungdung.route('/sinhvien/<int:namhoc>')
def school_year(namhoc):
    """Xử lý route /sinhvien/<namhoc>"""
    chuoi = "Day la trang sinh vien nam " 
    nam = str(namhoc)
    return chuoi + nam

# --- Chạy Ứng dụng trên Cổng 5050 ---
if __name__ == "__main__":
    ungdung.run(port=5050)