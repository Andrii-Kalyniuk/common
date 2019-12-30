from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/<item_from_img>')
def get_item(item_from_img):
    return render_template("item.html",
                           item_from_img=item_from_img, data=get_data())


@app.route('/author.html')
def get_author_page():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(debug=True)
