from .db import MySQLDatabase
from .goods_price import GoodsPrice

class GoodsPriceManager:
    def __init__(self, db: MySQLDatabase):
        self.db = db
        self.table = "goods_price"

    def add_price(self, goods_id: int, price: float, date: str) -> int:
        data = {
            "goods_id": goods_id,
            "price": price,
            "date": date
        }
        return self.db.create(self.table, data)

    def get_prices(self, goods_id: int = None, limit: int = 365):
        where = {"goods_id": goods_id} if goods_id is not None else None
        rows = self.db.read(self.table, where, order_by="date DESC", limit=limit)
        return [GoodsPrice(**row) for row in rows]

    def update_price(self, id: int, price: float = None, date: str = None) -> int:
        data = {}
        if price is not None:
            data["price"] = price
        if date is not None:
            data["date"] = date
        if not data:
            return 0
        where = {"id": id}
        return self.db.update(self.table, data, where)

    def delete_price(self, id: int) -> int:
        where = {"id": id}
        return self.db.delete(self.table, where)