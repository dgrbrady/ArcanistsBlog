from flask import render_template, session, redirect, url_for, flash, request
from .forms import LoginForm, ChangeEmailForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, BigNumbers
from werkzeug.urls import url_parse
from app import db, main

@main.bp.route('/', methods=['GET', 'POST'])
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
    return render_template('/index.html', form=form)

@login_required
@main.bp.route('/dashboard')
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

@main.bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user, email=current_user.email)