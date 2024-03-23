products = {
    "apple": 0.75,
    "banana": 0.60,
    "orange": 0.90,
    "milk": 2.50,
    "bread": 1.80
}

def calculate_total(cart):
    total = 0
    for item, quantity in cart.items():
        if item in products:
            total += products[item] * quantity
    return total

def apply_discounts(total):
    if total > 10.0:
        total *= 0.9  
    return total

def check_free_shipping(total):
    if total > 20.0:
        return True
    return False

cart = {}

while True:
    print("\nAvailable Products:")
    for item, price in products.items():
        print(f"{item}: Ksh{price}")

    print("\nEnter 'done' to finish adding items.")
    
    item = input("Enter item name: ").lower()
    
    if item == "done":
        break
    
    if item in products:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                if item in cart:
                    cart[item] += quantity
                else:
                    cart[item] = quantity
                print(f"{quantity} {item}(s) added to the cart.")
            else:
                print("Please enter a valid quantity.")
        except ValueError:
            print("Please enter a valid quantity.")

    else:
        print("Invalid item. Please choose from the available products.")

total_cost = calculate_total(cart)

total_cost_with_discount = apply_discounts(total_cost)

free_shipping = check_free_shipping(total_cost)

print("\nCart Items:")
for item, quantity in cart.items():
    print(f"{item}: {quantity}")

print("\nTotal Cost (Before Discounts): Ksh", total_cost)
print("Total Cost (After Discounts): Ksh", total_cost_with_discount)

if free_shipping:
    print("Congratulations! Your order qualifies for free shipping.")
else:
    print("Additional shipping charges may apply.")
