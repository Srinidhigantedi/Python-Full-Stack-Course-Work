n = int(input("Enter number of rows: "))

for row in range(n*2):
    if row<n:
        print('*'*(row+1))
    else:
        print('*'*(2*n-row))
