from flask import Blueprint,jsonify,render_template,request
from urllib.parse import urlparse,urlunparse
from .parser import parse_html
from .goods_manager import GoodsManager
from .db import MySQLDatabase

app = Blueprint('app', __name__)
db = MySQLDatabase(host='localhost',user='root',
                   password='password',db='price_tracking')
gm = GoodsManager(db)

@app.before_app_request
def before_req():
    print("before req!\n")

@app.after_app_request
def after_req(resp):
    print("after req!\n")
    return resp

@app.route('/', methods=['GET'])
def method_name():
    url = request.args.get('url')
    if url is None or url.strip() == '':
        return render_template('index.html')
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if hostname is None:
        return render_template('index.html', err='无效的URL！')
    url_clean = urlunparse((
        parsed_url.scheme or 'http',
        hostname,
        parsed_url.path or '',
        '',
        '',
        ''
    ))
    goods = gm.get_goods_by_url(url_clean)
    if goods:
        return render_template('index.html', **model)
    m = parse_html(url)
    model = {
        "url": url,
        "title": "My Website",
        "dates": ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01",
                  "2023-06-01","2023-07-01","2023-08-01"],
        "prices": [100, 200,100,100,200 ,300, 250, 200],
    }
    return render_template('index.html', **model)