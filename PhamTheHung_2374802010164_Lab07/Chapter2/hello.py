from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Hello World!</h1>
        <h2>Phạm Thế Hùng - 2374802010164</h2>
        <h3>Lớp: 251_71ITSE31003_0103</h3>
    '''
from flask import Flask, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/info')
def info():
    user_agent = request.headers.get('User-Agent')
    return '''
    <h2>Request Information</h2>
    <p><strong>Method:</strong> {}</p>
    <p><strong>URL:</strong> {}</p>
    <p><strong>User-Agent:</strong> {}</p>
    <p><strong>Remote IP:</strong> {}</p>
    '''.format(request.method, request.url, user_agent, request.remote_addr)

@app.route('/cookie')
def set_cookie():
    response = make_response('<h1>Cookie has been set!</h1>')
    response.set_cookie('username', 'flask_user')
    return response

@app.route('/redirect-test')
def redirect_test():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
