import tkinter as tk
from tkinter import ttk, Menu
from khachhang import KhachHangFrame
from sanpham import SanPhamFrame
from hoadon import HoaDonFrame
from thongke import doanhthu_theo_ngay


def main():
    win = tk.Tk()
    win.title("Phần mềm Quản lý Cửa hàng - Phạm Thế Hùng 2374802010164")
    win.geometry("1000x650")
    win.iconbitmap("pyc.ico")
    win.resizable(False, False)

    title_label = ttk.Label(
        win,
        text="PHẦN MỀM QUẢN LÝ CỬA HÀNG\nPhạm Thế Hùng - 2374802010164",
        font=("Segoe UI", 18, "bold"),
        foreground="#0078D7"
    )
    title_label.pack(pady=10)

    container = ttk.Frame(win)
    container.pack(fill="both", expand=True)

    def open_frame(frame_class):
        for widget in container.winfo_children():
            widget.destroy()
        frame = frame_class(container)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

    menubar = Menu(win)
    menu_ql = Menu(menubar, tearoff=0)
    menu_ql.add_command(label="Quản lý khách hàng", command=lambda: open_frame(KhachHangFrame))
    menu_ql.add_command(label="Quản lý sản phẩm", command=lambda: open_frame(SanPhamFrame))
    menu_ql.add_separator()
    menu_ql.add_command(label="Lập hóa đơn", command=lambda: open_frame(HoaDonFrame))
    menu_ql.add_command(label="Thống kê doanh thu", command=lambda: doanhthu_theo_ngay(win, top_n=30))
    menubar.add_cascade(label="Chức năng", menu=menu_ql)
    menubar.add_command(label="Thoát", command=win.destroy)

    win.config(menu=menubar)

    frame_intro = ttk.Frame(container)
    frame_intro.pack(fill="both", expand=True)
    ttk.Label(
        frame_intro,
        text="Chào mừng bạn đến với hệ thống quản lý cửa hàng tạp hóa!",
        font=("Segoe UI", 14)
    ).pack(expand=True)

    win.mainloop()


if __name__ == "__main__":
    main()
