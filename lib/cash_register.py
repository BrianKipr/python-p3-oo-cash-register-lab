class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)  # Add multiple items to the list
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            self.total -= (self.total * self.discount) / 100
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def _get_price_of_item(self, title):
        return sum(item_price for item_title, item_price in self.item_prices if item_title == title)

    def _price_of_last_item(self):
        if self.items:
            last_item_title = self.items[-1]
            last_item_price = self._get_price_of_item(last_item_title)
            return last_item_price
        return 0

    def void_last_transaction(self):
        if self.items:
            last_item_price = self._price_of_last_item()
            self.items.pop()
            self.total -= last_item_price
        else:
            print("No items to void.")
