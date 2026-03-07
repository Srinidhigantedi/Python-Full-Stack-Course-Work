Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

===== RESTART: C:/Users/saake/Desktop/Python FS/Day-6/string_operations.py =====
python programming

===== RESTART: C:/Users/saake/Desktop/Python FS/Day-6/string_operations.py =====
python programming
pythonpythonpython
'*'*50
'**************************************************'
names='saakethsandeepswapnil'
names[0]
's'
names[-1]
'l'
names[-11]
'd'
#s[start,stop+1,step]
names[0:7:1]
'saaketh'
names[:7]
'saaketh'
names[7:14]
'sandeep'
names[14:21]
'swapnil'
names[14:]
'swapnil'
names[::-1]
'linpawspeednashtekaas'
names[7:-1]
'sandeepswapni'
names[7::-1]
'shtekaas'
names[6::-1]
'htekaas'
names[13::-1]
'peednashtekaas'
names[-1:-6:-1]
'linpa'
names[-1:-7:-1]
'linpaw'
names[-1:-8:-1]
'linpaws'
'saaketh'in names
True
'bharath' not in names
True
len(arr)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    len(arr)
NameError: name 'arr' is not defined
len(names)
21
max(names)
'w'
min(names)
'a'
ord(s)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ord(s)
NameError: name 's' is not defined. Did you mean: 's1'?
ord('s')
115
ord('w')
119
chr(5)
'\x05'
chr(30)
'\x1e'
sorted(names)
['a', 'a', 'a', 'a', 'd', 'e', 'e', 'e', 'h', 'i', 'k', 'l', 'n', 'n', 'p', 'p', 's', 's', 's', 't', 'w']
names.upper()
'SAAKETHSANDEEPSWAPNIL'
names.lower()
'saakethsandeepswapnil'
names.swapcase()
'SAAKETHSANDEEPSWAPNIL'
names='SaakethSandeepSwapnil'
names.swapcase()
'sAAKETHsANDEEPsWAPNIL'
a='python'
a,center(30,'-')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a,center(30,'-')
NameError: name 'center' is not defined
a.center(30,'-')
'------------python------------'
a.ljust(30,'-')
'python------------------------'
a.rjust(30,'-')
'------------------------python'
a.isalpha()
True
'12'.isaplha()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    '12'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
'12'.isalpha()
False
'12'.isdigit()
True
'a12'.isalnum()
True
'python.py'.startswith('p')
True
'python.py'.endswith('.py')
True
'a'.islower()
True
'   '.isspace()
True
'   h'.isspace()
False
s='python is easy'
s.replace('python','java')
'java is easy'
s.split()
['python', 'is', 'easy']
s.title()
'Python Is Easy'
s.captilize()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
s.capitalize()
'Python is easy'
s='     python
SyntaxError: unterminated string literal (detected at line 1)
s='     python'
s.lstrip()
'python'
s.rstrip()
'     python'
s.index('y')
6
s.index('o')
9
s.index('z')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.find('z')
-1
>>> 
==== RESTART: C:/Users/saake/Desktop/Python FS/Day-6/password_validation.py ====
enter the password:saaketh123
weak password
>>> saaketh
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    saaketh
NameError: name 'saaketh' is not defined
>>> 
==== RESTART: C:/Users/saake/Desktop/Python FS/Day-6/password_validation.py ====
enter the password:saaketh
length needs to be >=8
>>> 
==== RESTART: C:/Users/saake/Desktop/Python FS/Day-6/password_validation.py ====
enter the password:Saaketh@123
strong password
>>> 
==== RESTART: C:/Users/saake/Desktop/Python FS/Day-6/password_validation.py ====
enter the password:d123@asdfg
weak password
>>> 
===== RESTART: C:/Users/saake/Desktop/Python FS/Day-6/username_generator.py ====
enter the name:saaketh
enter the dob[YYYY-MM-DD]:2003-08-23
hi saaketh!
 Your username:sath2303
>>> 
===== RESTART: C:/Users/saake/Desktop/Python FS/Day-6/username_generator.py ====
enter the name:sathvik
enter the dob[YYYY-MM-DD]:2003-12-25
hi sathvik!
 Your username:saik2503
