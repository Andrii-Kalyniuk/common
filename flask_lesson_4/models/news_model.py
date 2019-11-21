from db import db
from datetime import datetime


class NewsModel(db.Model):
    __tablename__ = "news"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.String(), unique=True, nullable=False)
    date = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
