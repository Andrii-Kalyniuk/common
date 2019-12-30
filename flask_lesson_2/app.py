from flask import Flask, request, render_template, make_response, jsonify, session, url_for
from werkzeug.utils import secure_filename, redirect
from blueprint.main import vegetable

app = Flask(__name__)
import os

app_list = []

app.config["SECRET_KEY"] = "super_secret_key"
app.register_blueprint(vegetable)


@app.route('/', methods=['GET', 'POST'])
def return_info():
    if request.method == 'GET':
        return render_template("hello.html")
    elif request.method == 'POST':
        app_list.append("1")
        print(app_list)
        return "ok"
    return "ok"


@app.route('/request', methods=['POST'])
def request_object_example():
    data = {
        "request.method": request.method,
        "request.args": request.args,
        "request.headers": request.headers,
        "request.data": request.data
    }
    print(data)
    return "ok"


@app.route("/save_file", methods=['POST'])
def save_file():
    file = request.files['file']
    file1 = request.files['file1']
    path = os.path.join('file', secure_filename(file.filename))
    path1 = os.path.join('file', file1.filename)
    file.save(path)
    file1.save(path1)
    return "ok"


@app.route('/home')
def get_home():
    session["value"] = 'Ok'
    return "ok"


@app.route('/test')
def test():
    print(session.get("login"))
    app.logger.info("INFO test url run")
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return "ok"


@app.route('/cookies')
def get_cookies():
    cookies = request.cookies
    return jsonify(cookies)


@app.route('/add_cookies')
def add_cookies():
    response = make_response("ok")
    response.set_cookie("1", "2")
    return response


@app.errorhandler(404)
def handle_404(error):
    return render_template("error_404.html")


if __name__ == '__main__':
    app.run(debug=True)
