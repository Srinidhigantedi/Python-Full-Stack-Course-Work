media=['bluesun.png','mountains.png','beach.png','garden.png','classroom.png','shopping.mp4','party.mp4','trip.mp4','jwellery.mp4','goa.mp4']
photos=[]
videos=[]

for i in media:
    if i.endswith('png'):
        photos.append(i)
    else:
       videos.append(i)

print("........Photos......")
for i in photos:
    print(i)
print("........Videos......")
for i in videos:
    print(i)    
    
select=set(input("Enter the files to share(using comma): ").split(','))

for i in select:
 if i in media:
     print(f"{i} Sent")
 else:
     print(f"{i} File is not present")

