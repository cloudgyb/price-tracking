from .db import MySQLDatabase
from .goods import Goods

class GoodsManager:
    def __init__(self, db: MySQLDatabase):
        self.db = db
        self.table = "goods"

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

    def update_goods(self, goods_id: int, data: dict):
        return self.db.update(self.table, data, {"id": goods_id})

    def delete_goods(self, goods_id: int):
        return self.db.delete(self.table, {"id": goods_id})

    def list_goods(self):
        results = self.db.read(self.table)
        return [Goods(row["id"], row["url"], row["price"], row["name"]) for row in results]