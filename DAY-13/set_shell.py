
s={1,2,3,4,5}
s
{1, 2, 3, 4, 5}
s[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
s[1:2]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s[1:2]
TypeError: 'set' object is not subscriptable
s.add("string")
s
{1, 2, 3, 4, 5, 'string'}
s.add((1,2,3))
s
{1, 2, 3, 4, 5, 'string', (1, 2, 3)}
s.add(12.3)
s
{1, 2, 3, 4, 5, 'string', (1, 2, 3), 12.3}
s.add(2)


=
s.add(2+3j)
s
{1, 2, 3, 4, 5, 'string', (2+3j), 12.3, (1, 2, 3)}
s.add(False)
s
{False, 1, 2, 3, 4, 5, 'string', (2+3j), 12.3, (1, 2, 3)}
s.add(True)
s
{False, 1, 2, 3, 4, 5, 'string', (2+3j), 12.3, (1, 2, 3)}
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add({1,2,3})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add(1:1,2:2,3:3)
SyntaxError: invalid syntax
s.add({1:1,2:2,3:3})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.add({1:1,2:2,3:3})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.pop()
False
s.remove(4)
s
{1, 2, 3, 5, 'string', (2+3j), 12.3, (1, 2, 3)}
s.remove(4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.remove(4)
KeyError: 4
s.discard(4)
s
{1, 2, 3, 5, 'string', (2+3j), 12.3, (1, 2, 3)}
s.clear()
s
set()
s=set()
s
set()
s={1,2,3,4,5}
2 in s
True
6 not in s
True
a={1,2,3,4,34,19,20}
a
{1, 2, 3, 4, 34, 19, 20}
a={1,2,3,4,19,20,34}
a
{1, 2, 3, 4, 34, 19, 20}
guys=['saaketh','nikhil','vardhan','shanmukh']
guys
['saaketh', 'nikhil', 'vardhan', 'shanmukh']
guys=['saaketh','nikhil','vardhan','shanmukh','abhinandhan','swapnil']
guys
['saaketh', 'nikhil', 'vardhan', 'shanmukh', 'abhinandhan', 'swapnil']
guys={'saaketh','nikhil','vardhan','shanmukh'}
guys
{'saaketh', 'nikhil', 'vardhan', 'shanmukh'}
guys={'saaketh','nikhil','vardhan','shanmukh','abhinandhan','swapnil'}
guys
{'saaketh', 'swapnil', 'vardhan', 'abhinandhan', 'nikhil', 'shanmukh'}
online={'varsha','poojitha'}
online
{'poojitha', 'varsha'}
guys.union(girls)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    guys.union(girls)
NameError: name 'girls' is not defined
guys.union(online)
{'saaketh', 'swapnil', 'poojitha', 'vardhan', 'abhinandhan', 'nikhil', 'shanmukh', 'varsha'}
guys&online
set()
guys.isdisjoint(online)
True
guys & online
set()
guys.isdisjoint(online)
True
girls={'madhu','priya','poojitha','meghna'}
girls
{'madhu', 'poojitha', 'priya', 'meghna'}
girls & online
{'poojitha'}
girls.disjoint(online)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    girls.disjoint(online)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
girls.disjoint(guys)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    girls.disjoint(guys)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
girls ^ online
{'madhu', 'priya', 'varsha', 'meghna'}
girls - online
{'madhu', 'priya', 'meghna'}
guys ^ online
{'saaketh', 'poojitha', 'abhinandhan', 'nikhil', 'shanmukh', 'varsha', 'swapnil', 'vardhan'}
girls.update({'swathi','sanjana','komali'})
girls
{'madhu', 'poojitha', 'meghna', 'sanjana', 'komali', 'swathi', 'priya'}
guys
{'saaketh', 'swapnil', 'vardhan', 'abhinandhan', 'nikhil', 'shanmukh'}
online
{'poojitha', 'varsha'}
guys.intersection(online)
set()
guys.intersection(girls)
set()
girls.intersection(online)
{'poojitha'}
girls.intersection(guys)
set()
online.intersection(guys)
set()
online.intersection(girls)
{'poojitha'}
a=[1,2,3,4,5,6,7,8]
b=[7,8,9,1,2,0]
a.intersection(b)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.intersection(b)
AttributeError: 'list' object has no attribute 'intersection'
a={1,2,3,4,5,6,7,8}
a={1,2,3,4,5,6,7,8}
a.intersection(b)
{8, 1, 2, 7}
a.intersection_update(b)
a
{8, 1, 2, 7}
b
[7, 8, 9, 1, 2, 0]
s={1,2,3,4}
>>> {1,2}.issubset(s)
True
>>> {6,10}.issubset(s)
False
>>> s.superset({1})
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s.superset({1})
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
>>> s.issuperset({1})
True
>>> s.issuper({10,11})
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.issuper({10,11})
AttributeError: 'set' object has no attribute 'issuper'. Did you mean: 'issubset'?
>>> s.issuperset({10,11})
False
>>> len(b)
6
>>> max(b)
9
>>> sorted(b)
[0, 1, 2, 7, 8, 9]
>>> sum(b)
27
>>> b=a
>>> id(b)
1977464221792
>>> id(a)
1977464221792
>>> c=a.copy()
>>> c
{8, 1, 2, 7}
>>> id(c)
1977464221344
>>> 
