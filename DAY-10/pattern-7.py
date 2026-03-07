n=int(input("enter the size:"))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()
