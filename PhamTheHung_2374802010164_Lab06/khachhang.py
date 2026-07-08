import tkinter as tk
from tkinter import ttk, messagebox
import pymysql.cursors
from db import get_connection


class KhachHangFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True, padx=10, pady=10)
        ttk.Label(self, text="QUẢN LÝ KHÁCH HÀNG", font=("Segoe UI", 18, "bold")).pack(pady=10)

        frame_input = ttk.Frame(self)
        frame_input.pack(pady=5, fill="x")

        ttk.Label(frame_input, text="Tên:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        ttk.Label(frame_input, text="SĐT:").grid(row=0, column=2, padx=5, pady=2, sticky="e")
        ttk.Label(frame_input, text="Địa chỉ:").grid(row=0, column=4, padx=4, pady=2, sticky="e")

        self.ten_var = tk.StringVar()
        self.sdt_var = tk.StringVar()
        self.diachi_var = tk.StringVar()

        ttk.Entry(frame_input, textvariable=self.ten_var, width=25).grid(row=0, column=1, padx=5)
        ttk.Entry(frame_input, textvariable=self.sdt_var, width=18).grid(row=0, column=3, padx=5)
        ttk.Entry(frame_input, textvariable=self.diachi_var, width=30).grid(row=0, column=5, padx=5)

        ttk.Button(frame_input, text="Thêm", command=self.them_khach).grid(row=0, column=6, padx=5)
        ttk.Button(frame_input, text="Sửa", command=self.sua_khach).grid(row=0, column=7, padx=5)
        ttk.Button(frame_input, text="Xóa", command=self.xoa_khach).grid(row=0, column=8, padx=5)

        self.table = ttk.Treeview(
            self,
            columns=("id", "ten", "sdt", "diachi"),
            show="headings"
        )

        cols = ("id", "ten", "sdt", "diachi")
        titles = ("Mã KH", "Tên khách hàng", "SĐT", "Địa chỉ")
        for c, t in zip(cols, titles):
            self.table.heading(c, text=t)
            if c == "ten":
                self.table.column(c, width=220, anchor="w")
            elif c == "diachi":
                self.table.column(c, width=100, anchor="w")
            else:
                self.table.column(c, width=100, anchor="center")
        scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scroll_y.set)
        scroll_y.pack(side="right", fill="y")

        self.table.pack(fill="both", expand=True, pady=10)
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        self.load_data()
    def load_data(self):
        self.table.delete(*self.table.get_children())
        conn = get_connection()
        if not conn:
            messagebox.showerror("Lỗi kết nối", "Không thể kết nối tới CSDL. Kiểm tra db.py và thông tin kết nối.")
            return
        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute("SELECT id, ten, sdt, diachi FROM khachhang ORDER BY id DESC")
            rows = cur.fetchall()
            for row in rows:
                self.table.insert("", "end", values=(row["id"], row["ten"], row["sdt"], row["diachi"]))
        except Exception as e:
            messagebox.showerror("Lỗi SQL", f"Lỗi khi truy vấn dữ liệu:\n{e}")
        finally:
            conn.close()

    def on_select(self, event):
        selected = self.table.focus()
        if selected:
            values = self.table.item(selected, "values")
            self.ten_var.set(values[1])
            self.sdt_var.set(values[2])
            self.diachi_var.set(values[3])

    def them_khach(self):
        ten, sdt, diachi = self.ten_var.get().strip(), self.sdt_var.get().strip(), self.diachi_var.get().strip()
        if not ten:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên khách hàng")
            return
        conn = get_connection()
        if not conn:
            messagebox.showerror("Lỗi kết nối", "Không thể kết nối tới CSDL.")
            return
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO khachhang (ten, sdt, diachi) VALUES (%s, %s, %s)", (ten, sdt, diachi))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Lỗi thêm", f"Không thể thêm khách hàng:\n{e}")
        finally:
            conn.close()
        self.load_data()
        self.clear_input()
    def sua_khach(self):
        selected = self.table.focus()
        if not selected:
            messagebox.showwarning("Chọn khách", "Vui lòng chọn khách hàng để sửa")
            return
        kh_id = self.table.item(selected, "values")[0]
        ten, sdt, diachi = self.ten_var.get().strip(), self.sdt_var.get().strip(), self.diachi_var.get().strip()
        if not ten:
            messagebox.showwarning("Thiếu dữ liệu", "Tên không được để trống")
            return
        conn = get_connection()
        if not conn:
            messagebox.showerror("Lỗi kết nối", "Không thể kết nối tới CSDL.")
            return
        try:
            cur = conn.cursor()
            cur.execute("UPDATE khachhang SET ten=%s, sdt=%s, diachi=%s WHERE id=%s", (ten, sdt, diachi, kh_id))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Lỗi sửa", f"Không thể cập nhật khách hàng:\n{e}")
        finally:
            conn.close()
        self.load_data()
        self.clear_input()

    def xoa_khach(self):
        selected = self.table.focus()
        if not selected:
            messagebox.showwarning("Chọn khách", "Vui lòng chọn khách hàng để xóa")
            return
        kh_id = self.table.item(selected, "values")[0]
        if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa khách hàng này?"):
            return
        conn = get_connection()
        if not conn:
            messagebox.showerror("Lỗi kết nối", "Không thể kết nối tới CSDL.")
            return
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM khachhang WHERE id=%s", (kh_id,))
            conn.commit()
        except Exception as e:
            messagebox.showerror("Lỗi xóa", f"Không thể xóa khách hàng:\n{e}")
        finally:
            conn.close()
        self.load_data()
        self.clear_input()

    def clear_input(self):
        self.ten_var.set("")
        self.sdt_var.set("")
        self.diachi_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Khách hàng")
    root.geometry("900x600")
    KhachHangFrame(root)
    root.mainloop()
