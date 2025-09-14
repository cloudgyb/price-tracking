from flask import Blueprint,jsonify,render_template,request
from urllib.parse import urlparse,urlunparse
from .goods_manager import GoodsManager
from .db import MySQLDatabase
from .goods_price_vo import GoodsPricesVo
from datetime import datetime

app = Blueprint('app', __name__)
db = MySQLDatabase(host='localhost',user='root',
                   password='123456',db='price_tracking')
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
    goods_price_vo: GoodsPricesVo = gm.get_goods_by_url(url_clean)
    if goods_price_vo:
        return render_template('index.html', **goods_price_vo.__dict__)
    return render_template('index.html', err='无法获取商品信息！')