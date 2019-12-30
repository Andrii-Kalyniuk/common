from db import db

author_works = db.Table(
    'author_works',
    db.Column('author_id', db.Integer, db.ForeignKey('author.author_id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.book_id'))
)


class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    works = db.relationship('Book', secondary=author_works, backref=db.backref('works'))


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
