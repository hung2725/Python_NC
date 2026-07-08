from flask import Flask
import datetime


ungdung = Flask(__name__)


@ungdung.route('/monhoc/')
def learn():
    chuoi = "Day la trang mon hoc!"
    return chuoi


@ungdung.route('/monhoc/<tenmon>')
def subjects(tenmon):
    chuoi = "Day la trang mon hoc"
    monhoc = str(tenmon).upper()
    if monhoc == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + monhoc
    return chuoi

@ungdung.route('/monhoc/') 
def learn(): 
    chuoi = "Day la trang mon hoc!" 
    return chuoi 

@ungdung.route('/monhoc/<tenmon>') 
def subjects(tenmon): 
    chuoi = "Day la trang mon hoc" 
    monhoc = str(tenmon).upper() 
    if monhoc == "": 
        chuoi = chuoi + "!" 

    else: 
        chuoi = chuoi + " " + monhoc 
    return chuoi 


if __name__ == "__main__":
    ungdung.run(port=5050)