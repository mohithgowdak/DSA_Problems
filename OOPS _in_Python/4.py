def return_mobile(price, brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100

    print("Refund price for Mobile is "+str(total_price))

def return_shoe(price, material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax  /100

    print("Refund price for Shoe is "+str(total_price))

return_mobile(1000, "Samsung")
