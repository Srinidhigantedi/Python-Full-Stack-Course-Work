
#read
file=open('names.txt','r')
content1=file.read()
file.seek(0)
content2=file.readline()
file.seek(0)
content3=file.readlines()

print(content1,content2,content3,sep='\n\n')

file.close()
'''

#write-1
file=open('names.txt','w')
file.write("hello everyone")
file.close()

#write-2 (without creating the text file also ,it creates automatically
file=open('name.txt','w')
file.write("hello everyone")
file.close()

#append
file=open('names.txt','a')
file.write("\n Welcome to python class")
file.close()

#append & write
file=open('names.txt','a+')
file.write("\n file operations")
file.seek(0)
print(file.read())
file.close()

#write & read
file=open('names.txt','w+')
file.write("\n file operations")
file.seek(0)
print(file.read())
file.close()


#read & write
file=open('names.txt','r+')
file.write("\n file operations")
file.seek(0)
print(file.read())
file.close()




#developers use
with open('names.txt','r+')as file:
    file.write("\n file operations")
    file.seek(0)
    print(file.read())

    
#write mode
with open('names.txt','w')as file:
    file.write("\n override")
    


#read mode
with open('names.txt','r')as file:
    content=file.read()
    print(content)




#append mode
with open('names.txt','a')as file:
    file.write("\n override")
'''    


