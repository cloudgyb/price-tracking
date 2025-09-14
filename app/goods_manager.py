from .db import MySQLDatabase
from .goods import Goods

from .goods_price_manager import GoodsPriceManager
from .GoodsWithPrices import GoodsWithPrices

class GoodsManager:
    def __init__(self, db: MySQLDatabase):
        self.db = db
        self.table = "goods"
        self.price_manager = GoodsPriceManager(db)

    def add_goods(self, goods: Goods):
        data = {
            "url": goods.url,
            "price": goods.price,
            "name": goods.name
        }
        goods_id = self.db.create(self.table, data)
        return goods_id

    def get_goods(self, goods_id: int):
        result = self.db.read(self.table, {"id": goods_id})
        if result:
            row = result[0]
            return Goods(row["id"], row["url"], row["price"], row["name"])
        return None
    def get_goods_by_url(self, url: str):
        result = self.db.read(self.table, {"url": url})
        if result:
            row = result[0]
            return Goods(row["id"], row["url"], row["price"], row["name"])
        return None
    def update_goods(self, goods_id: int, data: dict):
        return self.db.update(self.table, data, {"id": goods_id})

    def delete_goods(self, goods_id: int):
        return self.db.delete(self.table, {"id": goods_id})

    def list_goods(self):
        results = self.db.read(self.table)
        return [Goods(row["id"], row["url"], row["price"], row["name"]) for row in results]
    
    def get_goods_with_prices(self, goods_id: int, price_limit: int = 365):
        goods = self.get_goods(goods_id)
        if not goods:
            return None
        prices = self.price_manager.get_prices(goods_id, limit=price_limit)
        return [GoodsWithPrices(goods, price) for price in [prices]]