from flask import request
from flask_restful import Resource, marshal_with

from db import db

from utils import check_login
from news.marshal_structure import news_structure
from models.news_model import NewsModel
import json


class News(Resource):
    # method_decorators = [check_login]  # add decorator check_login to all methods from Main

    @marshal_with(news_structure)
    def get(self, value=None):
        if value:
            data = NewsModel.query.get(value)
            return data
        return NewsModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_post = NewsModel(**data)
        db.session.add(new_post)
        db.session.commit()
        return "Successfully added a new news"

    def put(self, value):
        data = json.loads(request.data)
        post = NewsModel.query.get(value)

        post.title = data.get("title")
        post.text = data.get("text")

        db.session.commit()
        return "Successfully updated the value"

    def delete(self, value):
        post = NewsModel.query.get(value)
        db.session.delete(post)
        db.session.commit()
        return "Successfully deleted the value"

