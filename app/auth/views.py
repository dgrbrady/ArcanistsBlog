from flask import render_template, session, redirect, url_for, flash, request
from .forms import RegistrationForm
from flask_login import current_user, logout_user, login_required
from app.models import User
from app import db, auth
from werkzeug.urls import url_parse

@auth.bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.bp.route('/register', methods=['GET', 'POST'])
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
    return render_template('auth/register.html', form=form)

@login_required
@auth.bp.route('/change-email', methods=['GET', 'POST'])
def change_email():
    new_email = request.form.get('new-email')
    current_user.set_email(email=new_email)
    db.session.add(current_user)
    db.session.commit()
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('main.profile')
    return redirect(next_page)