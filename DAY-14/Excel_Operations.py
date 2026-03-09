'''
#read mode in excel sheet
import csv

with open('sample.csv','r') as file:
    content=csv.reader(file)
    for row in content:
        print(row)
       

#access column
import csv

with open('sample.csv','r') as file:
    content=csv.reader(file)
    for row in content:
        print(row[1])

#access column 
import csv

with open('sample.csv','r') as file:
    content=csv.reader(file)
    for row in content:
        print(row[2])
        

#write mode in excel sheet
import csv
with open("samples.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["6","Nikhil","JFS"])
   
    
#append mode in excel sheet
import csv
with open('sample.csv','a',newline='\n') as file:
    data=csv.writer(file)
    data.writerow(['6','bharath'])
    data.writerow(['7','hari'])
'''
     
#write mode in excel sheet and create new excel sheet
import csv
with open('product.csv','w',newline='') as file:
    data=csv.writer(file)
    data.writerow(['product_IDS','Product','Price'])
    data.writerow(['1','laptop','50000'])
    data.writerow(['2','charger','2000'])
    data.writerow(['3','mouse','500'])
    data.writerow(['4','tab','32000'])
    data.writerow(['5','iphone','152000'])

