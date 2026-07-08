from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'hard-to-guess-string')

@app.route('/')
def index():
    return '''
        <h1>Hello World!</h1>
        <h2>Phạm Thế Hùng - 2374802010164</h2>
        <h3>Lớp: 251_71ITSE31003_0103</h3>
        <p>Flask is working!</p>
    '''

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1><p>Chào mừng bạn đến với Flask app.</p>'

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ['true', '1']
    app.run(debug=debug_mode, host='127.0.0.1', port=5000)
