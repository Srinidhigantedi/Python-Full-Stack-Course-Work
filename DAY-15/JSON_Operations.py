'''
#write mode
import json
with open('demo.json',"w")as file:
    data=[
        {'id':'1','name':'saaketh'},
        {'id':'2','name':'swapnil'},
        {'id':'3','name':'shanmukh'},
        {'id':'4','name':'nikhil'},
        {'id':'5','name':'sandeep'},
        ]
    json.dump(data,file,indent=4)
    print("Data saved successfully!!!")

'''
#read mode
import json

with open('demo.json',"r") as file:
    data=json.load(file)

data.append({'id':'6','name':'varsha'})
with open('demo.json',"w") as file:
    json.dump(data,file,indent=4)
    
