from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template("index.html")

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('login.html', form=form)

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')