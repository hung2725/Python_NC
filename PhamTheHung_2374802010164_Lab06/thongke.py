import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime


def doanhthu_theo_ngay(master=None, top_n=30):
    # Kết nối CSDL
    conn = get_connection()
    if not conn:
        messagebox.showerror("Lỗi kết nối", "Không thể kết nối đến cơ sở dữ liệu!")
        return

    cur = conn.cursor()
    cur.execute("SELECT ngaylap, tongtien FROM hoadon")
    data = cur.fetchall()
    conn.close()

    # Nếu không có dữ liệu
    if not data:
        messagebox.showinfo("Thông báo", "Chưa có dữ liệu hóa đơn!")
        return

    # Xử lý dữ liệu
    doanhthu = {}
    for ngay, tien in data:
        if isinstance(ngay, str):
            ngay_dt = datetime.strptime(ngay, "%Y-%m-%d")
        else:
            ngay_dt = ngay
        ngay_str = ngay_dt.strftime("%Y-%m-%d")
        doanhthu[ngay_str] = doanhthu.get(ngay_str, 0) + tien

    ngay_hien = sorted(doanhthu.keys())
    tiens = [doanhthu[ngay] for ngay in ngay_hien]
    if len(ngay_hien) > top_n:
        ngay_hien = ngay_hien[-top_n:]
        tiens = tiens[-top_n:]
    chart_win = tk.Toplevel(master)
    chart_win.title("Biểu đồ doanh thu theo ngày - Phạm Thế Hùng 2374802010164")
    chart_win.iconbitmap("pyc.ico")
    chart_win.geometry("900x500")
    chart_win.resizable(False, False)

    lbl_title = ttk.Label(chart_win, text="BIỂU ĐỒ DOANH THU THEO NGÀY", font=("Segoe UI", 16, "bold"))
    lbl_title.pack(pady=10)

    fig, ax = plt.subplots(figsize=(8, 3.5))  #giảm chiều dọc để không tràn
    ax.plot(ngay_hien, tiens, color='green', marker='o', linewidth=2)
    ax.fill_between(ngay_hien, tiens, color='lightgreen', alpha=0.4)
    ax.set_title(f"Doanh thu {top_n} ngày gần nhất", fontsize=13, pad=10)
    ax.set_xlabel("Ngày lập", fontsize=11)
    ax.set_ylabel("Doanh thu (VND)", fontsize=11)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True, linestyle='--', alpha=0.5)

    for x, y in zip(ngay_hien, tiens):
        ax.text(x, y + 0.02 * max(tiens), f"{int(y):,}", ha='center', fontsize=8)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=chart_win)
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=5)
    canvas.draw()

    btn_close = ttk.Button(chart_win, text="Đóng", command=chart_win.destroy)
    btn_close.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Thống kê doanh thu")
    root.geometry("400x250")
    root.resizable(False, False)

    ttk.Label(root, text="THỐNG KÊ DOANH THU", font=("Segoe UI", 16, "bold")).pack(pady=20)
    ttk.Button(root, text="Xem biểu đồ", width=20, command=lambda: doanhthu_theo_ngay(root, top_n=30)).pack(pady=10)
    ttk.Button(root, text="Thoát", width=20, command=root.destroy).pack(pady=10)

    root.mainloop()
 