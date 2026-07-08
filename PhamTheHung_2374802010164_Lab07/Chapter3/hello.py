from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/variables/<name>')
def variables_demo(name):
    user_data = {
        'email': f'{name.lower()}@example.com',
        'age': 25
    }
    hobbies = ['reading', 'programming', 'music']
    return render_template('variables_demo.html', 
                           name=name, 
                           user_data=user_data, 
                           hobbies=hobbies)

# ✅ Route cho trang DateTime Demo
@app.route('/datetime')
def datetime_demo():
    current_time = datetime.utcnow()
    return render_template('datetime_demo.html', current_time=current_time)

@app.route('/conditionals')
def conditionals():
    user = {
        'name': 'Admin User',
        'is_admin': True
    }
    return render_template('conditionals.html', user=user)

@app.route('/loops')
def loops():
    users = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'name': 'Charlie', 'email': 'charlie@example.com'}
    ]
    return render_template('loops.html', users=users)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bootstrap/user/<name>')
def bootstrap_user(name):
    return render_template('bootstrap_user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Route test lỗi 500
@app.route('/error500')
def error500():
    return 1 / 0

if __name__ == '__main__':
    app.run(debug=True)
