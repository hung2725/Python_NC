import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection

def open_khachhang_window():
    win = tk.Toplevel()
    win.title("Quản lý Khách Hàng")
    win.iconbitmap("pyc.ico")

    tk.Label(win, text="Tên KH:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Địa chỉ:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(win, text="SĐT:").grid(row=2, column=0, padx=10, pady=5)

    ten = tk.Entry(win, width=30)
    diachi = tk.Entry(win, width=30)
    sdt = tk.Entry(win, width=30)
    ten.grid(row=0, column=1)
    diachi.grid(row=1, column=1)
    sdt.grid(row=2, column=1)

    def them():
        if not ten.get():
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên khách hàng")
            return
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO khachhang (ten, diachi, sdt) VALUES (%s,%s,%s)", 
                    (ten.get(), diachi.get(), sdt.get()))
        conn.commit()
        conn.close()
        load()
        messagebox.showinfo("Thành công", "Đã thêm khách hàng!")

    def xoa():
        selected = tree.focus()
        if not selected:
            return
        id = tree.item(selected)['values'][0]
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM khachhang WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        load()

    def load():
        for i in tree.get_children():
            tree.delete(i)
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM khachhang")
        for row in cur.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

    tk.Button(win, text="Thêm", command=them).grid(row=3, column=0, pady=5)
    tk.Button(win, text="Xóa", command=xoa).grid(row=3, column=1, pady=5)

    cols = ("ID", "Tên KH", "Địa chỉ", "SĐT")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=150)
    tree.grid(row=4, column=0, columnspan=2, pady=10)
    load()
