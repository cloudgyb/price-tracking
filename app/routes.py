from flask import Blueprint,jsonify

app = Blueprint('app', __name__)

@app.before_app_request
def before_req():
    print("before req!\n")

@app.after_app_request
def after_req(resp):
    print("after req!\n")
    return resp

@app.route('/')
def method_name():
    return "Hello world!"

@app.route('/config')
def test_config():
    return jsonify(app.name)