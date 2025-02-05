from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(80), nullable=False, unique=True)
     password = db.Column(db.String(80), nullable=False)
     role = db.Column(db.String(80), nullable=False, default='user')

     # Relacionamento com Meal (um usuário pode ter várias refeições)
     meals = db.relationship('Meal', backref='user', lazy=True)

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_time = db.Column(db.DateTime, nullable=False)
    in_diet = db.Column(db.Boolean, nullable=False)

    # Relacionamento com User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)