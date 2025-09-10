class Goods:
    def __init__(self, id: int, url: str, price: float, name: str):
        self.id = id
        self.url = url
        self.price = price
        self.name = name

    def __repr__(self):
        return f"Goods(name={self.name!r}, price={self.price!r}, url={self.url!r})"