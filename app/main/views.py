from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request
from . import main
from .forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, BigNumbers
from werkzeug.urls import url_parse
from app import db
import pdb

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.index'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.dashboard')
        return redirect(next_page)
    return render_template('index.html', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@login_required
@main.route('/dashboard')
def dashboard():
    big_numbers = BigNumbers.query.first()
    open_tickets = big_numbers.open_tickets
    closed_tickets = big_numbers.closed_tickets
    last_month = big_numbers.tickets_last_month
    this_quarter = big_numbers.tickets_this_quarter
    ticket_leader = big_numbers.ticket_leader
    return render_template('dashboard.html',
                            open_tickets=open_tickets,
                            closed_tickets=closed_tickets,
                            last_month=last_month,
                            this_quarter=this_quarter,
                            ticket_leader=ticket_leader)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)

@main.route('/profile')
@login_required
def profile():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    if user == current_user:
        return render_template('profile.html', user=user, email=user.email)
    else:
        return render_template('403.html')