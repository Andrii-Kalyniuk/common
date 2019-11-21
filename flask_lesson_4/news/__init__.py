from flask import Blueprint
from flask_restful import Api
from news.routes import News

news = Blueprint("news", __name__)
api_news = Api(news)

api_news.add_resource(News, "/news", "/news/<value>")
