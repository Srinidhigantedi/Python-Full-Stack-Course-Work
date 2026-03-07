
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=int(input("enter the integer:"))
enter the integer:15
b=float(input("enter the float value:"))
enter the float value:12.0
s=inout("enter the str:")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s=inout("enter the str:")
NameError: name 'inout' is not defined. Did you mean: 'input'?
s=input("enter the str:")
enter the str:'python'
s
"'python'"
saaketh sanjana sandeep
SyntaxError: invalid syntax
names=input("enter the names:")
enter the names:saaketh sandeep
names
'saaketh sandeep'
names.split()
['saaketh', 'sandeep']
n=1,2,3,4,5
n.split(,)
SyntaxError: invalid syntax
n='1,2,3,4,5'
n.split(,)
SyntaxError: invalid syntax
KeyboardInterrupt
n='1,2,3,4,5'
n.split(',')
['1', '2', '3', '4', '5']
names=input("enter the names:").split()
enter the names:saaketh sandeep
names
['saaketh', 'sandeep']
rollno=input().split()
1 7 8 9 5 4
rollno
['1', '7', '8', '9', '5', '4']
k=map(int,rollno)
k
<map object at 0x0000017F663D94C0>
k=list(map(int,rollno))
k
[1, 7, 8, 9, 5, 4]
k=list(map(int,input().split()))
1 6 5 3 38 37 57
k
[1, 6, 5, 3, 38, 37, 57]
k=list(map(float,input().split()))
4 2 6 7 8.4 7.3
k
[4.0, 2.0, 6.0, 7.0, 8.4, 7.3]
k=input().split()
sad happy worst good
k
['sad', 'happy', 'worst', 'good']
k=tuple(map(int,input().split()))
1 2 4 3 
k
(1, 2, 4, 3)
k=tuple(map(float,input().split()))
12.3 14.9 1.1
k
(12.3, 14.9, 1.1)
k=tuple(input().split())
sad happy good
k
('sad', 'happy', 'good')
k=set(map(int,input().split()))
1 1 2 4 2 1 5 5 9 0
k
{0, 1, 2, 4, 5, 9}
k=set(map(float,input().split()))
1.4 2.8 5.6
k
{1.4, 2.8, 5.6}
k=set(input().split()
      shh shha shhs
      
SyntaxError: '(' was never closed
k=set(input().split())
      
sh shhd shdb
k
      
{'shhd', 'sh', 'shdb'}
k=eveal(input())
      
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    k=eveal(input())
NameError: name 'eveal' is not defined. Did you mean: 'eval'?
k=eval(input())
      
(12: "dqda" , 13: "eqaq")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    k=eval(input())
  File "<string>", line 1
    (12: "dqda" , 13: "eqaq")
       ^
SyntaxError: invalid syntax
k=eval(input())
      

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    k=eval(input())
  File "<string>", line 0
    
SyntaxError: invalid syntax

k=eval(input())
      
k=eval(input())
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    k=eval(input())
  File "<string>", line 1
    k=eval(input())
           ^^^^^
SyntaxError: invalid syntax. Did you mean 'not'?
k=eval(input())
      
{12:"djshd",13: "dsh"}
k
      
{12: 'djshd', 13: 'dsh'}
a,b,c=10,20,30
      
a
      
10
b
      
20
c
      
30
a=10,20,30
      
a
      
(10, 20, 30)
username,password = input().split()
      
username,password = input().split()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    username,password = input().split()
ValueError: too many values to unpack (expected 2, got 3)
username,password = input().split()
      

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    username,password = input().split()
ValueError: not enough values to unpack (expected 2, got 0)
username,password = input().split()
      
saaketh 123@
username
      
'saaketh'
password
      
'123@'
a=10
      
b=20.3
      
c="python"
      
print("a=",a,"b=",b,"c=",c)
      
a= 10 b= 20.3 c= python
>>> print("a=",a,"b=",b,"c=",c,sep='')
...       
a=10b=20.3c=python
>>> print("a=",a,"b=",b,"c=",c,sep='@')
...       
a=@10@b=@20.3@c=@python
>>> print("a=",a,"b=",b,"c=",c,sep='@',end='-----')
...       
a=@10@b=@20.3@c=@python-----
>>> print(f"a={a} b={b} c={c}")
...       
a=10 b=20.3 c=python
>>> print(f"a={a}\t b={b}\t c={c}")
...       
a=10	 b=20.3	 c=python
>>> print(f"a={a}\tb={b}\tc={c}")
...       
a=10	b=20.3	c=python
>>> print(f"a={a}\nb={b}\nc={c}")
...       
a=10
b=20.3
c=python
>>> print("a=%d\n b=%f\n c=%s" %(a,b,c))
...       
a=10
 b=20.300000
 c=python
>>> print("a={}\nb={}\nc={}".format(a,b,c))
...       
a=10
b=20.3
c=python
>>> print("a={}\nb={}\nc={}".format(b,a,c))
...       
a=20.3
b=10
c=python
>>> print("a={0}\nb={2}\nc={1}".format(a,b,c))
...       
a=10
b=python
c=20.3
