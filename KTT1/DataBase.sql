CREATE DATABASE IF NOT EXISTS quanly_hoadon;
USE quanly_hoadon;

CREATE TABLE khachhang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten VARCHAR(100),
    diachi VARCHAR(255),
    sdt VARCHAR(20)
);

CREATE TABLE mathang (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tenhang VARCHAR(100),
    dongia FLOAT,
    donvi VARCHAR(20),
    soluong INT
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
    mathang_id INT,
    soluong INT,
    dongia FLOAT,
    thanhtien FLOAT,
    FOREIGN KEY (hoadon_id) REFERENCES hoadon(id),
    FOREIGN KEY (mathang_id) REFERENCES mathang(id)
);
