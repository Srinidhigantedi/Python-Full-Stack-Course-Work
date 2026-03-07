'''
for var in seq:
    #stmts

seq: list,tuple,set,dict,str,range

#list
products=['bread','butter','milk','sugar','salt']

for product in products:
    print(f'{product}- Add to fav | Buy Now | Add to cart' )


#tuple
sizes=('xs','s','m','l','xl','xxl')
for s in sizes:
    print(f'....|{s}|.....')


#set
my_set = {10, 20, 30, 40}

for item in my_set:
    print(item)


#set
followers={'saaketh','swapnil','nikhil','sandeep'}
for i in followers:
    print(f'{i}-|follow back | remove| message')

#dict
student = {"name": "Rahul", "age": 20, "marks": 85}

for key in student:
    print(key)


#dict

data={
'varsha':['c','python','java'],
'saaketh' : ['ml','ai','python'],
'swapnil' : ['java','html']
}
for i in data :
  print(f"{i}:{data[i]}")
  

#str
name = "saaketh"

for ch in name:
    print(f"Character: {ch}")
 
#str
s='python'
for i in s:
    print(i)

#range(start,stop+1,step)= range(0,n,1)
for i in range(0,10,2):
    print(i)

#range
for i in range(1,11):
    print(i)

#range
for i in range(1,100,2):
    print(i)

#range
for i in range(2,101,2):
    print(i)

#range
for i in range(10,0,-1):
    print(i)

#tables
n=int(input("enter the number:"))
print(f"{n}-Table")
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
    


#break
for i in range(1,10):
    if i==7:
        break
    print(i)

#continue
for i in range(1,10):
    if i==7:
        continue
    print(i)


#while
#print numbers from 1-10
i=1
while i<=10:
    print(i)
    i=i+1

#while
#print numbers from 10-1
i = 10
while i >= 1:
    print(i)
    i= i-1

#playing game1
moves=15
winning_point=int(input("tell me how many moves is required to finish a game:"))
while moves>=1:
    if 15-winning_point==moves:
        print("you won the game")
        break
    print(f"{moves}are left")
    moves-=1
else:
    print("game over")
'''
#playing game2
bullets=10
while bullets >0:
    print(f"You have {bullets} bullets, shoot them!!")
    bullets-=1
else:
    print("Game Over")
