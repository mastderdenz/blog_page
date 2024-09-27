from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), unique = True)
    username = db.Column(db.String(20), unique = True)
    password = db.Column(db.String(150), unique = False)
    date_created =  db.Column(db.DateTime(timezone = True), default = func.now())
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    likes = db.relationship('Like', backref='user', passive_deletes=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable = False)
    image_data = db.Column(db.LargeBinary)
    author = db.Column(db.Integer, db.ForeignKey("user.id", ondelete = "CASCADE"), nullable = False)
    date_created =  db.Column(db.DateTime(timezone = True), default = func.now())
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    likes = db.relationship('Like', backref='post', passive_deletes=True)



class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(200), nullable = False)
    author = db.Column(db.Integer, db.ForeignKey("user.id", ondelete = "CASCADE"), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete = "CASCADE"), nullable = False)
    date_created =  db.Column(db.DateTime(timezone = True), default = func.now())

class Like(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.Integer, db.ForeignKey("user.id", ondelete = "CASCADE"), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete = "CASCADE"), nullable = False)
    date_created =  db.Column(db.DateTime(timezone = True), default = func.now())


