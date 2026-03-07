'''
class InstagramV1:   #parent class
    
   def __init__(self,username):
       self.username = username
       print(f"Hey {self.username}, Welcome to the Instagram!!!")
       
   def reels(self):
       print("You can upload and scroll the reels")
       
   def posts(self):
       print("You can post your pics")
       
sapnil = InstagramV1("sapnil")   #this is constructor
sapnil.reels()                   #this is the instance method
sapnil.posts()                   #this is the instance method
'''




'''
#SINGLE INHERITANCE
class InstagramV1:   #parent class
    
   def __init__(self,username):
       self.username = username
       print(f"Hey {self.username}, Welcome to the Instagram!!!")
       
   def reels(self):
       print("You can upload and scroll the reels")
       
   def posts(self):
       print("You can post your pics")
       


#Constructor is varying from class to class, declare constructor in new class and call the thing inside of it
#when we want to acquire the proporties of the parent class to child we have to do below synatx

class InstagramV2(InstagramV1):   # child class

    def __init__(self,username):
        super().__init__(username)# calling by "super" keyword
         
         #constructor calling from parent class
         
         
    def story(self):
        print("You cn upload the story")
        
sapnil = InstagramV1("sapnil")   #this is constructor
sapnil.reels()                   #this is the instance method
sapnil.posts()                   #this is the instance method

srinidhi = InstagramV2("srinidhi")
srinidhi.reels()
srinidhi.posts()
srinidhi.story()
'''




'''
#MULTILEVEL INHERITANCE
#super key word is used when you have the same constructor and want to access from the parent to child then use it.

class InstagramV1:   #parent1 class
    
   def __init__(self,username):
       self.username = username
       print(f"Hey {self.username}, Welcome to the Instagram!!!")
       
   def reels(self):
       print("You can upload and scroll the reels")
       
   def posts(self):
       print("You can post your pics")

class InstagramV2(InstagramV1):   # parent2 class

    def __init__(self,username):
        super().__init__(username)# calling by "super" keyword
        
    def story(self):
        print("You can upload the story")
        
class InstagramV3(InstagramV2):   # child class

    def __init__(self,username):
        super().__init__(username)# calling by "super" keyword
    def note(self):
        print("You can upload the note")

sapnil = InstagramV1("sapnil")   
sapnil.reels()                  
sapnil.posts()                   

srinidhi = InstagramV2("srinidhi")
srinidhi.reels()
srinidhi.posts()
srinidhi.story()

neha = InstagramV3("neha")
neha.reels()
neha.posts()
neha.story()
neha.note()
'''




'''
#MULTIPLE INHERITANCE- single child and multiple parents( accessing the proporties from multiple parents to single child)

class InstagramV1:   #parent1 class
    
   def __init__(self,username):
       self.username = username
       print(f"Hey {self.username}, Welcome to the Instagram!!!")
       
   def reels(self):
       print("You can upload and scroll the reels")
       
   def posts(self):
       print("You can post your pics")

class InstagramV2(InstagramV1):   # parent2 class

    def __init__(self,username):
        super().__init__(username)# calling by "super" keyword
        
    def story(self):
        print("You can upload the story")
        
class InstagramV3(InstagramV2):   # parent3 class

    def __init__(self,username):
        super().__init__(username)# calling by "super" keyword
    def note(self):
        print("You can upload the note")
class Live:
    def lauchlive(self):
        print("Now you can go on live")

class Verification:
    def verify(self):
        print("You can verify your account for better features")
        
class InstagramV4(InstagramV3,Live,Verification):
    def __init__(self,username):
       super().__init__(username) 
        
    

sapnil = InstagramV1("sapnil")   
sapnil.reels()                  
sapnil.posts()                   

srinidhi = InstagramV2("srinidhi")
srinidhi.reels()
srinidhi.posts()
srinidhi.story()

neha = InstagramV3("neha")
neha.reels()
neha.posts()
neha.story()
neha.note()

akhil = InstagramV4("akhil")
akhil.reels()
akhil.posts()
akhil.story()
akhil.note()
akhil.lauchlive()
akhil.verify()
'''



#total code(hierachical inheritance)


class instagramV1:
    def __init__(self,username):
        self.username=username
        print(f" hey {self.username}, welcome to the Instagram!!!")
    def reels(self):
        print("you can upload and scroll the reels")
    def posts(self):
        print("you can post your pictures")

class instagramV2(instagramV1):
    def __init__(self,username):
        super().__init__(username)
    def story(self):
        print("you can upload the story")

class instagramV3(instagramV2):
    def __init__(self,username):
        super().__init__(username)
    def note(self):
        print("you can upload a note")

class live:
    def launchlive(self):
        print("now you can go on live")
class verification:
    def verify(self):
        print("you can verify your account for better features")
class instagramV4(instagramV3,live,verification):
    def __init__(self,username):
        super().__init__(username)

class creator(instagramV4):
    def __init__(self,username):
        super().__init__(username)
    def insights(self):
        print("you can check your posts insights")
class business(instagramV4):
    def __init__(self,username):
        super().__init__(username)
    def buttons(self):
        print("you can contact them mail and number")
    

saaketh=instagramV1('saaketh')
saaketh.reels()
saaketh.posts()
nikhil=instagramV2('Nikhil')
nikhil.reels()
nikhil.posts()
nikhil.story()
praveen=instagramV3('praveen')
praveen.reels()
praveen.posts()
praveen.story()
praveen.note()
sandeep=instagramV4('sandeep')
sandeep.reels()
sandeep.posts()
sandeep.story()
sandeep.note()
sandeep.launchlive()
sandeep.verify()


















       


