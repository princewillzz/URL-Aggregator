
from app import db

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    link = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



    