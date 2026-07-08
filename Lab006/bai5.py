from flask import Flask
import datetime


ungdung = Flask(__name__)


@ungdung.route('/')
def hello():
    tentruong = 'Đại học Van Lang!'
    lienket = '<a href="https://www.vlu.edu.vn">' + tentruong + '</a><br>'
    chuoi = lienket
    nam = datetime.date.today().year
    chuoi = chuoi + '<b>Xin </b><b><i>chao!</i></b> Tan sinh vien nam ' + str(nam) + '!'
    return chuoi


@ungdung.route('/monhoc')
def learn():

    return "Day la trang mon hoc!"


if __name__ == "__main__":
    ungdung.run(port=5050)