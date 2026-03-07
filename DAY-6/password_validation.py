pwd=input("enter the password:")

if len(pwd)>=8:
    s=set()
    for i in pwd:
        if i.isupper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digit")
        else:
            s.add("splchar")
    if len(s)==4:
        print("strong password")
    else:
        print("weak password")
else:
    print("length needs to be >=8")
