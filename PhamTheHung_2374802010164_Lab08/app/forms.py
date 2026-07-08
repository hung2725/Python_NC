from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[
        DataRequired(message='Tiêu đề là bắt buộc'),
        Length(min=5, max=200, message='Tiêu đề phải từ 5-200 ký tự')
    ])
    
    content = TextAreaField('Nội dung', validators=[
        DataRequired(message='Nội dung là bắt buộc'),
        Length(min=10, message='Nội dung phải ít nhất 10 ký tự')
    ])
    
    submit = SubmitField('Đăng bài')

from wtforms import PasswordField
from wtforms.validators import Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[
        DataRequired(),
        Length(min=4, max=20)
    ])
    
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    
    password = PasswordField('Mật khẩu', validators=[
        DataRequired(),
        Length(min=6)
    ])
    
    password2 = PasswordField('Xác nhận mật khẩu', validators=[
        DataRequired(),
        EqualTo('password', message='Mật khẩu không khớp')
    ])
    
    submit = SubmitField('Đăng ký')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Tên đăng nhập đã tồn tại')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email đã được sử dụng')
        
from wtforms import BooleanField

class LoginForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[DataRequired()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    remember_me = BooleanField('Ghi nhớ đăng nhập')
    submit = SubmitField('Đăng nhập')

class CommentForm(FlaskForm):
    content = TextAreaField('Nội dung bình luận', validators=[
        DataRequired(message='Vui lòng nhập bình luận'),
        Length(min=3, message='Bình luận phải có ít nhất 3 ký tự')
    ])
    submit = SubmitField('Gửi bình luận')
