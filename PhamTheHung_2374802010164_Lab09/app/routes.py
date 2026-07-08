# routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
import os
from app import db
from app.models import Post, Comment, User
from app.forms import PostForm, AboutForm, CommentForm

main = Blueprint('main', __name__)

# --- Home / Index (không cần đăng nhập) ---
@main.route('/')
@main.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', posts=posts)

# --- Single Post (hiển thị + bình luận) ---
@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.timestamp.desc()).all()

    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("Vui lòng đăng nhập để bình luận.", "warning")
            return redirect(url_for('auth.login'))

        new_comment = Comment(
            content=form.content.data,
            author=current_user,
            post_id=post.id
        )
        db.session.add(new_comment)
        db.session.commit()
        flash("Bình luận của bạn đã được đăng!", "success")
        return redirect(url_for('main.post', post_id=post.id))

    return render_template('post.html', post=post, form=form, comments=comments)

# --- Create New Post ---
@main.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        filename = None
        if form.image_file.data:
            file = form.image_file.data
            filename = secure_filename(file.filename)
            upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)

        post = Post(
            title=form.title.data,
            content=form.content.data,
            image_url=url_for('static', filename=f'uploads/{filename}') if filename else form.image_url.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('create_post.html', form=form)

# --- Blog Listing Page ---
@main.route('/blog')
@login_required
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=6)
    return render_template('blog.html', posts=posts)

# --- About Page ---
@main.route('/about', methods=['GET', 'POST'])
@login_required
def about():
    form = AboutForm(obj=current_user)  # Load dữ liệu hiện tại
    image_url = current_user.about_image_url or url_for('static', filename='images/1000.jpg')
    bio_text = current_user.about_content

    if form.validate_on_submit():
        # Xử lý ảnh
        if form.picture.data:
            file = form.picture.data
            filename = secure_filename(file.filename)
            upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)
            file.save(os.path.join(upload_folder, filename))
            current_user.about_image_url = url_for('static', filename=f'uploads/{filename}')

        current_user.about_content = form.bio.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        db.session.commit()
        flash('Cập nhật About thành công!', 'success')
        return redirect(url_for('main.about'))

    # Nếu chưa có bio, hiển thị form
    if not bio_text:
        return render_template('about.html', form=form, image_url=image_url, bio=None)

    # Nếu đã có bio, hiển thị thông tin
    return render_template('about.html', bio=bio_text, image_url=image_url)


# --- Contact Page ---
@main.route('/contact')
@login_required
def contact():
    return render_template('contact.html')

# --- Update User Info (email, phone, address) ---
@main.route('/update_user_info', methods=['POST'])
@login_required
def update_user_info():
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')

    current_user.email = email
    if hasattr(current_user, 'phone'):
        current_user.phone = phone
    if hasattr(current_user, 'address'):
        current_user.address = address

    db.session.commit()
    flash('Cập nhật thông tin cá nhân thành công!', 'success')
    return redirect(url_for('main.blog'))

# --- Search Posts ---
@main.route('/search')
def search():
    query = request.args.get('q', '').strip()
    page = request.args.get('page', 1, type=int)
    if query:
        posts = Post.query.filter(Post.title.ilike(f"%{query}%")) \
                         .order_by(Post.timestamp.desc()) \
                         .paginate(page=page, per_page=5)
    else:
        posts = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=5)
    return render_template('search.html', posts=posts, query=query)
