n=int(input("enter the size:"))
num=0
for row in range(n):
    for col in range(n):
        print(row+col,end=' ')
        num+=1
    print()
