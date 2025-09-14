from datetime import datetime

class GoodsPrice:
    def __init__(self, id: int = None, goods_id: int = None, price: float = 0.0, create_time: datetime = None):
        self.id = id
        self.goods_id = goods_id
        self.price = price
        self.create_time = create_time or datetime.now()

    def __repr__(self):
        return f"GoodsPrice(goods_id={self.goods_id!r}, price={self.price!r}, date={self.create_time!r})"