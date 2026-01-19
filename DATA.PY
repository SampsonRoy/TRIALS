from werkzeug.security import generate_password_hash, check_password_hash

# In signup route:
new_user = User(
    name=name,
    email=email,
    password=generate_password_hash(password, method='pbkdf2:sha256'),
    institution=institution
)
# In login:
if user and check_password_hash(user.password, password):
    # login
    import os
from werkzeug.security import generate_password_hash, check_password_hash
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL'):
    # Render Postgres: fix scheme if needed
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1)
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'eduresourcehub.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
