def calculate_bill(base_price, *extra_toppings, **options):
    total = base_price
    for topping in extra_toppings:
        total += topping

    discount = options.get("discount", 0)
    delivery = options.get("delivery", False)

    total = total - (total * discount / 100)

    if delivery:
        total += 3.0

    return round(total, 2)


print(calculate_bill(10.0, 2.0, 3.0))                             
print(calculate_bill(10.0, 2.0, 3.0, discount=10, delivery=True)) 