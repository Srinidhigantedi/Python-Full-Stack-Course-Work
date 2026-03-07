n = int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == col or row+col==n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
