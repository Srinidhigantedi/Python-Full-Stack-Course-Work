data = {
    1: {'product': 'bread', "price": 200},
    2: {'product': 'cake', "price": 400},
    3: {'product': 'biscuit', "price": 10},
    4: {'product': 'salt', "price": 50},
    5: {'product': 'soap', "price": 50},
    6: {'product': 'tea powder', "price": 70},
    7: {'product': 'eggs(12pcs)', "price": 70},
    8: {'product': 'Rice', "price": 100},
}

print('Index'.ljust(7), 'Product Name'.ljust(20), 'Price'.ljust(10))

for i in data:
    print(str(i).ljust(7),
          data[i]['product'].ljust(20),
          str(data[i]['price']).ljust(10))

indexes = list(map(int, input().split()))

print("Bill".center(30, '-'))

total_bill = 0
s = set()

for i in indexes:
    if i not in s:
        print(f'{data[i]["product"]} {data[i]["price"]}*{indexes.count(i)}={data[i]["price"]*indexes.count(i)}')
        total_bill += data[i]["price"] * indexes.count(i)
        s.add(i)

print(f"Your Bill: ${total_bill}")
