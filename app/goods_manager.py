from .db import MySQLDatabase
from .goods import Goods
from .parser import parse_html
from .goods_price_manager import GoodsPriceManager
from .goods_price_vo import GoodsPricesVo
from .goods_price import GoodsPrice
from datetime import datetime

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
    
    def get_goods_by_url(self, url: str) -> GoodsPricesVo:
        """
        Retrieves goods information and their price history by URL.

        If the goods with the specified URL exist in the database, fetches the goods and their associated price history.
        If not, parses the HTML at the given URL to extract goods information, adds the new goods and its price to the database,
        and returns the newly created goods with the current price and timestamp.

        Args:
            url (str): The URL of the goods to retrieve.

        Returns:
            GoodsPricesVo: An object containing the goods information, a list of prices, and corresponding dates.
        """
        result = self.db.read(self.table, {"url": url}, limit=1)
        if result:
            row = result[0]
            goods = Goods(row["id"], row["url"], row["price"], row["name"])
            return self.get_goods_with_prices(goods=goods)
        else:
            m = parse_html(url)
            title = m['title'] if m['title'] else '未知商品'
            price = float(m['price'])
            goods = Goods(url=url, price=price, name=title)
            goods_id = self.add_goods(goods)
            goods_price = GoodsPrice(goods_id=goods_id, price=price)
            self.add_goods_price(goods_price=goods_price)
            return GoodsPricesVo(goods=goods, prices=[f"{price:.2f}"], 
                                 dates=[datetime.now().strftime('%Y-%m-%d')])

    def update_goods(self, goods_id: int, data: dict):
        return self.db.update(self.table, data, {"id": goods_id})

    def delete_goods(self, goods_id: int):
        return self.db.delete(self.table, {"id": goods_id})

    def list_goods(self):
        results = self.db.read(self.table)
        return [Goods(row["id"], row["url"], row["price"], row["name"]) for row in results]
    
    def add_goods_price(self, goods_price: GoodsPrice):
        self.price_manager.add_price(goods_price)

    def get_goods_with_prices(self, goods: Goods, price_limit: int = 365) -> GoodsPricesVo:
        if not goods:
            return None
        prices = self.price_manager.get_prices(goods_id=goods.id, limit=price_limit)
        price_list = []
        date_list = []
        for p in prices:
            price_list.append(f"{p.price:.2f}")
            date_list.append(p.create_time.strftime('%Y-%m-%d'))

        return GoodsPricesVo(goods, price_list, date_list)