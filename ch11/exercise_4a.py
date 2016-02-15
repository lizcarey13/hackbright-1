str_bill = "item:apples,quantity:4,price:1.50\n"

def calculate_bill(str_input):
    split_str = str_input.split(",")
    quantity = float(split_str[1].split(":")[1])
    price = float(split_str[2].split(":")[1])
    return quantity * price

calculate_bill(str_bill)

items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]

def calculate_bill_list(bill_list):
    total = 0
    for item in bill_list:
        total += calculate_bill(item)

    return total

print calculate_bill_list(items)
