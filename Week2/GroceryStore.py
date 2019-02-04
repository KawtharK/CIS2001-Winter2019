import Item

cart = []

cart.append(Item.Item("Chips", 2.5))
cart.append(Item.Item("Pop", 1.0))
cart.append(Item.TaxableItem("Cake", 4.0, 1.06))
Item.TaxableItem.tax_rate = 1.10

for item in cart:
    print(item)