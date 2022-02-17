


from crypt import methods
from re import L
from flask_bcrypt import Bcrypt
from flask import Blueprint, redirect, render_template, request, url_for
from app import app

from app.forms.LoginForm import LoginForm

from app.forms.RegisterForm import RegisterForm
from app.models.User import User

from flask_login import login_user, LoginManager, login_required, current_user, logout_user

from app import db

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')
bcrypt = Bcrypt(app=app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login_view"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@mod_auth.route("/login", methods=['GET', 'POST'])
def login_view():

    form = LoginForm()

    if request.method == 'GET':
        return render_template("login.html", form=form)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('admin.admin_dashboard'))

    return render_template("login.html", form=form)


@mod_auth.route("/register", methods=['GET', 'POST'])
def register_view():

    form = RegisterForm()

    if request.method == 'GET':
        return render_template("register.html", form=form)

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login_view'))

    return render_template("register.html", form=form)



@mod_auth.get("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login_view'))
