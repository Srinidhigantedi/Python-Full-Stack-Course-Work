Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,12.3,"string",[1,2,3],(1,2,3),{1,23},{1:1,2:4,3:9},False,None,2+9j]
l
[1, 12.3, 'string', [1, 2, 3], (1, 2, 3), {1, 23}, {1: 1, 2: 4, 3: 9}, False, None, (2+9j)]
names = ['saaketh','sapnil','bharat','pushwanth','sravanthi','varsha','srinidhi']
names[1]
'sapnil'
names[-1]
'srinidhi'
names[2]
'bharat'
names[3]
'pushwanth'
names[-3]
'sravanthi'
names[-3:]
['sravanthi', 'varsha', 'srinidhi']
names[:4]
['saaketh', 'sapnil', 'bharat', 'pushwanth']
names[2:4]
['bharat', 'pushwanth']
names[::-1]
['srinidhi', 'varsha', 'sravanthi', 'pushwanth', 'bharat', 'sapnil', 'saaketh']
names[-1:-4:-1]
['srinidhi', 'varsha', 'sravanthi']
names.append('abid')
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sravanthi', 'varsha', 'srinidhi', 'abid']
names.extend(['abhinandhan','ravi','vardhan','umesh'])
names
['saaketh', 'sapnil', 'bharat', 'pushwanth', 'sravanthi', 'varsha', 'srinidhi', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
names.insert(3,"Satya")
names
['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sravanthi', 'varsha', 'srinidhi', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
names.remove("ravi")
names
['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sravanthi', 'varsha', 'srinidhi', 'abid', 'abhinandhan', 'vardhan', 'umesh']
id(names)
2538173987328
names.pop(1)
'sapnil'
names.pop(3)
'pushwanth'
names
['saaketh', 'bharat', 'Satya', 'sravanthi', 'varsha', 'srinidhi', 'abid', 'abhinandhan', 'vardhan', 'umesh']
names.pop()
'umesh'
names.pop()
'vardhan'
names
['saaketh', 'bharat', 'Satya', 'sravanthi', 'varsha', 'srinidhi', 'abid', 'abhinandhan']
del names[2]
names
['saaketh', 'bharat', 'sravanthi', 'varsha', 'srinidhi', 'abid', 'abhinandhan']
names.clear()
names
[]
id(names)
2538173987328
names=['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
names
['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
names.index('bharat')
2
names.count('abid')
1
sorted(names)
['Satya', 'abhinandhan', 'abid', 'bharat', 'nikhil', 'praveen', 'pushwanth', 'ravi', 'saaketh', 'sapnil', 'sathvik', 'shanmukha', 'umesh', 'vardhan']
names
['saaketh', 'sapnil', 'bharat', 'Satya', 'pushwanth', 'sathvik', 'nikhil', 'praveen', 'shanmukha', 'abid', 'abhinandhan', 'ravi', 'vardhan', 'umesh']
names.sort()
names
['Satya', 'abhinandhan', 'abid', 'bharat', 'nikhil', 'praveen', 'pushwanth', 'ravi', 'saaketh', 'sapnil', 'sathvik', 'shanmukha', 'umesh', 'vardhan']
names.reverse()
names
['vardhan', 'umesh', 'shanmukha', 'sathvik', 'sapnil', 'saaketh', 'ravi', 'pushwanth', 'praveen', 'nikhil', 'bharat', 'abid', 'abhinandhan', 'Satya']
max(names)
'vardhan'
min(names)
'Satya'
len(names)
14
>>> 1=[1,2,3,4,5]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 
>>> l=[1,2,3,4,5]
>>> sum(l)
15
>>> a=[1,2,3,4,5]
>>> b=a
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> a.append(6)
>>> a
[1, 2, 3, 4, 5, 6]
>>> b.append(15)
>>> b
[1, 2, 3, 4, 5, 6, 15]
>>> id(a)
2538172948992
>>> id(b)
2538172948992
>>> c=a.copy()
>>> c
[1, 2, 3, 4, 5, 6, 15]
>>> a
[1, 2, 3, 4, 5, 6, 15]
>>> c.append(10\)
...          
SyntaxError: unexpected character after line continuation character
>>> c.append(10)
...          
>>> c
...          
[1, 2, 3, 4, 5, 6, 15, 10]
>>> a
...          
[1, 2, 3, 4, 5, 6, 15]
