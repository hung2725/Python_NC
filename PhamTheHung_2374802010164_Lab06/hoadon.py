import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
from db import get_connection


class HoaDonFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        ttk.Label(
            self,
            text="LẬP HÓA ĐƠN BÁN HÀNG",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=10)

        self.khach_var = tk.StringVar()
        self.sp_var = tk.StringVar()
        self.sl_var = tk.StringVar(value="1")
        self.items = []

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        self.tab_lap = ttk.Frame(notebook)
        self.tab_ls = ttk.Frame(notebook)
        notebook.add(self.tab_lap, text="Lập hóa đơn")
        notebook.add(self.tab_ls, text="Lịch sử hóa đơn")

        self.build_tab_lap()
        self.build_tab_ls()

        self.load_combobox_data()
        self.load_lichsu_hoadon()

    def build_tab_lap(self):
        frame_top = ttk.Frame(self.tab_lap)
        frame_top.pack(pady=5)

        ttk.Label(frame_top, text="Khách hàng:").grid(row=0, column=0, padx=5, pady=3)
        self.cb_khach = ttk.Combobox(frame_top, textvariable=self.khach_var, width=30, state="readonly")
        self.cb_khach.grid(row=0, column=1, padx=5)

        ttk.Label(frame_top, text="Sản phẩm:").grid(row=1, column=0, padx=5, pady=3)
        self.cb_sp = ttk.Combobox(frame_top, textvariable=self.sp_var, width=30, state="readonly")
        self.cb_sp.grid(row=1, column=1, padx=5)

        ttk.Label(frame_top, text="Số lượng:").grid(row=1, column=2, padx=5)
        ttk.Entry(frame_top, textvariable=self.sl_var, width=8).grid(row=1, column=3, padx=5)

        ttk.Button(frame_top, text="Thêm sản phẩm", command=self.them_sp)\
            .grid(row=1, column=4, padx=10)

        frame_table = ttk.Frame(self.tab_lap)
        frame_table.pack(fill="both", expand=True, pady=10)

        cols = ("Tên SP", "Số lượng", "Đơn giá", "Thành tiền")
        self.tree = ttk.Treeview(frame_table, columns=cols, show="headings", height=6)
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor="center", width=120)
        self.tree.pack(fill="both", expand=True)

        self.lbl_tong = ttk.Label(
            self.tab_lap,
            text="Tổng tiền: 0 VND",
            font=("Segoe UI", 12, "bold"),
            foreground="red"
        )
        self.lbl_tong.pack(pady=5)

        ttk.Button(
            self.tab_lap,
            text="Lưu & Xuất Hóa Đơn (PDF)",
            command=self.luu_hoadon
        ).pack(pady=5)

    def build_tab_ls(self):
        frame = ttk.Frame(self.tab_ls)
        frame.pack(fill="both", expand=True, pady=10)

        cols = ("Mã HĐ", "Ngày lập", "Khách hàng", "Tổng tiền")
        self.tree_ls = ttk.Treeview(frame, columns=cols, show="headings", height=8)
        for c in cols:
            self.tree_ls.heading(c, text=c)
            self.tree_ls.column(c, anchor="center", width=150)
        self.tree_ls.pack(side="left", fill="both", expand=True)

        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree_ls.yview)
        self.tree_ls.configure(yscroll=scroll.set)
        scroll.pack(side="right", fill="y")

        self.tree_ls.bind("<<TreeviewSelect>>", self.xem_chi_tiet_hoadon)

        ttk.Label(
            self.tab_ls,
            text="CHI TIẾT HÓA ĐƠN",
            font=("Segoe UI", 12, "bold"),
            foreground="blue"
        ).pack(pady=5)

        cols_ct = ("Tên SP", "Số lượng", "Đơn giá", "Thành tiền")
        self.tree_ct = ttk.Treeview(self.tab_ls, columns=cols_ct, show="headings", height=8)
        for c in cols_ct:
            self.tree_ct.heading(c, text=c)
            self.tree_ct.column(c, anchor="center", width=130)
        self.tree_ct.pack(fill="both", expand=True, pady=5)

    def load_combobox_data(self):
        conn = get_connection()
        if not conn:
            messagebox.showerror("Lỗi", "Không kết nối được CSDL!")
            return
        with conn.cursor() as cur:
            cur.execute("SELECT id, ten FROM khachhang")
            khach = cur.fetchall()
            self.cb_khach["values"] = [f"{k[0]} - {k[1]}" for k in khach]

            cur.execute("SELECT id, ten, dongia FROM sanpham")
            sp = cur.fetchall()
            self.cb_sp["values"] = [f"{s[0]} - {s[1]}" for s in sp]
            self.sanpham_dict = {s[0]: (s[1], s[2]) for s in sp}
        conn.close()

    def them_sp(self):
        if not self.sp_var.get() or not self.sl_var.get().isdigit():
            messagebox.showwarning("Thiếu dữ liệu", "Chọn sản phẩm và nhập số lượng hợp lệ!")
            return

        sp_id = int(self.sp_var.get().split(" - ")[0])
        ten, gia = self.sanpham_dict[sp_id]
        sl = int(self.sl_var.get())
        thanhtien = sl * gia

        self.items.append((sp_id, ten, sl, gia, thanhtien))
        self.refresh_table()

    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        tong = 0
        for _, ten, sl, gia, tt in self.items:
            self.tree.insert("", "end", values=(ten, sl, f"{gia:,.0f}", f"{tt:,.0f}"))
            tong += tt
        self.lbl_tong.config(text=f"Tổng tiền: {tong:,.0f} VND")

    def luu_hoadon(self):
        if not self.khach_var.get() or not self.items:
            messagebox.showwarning("Thiếu dữ liệu", "Chọn khách hàng và sản phẩm trước khi lưu!")
            return

        kh_id = int(self.khach_var.get().split(" - ")[0])
        kh_ten = self.khach_var.get().split(" - ")[1]
        tongtien = sum(tt for *_, tt in self.items)

        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO hoadon (ngaylap, khachhang_id, tongtien) VALUES (%s, %s, %s)",
                (date.today(), kh_id, tongtien)
            )
            hd_id = cur.lastrowid

            for sp_id, _, sl, gia, tt in self.items:
                cur.execute(
                    """INSERT INTO chitiethoadon (hoadon_id, sanpham_id, soluong, dongia, thanhtien)
                       VALUES (%s, %s, %s, %s, %s)""",
                    (hd_id, sp_id, sl, gia, tt)
                )
        conn.commit()
        conn.close()

        try:
            self.xuat_pdf(hd_id, kh_ten, self.items, tongtien)
            messagebox.showinfo("Thành công", f"Đã lưu hóa đơn {hd_id}!\nTổng: {tongtien:,.0f} VND")
        except FileNotFoundError:
            messagebox.showerror("Lỗi", "Không tìm thấy font DejaVuSans.ttf.\nHãy đặt file này cùng thư mục dự án.")
            return

        self.items.clear()
        self.refresh_table()
        self.load_lichsu_hoadon()

    def xuat_pdf(self, mahd, kh_ten, items, tongtien):
        filename = f"hoadon_{mahd}.pdf"
        font_path = "DejaVuSans.ttf"
        pdfmetrics.registerFont(TTFont("DejaVu", font_path))

        c = canvas.Canvas(filename, pagesize=A4)
        c.setFont("DejaVu", 16)
        c.drawString(180, 800, "HÓA ĐƠN BÁN HÀNG")
        c.setFont("DejaVu", 12)
        c.drawString(50, 770, f"Mã hóa đơn: {mahd}")
        c.drawString(50, 750, f"Khách hàng: {kh_ten}")
        c.drawString(50, 730, f"Ngày lập: {date.today()}")

        y = 700
        c.drawString(50, y, "Tên sản phẩm")
        c.drawString(250, y, "Số lượng")
        c.drawString(350, y, "Đơn giá")
        c.drawString(450, y, "Thành tiền")
        y -= 20

        for it in items:
            c.drawString(50, y, it[1])
            c.drawString(250, y, str(it[2]))
            c.drawString(350, y, f"{it[3]:,.0f}")
            c.drawString(450, y, f"{it[4]:,.0f}")
            y -= 20

        c.setFont("DejaVu", 12)
        c.drawString(400, y - 20, f"Tổng cộng: {tongtien:,.0f} VND")
        c.save()

        try:
            os.startfile(filename)
        except AttributeError:
            messagebox.showinfo("Xuất PDF", f"Đã lưu hóa đơn ra file {filename}")

    def load_lichsu_hoadon(self):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT h.id, h.ngaylap, k.ten, h.tongtien
                FROM hoadon h
                JOIN khachhang k ON h.khachhang_id = k.id
                ORDER BY h.id DESC
            """)
            rows = cur.fetchall()
        conn.close()

        self.tree_ls.delete(*self.tree_ls.get_children())
        for r in rows:
            self.tree_ls.insert("", "end", values=(r[0], r[1], r[2], f"{r[3]:,.0f}"))

    def xem_chi_tiet_hoadon(self, event):
        selected = self.tree_ls.focus()
        if not selected:
            return

        mahd = self.tree_ls.item(selected)["values"][0]
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT s.ten, c.soluong, c.dongia, c.thanhtien
                FROM chitiethoadon c
                JOIN sanpham s ON c.sanpham_id = s.id
                WHERE c.hoadon_id = %s
            """, (mahd,))
            rows = cur.fetchall()
        conn.close()

        self.tree_ct.delete(*self.tree_ct.get_children())
        for r in rows:
            self.tree_ct.insert("", "end", values=(r[0], r[1], f"{r[2]:,.0f}", f"{r[3]:,.0f}"))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Hóa đơn")
    root.geometry("850x600")
    HoaDonFrame(root)
    root.mainloop()
