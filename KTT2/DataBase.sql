CREATE DATABASE IF NOT EXISTS minimart CHARACTER SET utf8mb4;
USE minimart;

CREATE TABLE loaisanpham (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tenloai VARCHAR(100)
);

CREATE TABLE sanpham (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100),
    dongia FLOAT,
    loai_id INT,
    FOREIGN KEY (loai_id) REFERENCES loaisanpham(id)
);

CREATE TABLE khachhang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100),
    sdt VARCHAR(20),
    diachi VARCHAR(200)
);

CREATE TABLE hoadon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ngaylap DATE,
    khachhang_id INT,
    tongtien FLOAT,
    FOREIGN KEY (khachhang_id) REFERENCES khachhang(id)
);

CREATE TABLE chitiethoadon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hoadon_id INT,
    sanpham_id INT,
    soluong INT,
    dongia FLOAT,
    thanhtien FLOAT,
    FOREIGN KEY (hoadon_id) REFERENCES hoadon(id),
    FOREIGN KEY (sanpham_id) REFERENCES sanpham(id)
);
