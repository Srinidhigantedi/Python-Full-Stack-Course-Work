n=int(input("enter the sizes:"))
for row in range(n):
    for spc in range(row+1):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()
