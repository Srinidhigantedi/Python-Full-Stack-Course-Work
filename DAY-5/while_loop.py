#first code
bullets = 10

while bullets > 0:
    print(f'You have {bullets} bullets, shoot them!')
    bullets -= 1

else:
    print('Game over')


#second code

i=1
while i<=10:
    print(i)
    i=i+1
    
moves = 15
n=15
winning_point = int(input("tell me how many moves is require"))

#third code

while moves >1:
    if 15- winning_point == moves:
     print("you won the game")
     break
    print(f"{moves} are left")
    moves-=1
else:
    print("gameover")  
