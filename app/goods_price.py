class GoodsPrice:
    def __init__(self, id: int, goods_id: int, price: float, date: str):
        self.id = id
        self.goods_id = goods_id
        self.price = price
        self.date = date

    def __repr__(self):
        return f"GoodsPrice(goods_id={self.goods_id!r}, price={self.price!r}, date={self.date!r})"