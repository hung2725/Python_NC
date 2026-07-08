import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection


class SanPhamFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(self, text="QUẢN LÝ SẢN PHẨM", font=("Segoe UI", 18, "bold")).pack(pady=10)
        frame_input = ttk.Frame(self)
        frame_input.pack(pady=5, fill="x")

        ttk.Label(frame_input, text="Tên:").grid(row=0, column=0, padx=5, pady=2)
        ttk.Label(frame_input, text="Đơn giá:").grid(row=0, column=2, padx=5, pady=2)
        ttk.Label(frame_input, text="Loại:").grid(row=0, column=4, padx=5, pady=2)

        self.ten_var = tk.StringVar()
        self.dongia_var = tk.StringVar()
        self.loai_var = tk.StringVar()

        ttk.Entry(frame_input, textvariable=self.ten_var, width=20).grid(row=0, column=1, padx=5)
        ttk.Entry(frame_input, textvariable=self.dongia_var, width=15).grid(row=0, column=3, padx=5)
        ttk.Entry(frame_input, textvariable=self.loai_var, width=25).grid(row=0, column=5, padx=5)

        ttk.Button(frame_input, text="Thêm", command=self.them_sp).grid(row=0, column=6, padx=5)
        ttk.Button(frame_input, text="Sửa", command=self.sua_sp).grid(row=0, column=7, padx=5)
        ttk.Button(frame_input, text="Xóa", command=self.xoa_sp).grid(row=0, column=8, padx=5)
        self.table = ttk.Treeview(
            self,
            columns=("id", "ten", "dongia", "loai"),
            show="headings",
            height=12
        )

        self.table.heading("id", text="Mã SP")
        self.table.heading("ten", text="Tên sản phẩm")
        self.table.heading("dongia", text="Đơn giá")
        self.table.heading("loai", text="Loại")

        self.table.column("id", width=80, anchor="center")
        self.table.column("ten", width=200, anchor="w")
        self.table.column("dongia", width=100, anchor="center")
        self.table.column("loai", width=150, anchor="center")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.table.pack(fill="both", expand=True, pady=10)
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        self.load_data()

    def load_data(self):
        self.table.delete(*self.table.get_children())
        conn = get_connection()
        if not conn:
            messagebox.showerror("Lỗi", "Không kết nối được CSDL")
            return

        cur = conn.cursor()
        cur.execute("""
            SELECT sp.id, sp.ten, sp.dongia, lp.tenloai 
            FROM sanpham sp
            LEFT JOIN loaisanpham lp ON sp.loai_id = lp.id
        """)
        for row in cur.fetchall():
            self.table.insert("", "end", values=row)
        conn.close()

    def on_select(self, event):
        selected = self.table.focus()
        if selected:
            values = self.table.item(selected, "values")
            self.ten_var.set(values[1])
            self.dongia_var.set(values[2])
            self.loai_var.set(values[3])
    def them_sp(self):
        ten = self.ten_var.get().strip()
        try:
            dongia = float(self.dongia_var.get())
        except ValueError:
            messagebox.showwarning("Lỗi dữ liệu", "Đơn giá phải là số hợp lệ!")
            return

        loai_text = self.loai_var.get().strip()
        if not ten or not loai_text:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ tên và loại sản phẩm!")
            return

        conn = get_connection()
        if not conn:
            messagebox.showerror("Lỗi", "Không kết nối được CSDL")
            return
        cur = conn.cursor()

        cur.execute("SELECT id FROM loaisanpham WHERE tenloai=%s", (loai_text,))
        result = cur.fetchone()
        if result:
            loai_id = result[0]
        else:
            cur.execute("INSERT INTO loaisanpham (tenloai) VALUES (%s)", (loai_text,))
            conn.commit()
            loai_id = cur.lastrowid

        cur.execute(
            "INSERT INTO sanpham (ten, dongia, loai_id) VALUES (%s, %s, %s)",
            (ten, dongia, loai_id)
        )
        conn.commit()
        conn.close()

        messagebox.showinfo("Thành công", f"Đã thêm sản phẩm '{ten}'!")
        self.load_data()
        self.clear_input()
    def sua_sp(self):
        selected = self.table.focus()
        if not selected:
            messagebox.showwarning("Chọn sản phẩm", "Vui lòng chọn sản phẩm để sửa")
            return

        sp_id = self.table.item(selected, "values")[0]
        ten = self.ten_var.get().strip()
        try:
            dongia = float(self.dongia_var.get())
        except ValueError:
            messagebox.showwarning("Lỗi dữ liệu", "Đơn giá phải là số")
            return

        loai_text = self.loai_var.get().strip()
        if not loai_text:
            messagebox.showwarning("Thiếu dữ liệu", "Nhập loại sản phẩm!")
            return

        conn = get_connection()
        if not conn:
            messagebox.showerror("Lỗi", "Không kết nối được CSDL")
            return

        cur = conn.cursor()

        cur.execute("SELECT id FROM loaisanpham WHERE tenloai=%s", (loai_text,))
        result = cur.fetchone()
        if result:
            loai_id = result[0]
        else:
            cur.execute("INSERT INTO loaisanpham (tenloai) VALUES (%s)", (loai_text,))
            conn.commit()
            loai_id = cur.lastrowid

        cur.execute(
            "UPDATE sanpham SET ten=%s, dongia=%s, loai_id=%s WHERE id=%s",
            (ten, dongia, loai_id, sp_id)
        )
        conn.commit()
        conn.close()

        messagebox.showinfo("Thành công", f"Đã sửa sản phẩm '{ten}'!")
        self.load_data()
        self.clear_input()
    def xoa_sp(self):
        selected = self.table.focus()
        if not selected:
            messagebox.showwarning("Chọn sản phẩm", "Vui lòng chọn sản phẩm để xóa")
            return

        sp_id = self.table.item(selected, "values")[0]
        if messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa sản phẩm này?"):
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM sanpham WHERE id=%s", (sp_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Thành công", "Đã xóa sản phẩm!")
            self.load_data()
            self.clear_input()
    def clear_input(self):
        self.ten_var.set("")
        self.dongia_var.set("")
        self.loai_var.set("")
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý sản phẩm")
    root.geometry("850x500")
    app = SanPhamFrame(root)
    root.mainloop()
