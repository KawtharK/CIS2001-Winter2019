class Item:

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_purchase_price(self):
        return self._price

    def __str__(self):
        return "{} costs: ${}".format(self._name, self.get_purchase_price())


class TaxableItem(Item):
    tax_rate = 1.06

    def __init__(self, name, price, tax_rate):
        super().__init__(name, price)
        if tax_rate >= 2:
            tax_rate /= 100
        elif tax_rate > 1:
            tax_rate -= 1
        self._tax_rate = tax_rate

    def get_purchase_price(self):
        return super().get_purchase_price() * self._tax_rate + super().get_purchase_price()