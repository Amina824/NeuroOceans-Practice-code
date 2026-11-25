def summarize_orders(order_list):
    unique_items = set()
    customer_orders = {}

    for name, item in order_list:
        unique_items.add(item)

        if name not in customer_orders:
            customer_orders[name] = []

        customer_orders[name].append(item)

    return unique_items, customer_orders


orders = [
    ("Ali", "Coffee"),
    ("Sara", "Tea"),
    ("Ali", "Sandich"),
    ("Zara", "Coffe"),
    ("Sara", "Cake"),
]

unique_items, customer_orders = summarize_orders(orders)
print(unique_items)
print(customer_orders["Sara"])