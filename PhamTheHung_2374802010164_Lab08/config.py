import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Pagination settings
    POSTS_PER_PAGE = 5
    
    # Flask-WTF settings
    WTF_CSRF_TIME_LIMIT = int(timedelta(hours=1).total_seconds())

