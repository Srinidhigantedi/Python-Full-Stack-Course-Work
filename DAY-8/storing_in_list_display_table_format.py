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

for i in range(n):
    print(f"--------Student-{i+1}----------")
    name = input("Enter the name: ")
    gpa = float(input("Enter the gpa: "))

    names.append(name)
    gpas.append(gpa)


print(f'{"Names".ljust(15)}{"GPA".ljust(5)}')
print('-'*20)
for i in range(len(names)):
    print(f'{names[i].ljust(14)}|{str(gpas[i]).ljust(5)}')
