def calculate_total(price, quantity):
    subtotal = price * quantity
    discount = 100
    total = subtotal - discount

    return total


price = 500
quantity = 3

result = calculate_total(price, quantity)

print("Final total:", result)