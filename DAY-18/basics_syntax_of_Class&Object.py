class Flipkart:
    discount = 10


    @classmethod
    def updateddiscount(cls,newdiscount):
        cls.discount = newdiscount
        

    def userinfo(self,name,phonenumber):
        self.name = name
        self.phonenumber = phonenumber
        print(f'Username: {self.name}')
        print(f'Phone Number: {self.phonenumber}')

    @staticmethod
    def banner():
        print("Welcome to the Flipkart\n10% discount is going on, shop now")


#object creation
srinidhi = Flipkart()
srinidhi.userinfo("Srinidhi",9440075750) #instance method calling object


srinidhi.updateddiscount(30)#class method calling by object
Flipkart.updateddiscount(40)#class method calling by class name

srinidhi.banner()#static method calling by object
Flipkart.banner()#static method calling by class name
neha = Flipkart()

#instance methods can be called by only objects
#class methods can be called by both objects and class name
#static methods can be called using both objects and class name


