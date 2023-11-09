# Dry clean: [garment, size, starch, same_day]
#   garments are shirt, pants, jacket, dress
#   each item is 12.95, plus 2.00 for starch
#   same-day service adds 10.00 per same-day item
# Wash and fold [description, weight]
#   4.95 per pound, with 10% off if more than 15 pounds
# Blankets: [type,dryclean, size]
#   type is "comforter" or "cover"
#   Flat fee of 25.00
# ---
# Output:
# Order Total Price

# Dry Clean: (L) shirt Starched
# Dry Clean: (L) shirt Starched
# ....
# Order total: 12.88

orders = [
    [
        ["shirt", "L", True, False],
        ["shirt", "M", True, False],
        ["shirt", "L", False, True],
        ["pants", "M", False, True],
        ["pants", "S", False, False],
        ["pants", "S", False, False],
        ["jacket", "M", False, False],
        ["jacket", "L", False, True]
    ],
    [
        ["dress", "M", False, True],
        ["whites", 5.25],
        ["darks", 12.5]
    ],
    [
        ["shirts and jeans", 28.0],
        ["comforter", False, "L"],
        ["cover", True, "L"],
        ["shirt", "L", True, True]
    ]
]

# SOLUTION - possible 'overkill' - created class definitions for each order type - in a larger 
# application these 'might' be stored in a 'models' folder (for example)
# and the functions for parsing and processing the order we could put in an 'orders' class.
# I've included everything within a single file here

class DryClean:
    def __init__(self, garment, size, starch, same_day):
        self.garment = garment
        self.size = size
        self.starch = starch
        self.same_day = same_day
        self.cost = 0

    def calculate_cost(self):
        self.cost = 12.95
        if self.starch:
            self.cost += 2.00

        if self.same_day:
            self.cost += 10.00

class WashAndFold:
    def __init__(self, description, weight):
        self.description = description
        self.weight = weight
        self.cost = 0

    def calculate_cost(self):
        self.cost = self.weight * 4.95

        if self.weight > 15:
            self.cost = self.cost - (self.cost * 10 / 100)

class Blanket:
    def __init__(self, type, dryclean, size):
        self.type = type
        self.dryclean = dryclean
        self.size = size
        self.cost = 25.00


def parse_order(order_items):
    order = []

    for item in order_items:
        match item:
            case "shirt" | "pants" | "jacket" | "dress" as garment, size, starch, sameday:
                order.append(DryClean(garment, size, starch, sameday))
            case "comforter" | "cover" as blanket, dryclean, size:
                order.append(Blanket(blanket, dryclean, size))
            case str() as desc, weight:
                order.append(WashAndFold(desc, weight))

    return order

def process_order(order):
    order_total = 0

    for item in order:
        match item:
            case DryClean():
                item.calculate_cost()
                order_total += item.cost 
            case WashAndFold():
                item.calculate_cost()
                order_total += item.cost
            case Blanket():
                order_total += item.cost
            case _:
                print("Everything else ....")

    return order_total

if __name__ == "__main__":
    for order in orders:
        order_data = parse_order(order)
        order_total = process_order(order_data)

        print(f"Total cost of order : {order_total:.2f}")

