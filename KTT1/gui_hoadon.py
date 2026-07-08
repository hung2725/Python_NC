import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def open_hoadon_window():
    win = tk.Toplevel()
    win.title("Lập Hóa Đơn")
    win.iconbitmap("pyc.ico")

    tk.Label(win, text="Khách hàng:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Sản phẩm:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(win, text="Số lượng:").grid(row=2, column=0, padx=10, pady=5)

    cb_khach = ttk.Combobox(win, width=30)
    cb_sp = ttk.Combobox(win, width=30)
    txt_sl = tk.Entry(win, width=10)
    cb_khach.grid(row=0, column=1)
    cb_sp.grid(row=1, column=1)
    txt_sl.grid(row=2, column=1)

    def load_combobox():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, ten FROM khachhang")
        cb_khach["values"] = [f"{r[0]} - {r[1]}" for r in cur.fetchall()]
        cur.execute("SELECT id, tenhang FROM mathang")
        cb_sp["values"] = [f"{r[0]} - {r[1]}" for r in cur.fetchall()]
        conn.close()

    items = []

    def them_sp():
        if not cb_sp.get() or not txt_sl.get():
            return
        sp_id = int(cb_sp.get().split(" - ")[0])
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT tenhang, dongia FROM mathang WHERE id=%s", (sp_id,))
        ten, gia = cur.fetchone()
        sl = int(txt_sl.get())
        thanhtien = sl * gia
        items.append((sp_id, ten, sl, gia, thanhtien))
        tree.insert("", "end", values=(ten, sl, gia, thanhtien))
        conn.close()
        tinh_tong()

    def tinh_tong():
        tong = sum([x[4] for x in items])
        lbl_tong.config(text=f"Tổng tiền: {tong:,.0f} VND")

    def xuat_pdf(mahd, khachhang, tongtien):
        filename = f"hoadon_{mahd}.pdf"
        c = canvas.Canvas(filename, pagesize=A4)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(200, 800, "HÓA ĐƠN THANH TOÁN")

        c.setFont("Helvetica", 12)
        c.drawString(50, 770, f"Mã hóa đơn: {mahd}")
        c.drawString(50, 750, f"Khách hàng: {khachhang}")
        c.drawString(50, 730, f"Ngày lập: {date.today()}")

        y = 700
        c.drawString(50, y, "Tên sản phẩm")
        c.drawString(250, y, "Số lượng")
        c.drawString(350, y, "Đơn giá")
        c.drawString(450, y, "Thành tiền")
        y -= 20

        for it in items:
            c.drawString(50, y, str(it[1]))
            c.drawString(250, y, str(it[2]))
            c.drawString(350, y, f"{it[3]:,.0f}")
            c.drawString(450, y, f"{it[4]:,.0f}")
            y -= 20

        c.setFont("Helvetica-Bold", 12)
        c.drawString(400, y - 20, f"Tổng cộng: {tongtien:,.0f} VND")

        c.save()
        os.startfile(filename)
        messagebox.showinfo("Xuất PDF", f"Đã lưu hóa đơn ra file {filename}")

    def luu_hoadon():
        if not cb_khach.get() or len(items) == 0:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng chọn khách hàng và thêm sản phẩm!")
            return
        kh_id = int(cb_khach.get().split(" - ")[0])
        kh_ten = cb_khach.get().split(" - ")[1]
        tong = sum([x[4] for x in items])
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO hoadon (ngaylap, khachhang_id, tongtien) VALUES (%s,%s,%s)",
                    (date.today(), kh_id, tong))
        hoadon_id = cur.lastrowid
        for it in items:
            cur.execute("""INSERT INTO chitiethoadon (hoadon_id, mathang_id, soluong, dongia, thanhtien)
                           VALUES (%s,%s,%s,%s,%s)""", (hoadon_id, it[0], it[2], it[3], it[4]))
        conn.commit()
        conn.close()
        xuat_pdf(hoadon_id, kh_ten, tong)
        messagebox.showinfo("Thành công", "Đã lưu hóa đơn thành công!")
        win.destroy()

    tk.Button(win, text="Thêm sản phẩm", command=them_sp).grid(row=3, column=1, pady=5)

    cols = ("Tên SP", "Số lượng", "Đơn giá", "Thành tiền")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=150)
    tree.grid(row=4, column=0, columnspan=3, pady=10)

    lbl_tong = tk.Label(win, text="Tổng tiền: 0 VND", font=("Arial", 12, "bold"))
    lbl_tong.grid(row=5, column=0, columnspan=2, pady=10)

    tk.Button(win, text="Lưu & Xuất Hóa Đơn (PDF)", command=luu_hoadon).grid(row=6, column=1, pady=10)

    load_combobox()
