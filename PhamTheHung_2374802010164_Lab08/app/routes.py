from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Post, User, Comment   # ✅ Thêm Comment model
from app.forms import PostForm, RegistrationForm, LoginForm, CommentForm  # ✅ Thêm CommentForm

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(
        page=page, 
        per_page=5, 
        error_out=False
    )
    return render_template('index.html', title='Trang chủ', posts=posts)

@bp.route('/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            user_id=1  # ✅ Tạm thời hardcode; sau này thay bằng current_user.id
        )
        post.slug = post.generate_slug()

        # ✅ Đảm bảo slug là duy nhất
        original_slug = post.slug
        counter = 1
        while Post.query.filter_by(slug=post.slug).first():
            post.slug = f"{original_slug}-{counter}"
            counter += 1

        db.session.add(post)
        db.session.commit()
        flash('Bài viết đã được tạo thành công!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('create_post.html', title='Tạo bài viết', form=form)

@bp.route('/post/<slug>', methods=['GET', 'POST'])
def post(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            user_id=1,  # ✅ sau này thay bằng current_user.id
            post_id=post.id
        )
        db.session.add(comment)
        db.session.commit()
        flash('Bình luận của bạn đã được gửi!', 'success')
        return redirect(url_for('main.post', slug=slug))

    comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.created_at.desc()).all()
    return render_template('post.html', title=post.title, post=post, form=form, comments=comments)
