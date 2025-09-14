from .goods import Goods

class GoodsPricesVo:
    def __init__(self, goods: Goods, prices: list, dates: list):
        self.goods = goods
        self.prices = prices
        self.dates = dates