Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d=['saaketh':23,'praveen':10,'sandeep':20]
SyntaxError: invalid syntax
d={'saaketh':23,'praveen':10,'sandeep':20}
d.keys()
dict_keys(['saaketh', 'praveen', 'sandeep'])
d.values()
dict_values([23, 10, 20])
d
{'saaketh': 23, 'praveen': 10, 'sandeep': 20}
d.items()
dict_items([('saaketh', 23), ('praveen', 10), ('sandeep', 20)])
e={}
e
{}
e=dict{}
SyntaxError: invalid syntax
e={}
e=dict{}
SyntaxError: invalid syntax
e={}
e=dict()
>>> e
{}
>>> d['saaketh']
23
>>> d['sandeep']
20
>>> d.get('saaketh')
23
>>> d.get('saaketh',"name is not present")
23
>>> d.get('nikhil',"name is not present")
'name is not present'
>>> d['sandeep']=25
>>> d
{'saaketh': 23, 'praveen': 10, 'sandeep': 25}
>>> d['saaketh']=18
>>> id(d)
2535742341056
>>> d['sandeep']=20
>>> id(d)
2535742341056
>>> d['abhinandhan']=16
>>> d
{'saaketh': 18, 'praveen': 10, 'sandeep': 20, 'abhinandhan': 16}
>>> d['rohith']=12
>>> d
{'saaketh': 18, 'praveen': 10, 'sandeep': 20, 'abhinandhan': 16, 'rohith': 12}
>>> d.update({'rohid':0,'pavan':'10'})
>>> d
{'saaketh': 18, 'praveen': 10, 'sandeep': 20, 'abhinandhan': 16, 'rohith': 12, 'rohid': 0, 'pavan': '10'}
>>> d.pop('pavan')
'10'
>>> d.popitem()
('rohid', 0)
>>> d.popitem()
('rohith', 12)
>>> del d['sandeep']
>>> d
{'saaketh': 18, 'praveen': 10, 'abhinandhan': 16}
d.clear()
d
{}

d=['praveen':23,'abhi':10,'sandeep':20]
SyntaxError: invalid syntax
d={'saaketh':23,'praveen':10,'sandeep':20}
d
{'saaketh': 23, 'praveen': 10, 'sandeep': 20}
d.setdefault('praveen',0)
10
d[1]='int'
d
{'saaketh': 23, 'praveen': 10, 'sandeep': 20, 1: 'int'}
d[12.3]='float'
d[string]='string'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    d[string]='string'
NameError: name 'string' is not defined. Did you forget to import 'string'?
d['string']='string'
d
{'saaketh': 23, 'praveen': 10, 'sandeep': 20, 1: 'int', 12.3: 'float', 'string': 'string'}
d[1,2,3]='set'
d
{'saaketh': 23, 'praveen': 10, 'sandeep': 20, 1: 'int', 12.3: 'float', 'string': 'string', (1, 2, 3): 'set'}
d[(1,2,3)]='tuple'
d
{'saaketh': 23, 'praveen': 10, 'sandeep': 20, 1: 'int', 12.3: 'float', 'string': 'string', (1, 2, 3): 'tuple'}
d[{1:1,2:2}]='dict'
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    d[{1:1,2:2}]='dict'
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
d.clear()
d
{}
d['val1']=1
d
{'val1': 1}
d['val2']=12.3
d
{'val1': 1, 'val2': 12.3}
d['val2']=[1,2,3,4]
d
{'val1': 1, 'val2': [1, 2, 3, 4]}
