from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['UPLOAD_FOLDER'] = 'static/files/'
db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def is_authenticated(self):
        pass

    def is_active(self):
        pass

    def is_anonymous(self):
        pass

    def get_id(self):
        return str(self.id)

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        password = generate_password_hash(
            password=request.form["password"],
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            name=request.form["name"].capitalize(),
            email=request.form["email"],
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.get_by_email(email)

        if not user:
            return redirect(url_for('login'))

        user_hash_pass = user.password
        if check_password_hash(user_hash_pass, password):
            login_user(user)
            return redirect(url_for('secrets'))
        return redirect(url_for('login'))


@app.route('/secrets')
@login_required
def secrets():
    name = current_user.name
    return render_template(
        "secrets.html",
        name=name
    )


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf'
    )


if __name__ == "__main__":
    app.run(debug=True)
