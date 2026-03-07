print('Welcome to "Hari" super market')
data={
1:{"Product":"Rice","Price":60},
2:{"Product":"Wheat Flour","Price":40},
3:{"Product":"Sugar","Price":80},
4:{"Product":"Milk","Price":25},
5:{"Product":"Eggs","Price":70},
6:{"Product":"Cooking Oil","Price":130},
7:{"Product":"Tea Powder","Price":90},
8:{"Product":"Salt","Price":20},
9:{"Product":"Bread","Price":30},
10:{"Product":"Soap","Price":25} }
indexes = list(map(int,input("Enter the indexes:  ").split(
print("Bill".center(30,'-'))
total_bill=0
s=set()
      for i in indexes:
          if i not in s:
             print(f'{data[i]["product"]}{data[i]["price"]}*{indexes.count(i)} = {data[i]["price"]*indexes.count(i)}
                   total_bill+=data[i]["price"]
print(f"Your Bill:{total_bill}")
