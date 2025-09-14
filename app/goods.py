class Goods:
    def __init__(self, id: int = None, url: str = '', price: float = 0.0, name: str = ''):
        self.id = id
        self.url = url
        self.price = price
        self.name = name

    def __repr__(self):
        return f"Goods(name={self.name!r}, price={self.price!r}, url={self.url!r})"