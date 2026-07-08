from app import create_app, db
from app.models import User, Post  # ✅ thêm dòng này

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Post': Post, 'User': User}

if __name__ == '__main__':
    app.run(debug=True)