Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
float(a)
10.0
str(a)
'10'
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
b=10
b=10.3
int(a)
10
int(b)
10
str(b)
'10.3'
list(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
s='python'
int(s)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
float(s)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
list(s)
['p', 'y', 't', 'h', 'o', 'n']
set(b)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
s='10'
int(s)
10
float(s)
10.0
bool(s)
True
l=[1,2,3,4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
'[1, 2, 3, 4, 5]'
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4,5)
int(t)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
str(t)
'(1, 2, 3, 4, 5)'
tuple(t)
(1, 2, 3, 4, 5)
set(t)
{1, 2, 3, 4, 5}
dict(t)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s=[1,2,3,4]
int(s)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(s)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'list'
str(s)
'[1, 2, 3, 4]'
tuple(s)
(1, 2, 3, 4)
set(s)
{1, 2, 3, 4}
dict(s)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(s)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
d={1:1,2:4,3:9,4:16}
int(d)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
>>> tuple(d)
(1, 2, 3, 4)
>>> set(d)
{1, 2, 3, 4}
>>> dict(d)
{1: 1, 2: 4, 3: 9, 4: 16}
>>> str(d)
'{1: 1, 2: 4, 3: 9, 4: 16}'
>>> bool(d)
True
>>> list(d)
[1, 2, 3, 4]
>>> a=True
>>> int(a)
1
>>> float(a)
1.0
>>> str(a)
'True'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
>>> bool(a)
True
>>> complex(a)
(1+0j)
