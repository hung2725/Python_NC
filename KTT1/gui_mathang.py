import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection

def open_mathang_window():
    win = tk.Toplevel()
    win.title("Quản lý Mặt Hàng")
    win.iconbitmap("pyc.ico")

    tk.Label(win, text="Tên hàng:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(win, text="Đơn giá:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(win, text="Đơn vị:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(win, text="Số lượng tồn:").grid(row=3, column=0, padx=10, pady=5)

    ten = tk.Entry(win, width=30)
    dongia = tk.Entry(win, width=30)
    donvi = tk.Entry(win, width=30)
    soluong = tk.Entry(win, width=30)
    ten.grid(row=0, column=1)
    dongia.grid(row=1, column=1)
    donvi.grid(row=2, column=1)
    soluong.grid(row=3, column=1)

    def them():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO mathang (tenhang, dongia, donvi, soluong) VALUES (%s,%s,%s,%s)", 
                    (ten.get(), dongia.get(), donvi.get(), soluong.get()))
        conn.commit()
        conn.close()
        load()
        messagebox.showinfo("Thành công", "Đã thêm mặt hàng!")

    def xoa():
        sel = tree.focus()
        if not sel: return
        id = tree.item(sel)['values'][0]
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM mathang WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        load()

    def load():
        for i in tree.get_children():
            tree.delete(i)
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM mathang")
        for row in cur.fetchall():
            tree.insert("", "end", values=row)
        conn.close()

    tk.Button(win, text="Thêm", command=them).grid(row=4, column=0, pady=5)
    tk.Button(win, text="Xóa", command=xoa).grid(row=4, column=1, pady=5)

    cols = ("ID", "Tên hàng", "Đơn giá", "Đơn vị", "Số lượng")
    tree = ttk.Treeview(win, columns=cols, show="headings")
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=130)
    tree.grid(row=5, column=0, columnspan=2, pady=10)
    load()
