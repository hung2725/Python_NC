import tkinter as tk
from tkinter import ttk
from db import get_connection
import matplotlib.pyplot as plt

def open_thongke_window():
    win = tk.Toplevel()
    win.title("Thống kê Doanh thu")
    win.iconbitmap("pyc.ico")

    tk.Label(win, text="Chọn Năm:", font=("Arial", 11)).pack(pady=10)
    cb_nam = ttk.Combobox(win, values=[2025], width=10)
    cb_nam.pack(pady=5)
    cb_nam.set(2025)

    def xem_bieudo():
        nam = cb_nam.get()
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT MONTH(ngaylap) AS thang, SUM(tongtien)
            FROM hoadon
            WHERE YEAR(ngaylap)=%s
            GROUP BY MONTH(ngaylap)
            ORDER BY thang
        """, (nam,))
        data = cur.fetchall()
        conn.close()

        if not data:
            tk.messagebox.showinfo("Thông báo", "Không có dữ liệu doanh thu cho năm này!")
            return

        thang = [str(r[0]) for r in data]
        doanhthu = [r[1] for r in data]

        plt.figure(figsize=(8,5))
        plt.bar(thang, doanhthu)
        plt.title(f"Doanh thu theo tháng năm {nam}")
        plt.xlabel("Tháng")
        plt.ylabel("Doanh thu (VND)")
        plt.show()

    tk.Button(win, text="Xem biểu đồ", command=xem_bieudo).pack(pady=20)
