from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import LoginForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    current_name = session.get('name')
    if current_name is not None:
        session['logged_in'] = True

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['password'] = form.password.data
        return redirect(url_for('main.index'))
    return render_template("index.html", 
                            form=form, 
                            name=session.get('name'),
                            logged_in=session.get('logged_in'))

@main.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    session['name'] = None
    return redirect(url_for('main.index'))