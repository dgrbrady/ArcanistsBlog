from flask import render_template, session, redirect, url_for, flash
from .forms import RegistrationForm
from flask_login import current_user, logout_user
from app.models import User
from app import db, auth

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