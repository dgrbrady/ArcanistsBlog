from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    assigned_role = db.Column(db.Integer, db.ForeignKey('role.id'))
    email = db.Column(db.String(64))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_email(self, email):
        self.email = email

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class BigNumbers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    open_tickets = db.Column(db.Integer)
    closed_tickets = db.Column(db.Integer)
    tickets_last_month = db.Column(db.Integer)
    tickets_this_quarter = db.Column(db.Integer)
    ticket_leader = db.Column(db.String(64))

    def get_open_tickets(self):
        return self.open_tickets

    def get_closed_tickets(self):
        return self.closed_tickets

    def get_tickets_last_month(self):
        return self.tickets_last_month

    def get_tickets_this_quarter(self):
        return self.tickets_this_quarter

    def get_ticket_leader(self):
        return self.ticket_leader


class Tickets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.String(64))
    owner = db.Column(db.String(64))
    status = db.Column(db.String(64))
    date_created = db.Column(db.Integer)
    title = db.Column(db.String(64))
    content = db.Column(db.String(128))

    def get_ticket_creator(self, id):
        return self.creator


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
