import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from gui_khachhang import open_khachhang_window
from gui_mathang import open_mathang_window
from gui_hoadon import open_hoadon_window
from gui_thongke import open_thongke_window

def main():
    root = ttk.Window(themename="litera")
    root.title("Quản Lý & Thanh Toán Hóa Đơn Bán Hàng")
    root.iconbitmap("pyc.ico")

    ttk.Label(root, text="HỆ THỐNG QUẢN LÝ THANH TOÁN HÓA ĐƠN",
              font=("Arial", 16, "bold")).pack(pady=25)

    ttk.Button(root, text="Quản lý Khách hàng", bootstyle=SUCCESS, width=30,
               command=open_khachhang_window).pack(pady=10)
    ttk.Button(root, text="Quản lý Mặt hàng", bootstyle=INFO, width=30,
               command=open_mathang_window).pack(pady=10)
    ttk.Button(root, text="Lập Hóa đơn", bootstyle=WARNING, width=30,
               command=open_hoadon_window).pack(pady=10)
    ttk.Button(root, text="Thống kê", bootstyle=WARNING, width=30,
               command=open_thongke_window).pack(pady=10)
    ttk.Button(root, text="Thoát", bootstyle=DANGER, width=30,
               command=root.destroy).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
