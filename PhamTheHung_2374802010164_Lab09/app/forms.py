from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from app.models import User

# ---------------- Registration Form ----------------
class RegistrationForm(FlaskForm):
    username = StringField('Tên người dùng', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Nhập lại mật khẩu', validators=[DataRequired(), EqualTo('password', message="Mật khẩu không khớp!")])
    submit = SubmitField('Đăng ký')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username đã tồn tại.')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email đã được đăng ký.')


# ---------------- Login Form ----------------
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Đăng nhập')


# ---------------- Post Form ----------------
class PostForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[DataRequired(), Length(1, 200)])
    content = TextAreaField('Nội dung', validators=[DataRequired()])
    image_url = StringField('Image URL (hoặc để trống nếu upload)')
    image_file = FileField('Upload Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Chỉ cho phép file ảnh!')])
    submit = SubmitField('Đăng bài')


# ---------------- Profile Form ----------------
class ProfileForm(FlaskForm):
    bio = TextAreaField('Giới thiệu cá nhân', validators=[Length(max=2000)])
    picture = FileField('Cập nhật ảnh đại diện', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Chỉ cho phép file ảnh!')
    ])
    submit = SubmitField('Lưu')


# ---------------- About Form ----------------
class AboutForm(FlaskForm):
    bio = TextAreaField('About / Bio', validators=[DataRequired(), Length(max=2000)])
    picture = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[Length(max=20)])
    address = StringField('Address', validators=[Length(max=255)])
    submit = SubmitField('Lưu')



# ---------------- Comment Form ----------------
class CommentForm(FlaskForm):
    content = TextAreaField('Bình luận', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Gửi')
