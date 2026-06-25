from dataclasses import dataclass

@dataclass
class Position:
    code: str
    shares: int
    cost: float

    def market_value(self, price: float):
        return self.shares * price

    def profit(self, price: float):
        return (price - self.cost) * self.shares

    def profit_rate(self, price: float):
        return (price - self.cost) / self.cost * 100
