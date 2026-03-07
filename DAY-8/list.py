names=['Satya', 'abhinandhan', 'abid', 'bharat', 'nikhil', 'praveen', 'pushwanth', 'ravi', 'saaketh', 'sapnil', 'sathvik', 'shanmukha', 'umesh', 'vardhan']

'''
for i in names:
    print(i)

for i in range(1,len(names)+1):
    print(i,names[i-1])

for i in enumerate(names):
    print(f'{i[0]}. {i[1]}')

i=0
while i<len(names):
    print(f'{i+1}. {names[i]}')
    i+=1

'''
n=int(input("Enter the number of students: "))

names,gpas = [],[]
max_val=0
max_name=' '

min_val=10
min_name=' '

for i in range(n):
    print(f"--------Student-{i+1}----------")
    name = input("Enter the name: ")
    gpa = float(input("Enter the gpa: "))

    if gpa>max_val:
       max_name=name
       max_val=gpa

    if gpa<min_val:
        min_name=name
        min_val=gpa
      

    names.append(name)
    gpas.append(gpa)


print(f'{"Names".ljust(15)}{"GPA".ljust(5)}')
print('-'*20)

    
for i in range(len(names)):
    print(f'{names[i].ljust(14)}|{str(gpas[i]).ljust(5)}')


print(f'The Highest value : {max_name},{max_val}')
print(f'The Lowest value : {min_name},{min_val}')    

    
          
