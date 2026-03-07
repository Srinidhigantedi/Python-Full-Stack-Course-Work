products= ['bread','salt','ice','milk','sugar']
for products in products:
    print(f'{products}-add to fav | buy now | add to cart')
sizes = ('xs','s','m','l','xl','xxl','xxl')

for s in sizes:
    print(f'...|{s}|...')
followers ={'varsha','sirisha','anvika'}

for i in followers:
    print(f'{i}-|follow back|remove|message|')
data={
    'varsha':['c','python','uiux'],
    'anvika':['figma','python','html','css'],
    'sirisha':['c','java''python','dbms']
              }

for i in data:
    print(f"{i}: {data[i]}")
s='python programming'
for i in s:
    print(i)  
#range(start,stop+1,step)=range(0,n,1)
for i in range(1,11):
    print(i)
for i in range(1,101):
    print(i)
for i in range(2,101,2):
    print(i)
for i in range(10,0,-1):
    print(i)
n=int(input("enter the number:"))
print(f"{n}-table")
for i in range (1,11):
    print(f'{n}*{i}={n*i}')
 
for i in range(1,10):
    if i==7:
        continue
    print(i)
for i in range(1,10):
    if i==7:
        break
    print(i)

