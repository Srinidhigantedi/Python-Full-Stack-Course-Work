products = ['heels', 'shirts', 'hand bags', 'laptop', 'facewash']
item = input('Enter the item:')

if item in products:
    print(f'The {item} is found\n Go and Shop')
else:
    print(f'Sorry the {item} is not found')
