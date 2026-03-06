name = input('Enter the name: ')
mobile_number = int(input('Enter the mobile number: '))

product_1 = input('Enter the product name: ')
price_1 = float(input('Enter the product_price: '))
product_2 = input('Enter the product name: ')
price_2 = float(input('Enter the product price: '))
product_3 = input('Enter the product name: ')
price_3 = int(input('Enter the price: '))

print(f"{name} your bill is")
print(f"{product_1}: ${price_1}")
print(f"{product_2}: ${price_2}")
print(f"{product_2}: ${price_3}")

total_bill = price_1 + price_2 + price_3

print(f" Hello {name} your total bill is {total_bill}")
