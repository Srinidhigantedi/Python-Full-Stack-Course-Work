#__init__ is used for declaring the constructor
#self.username is the public
#self.__password is the private
#self._friends is the protect


class Snapchat:
    def __init__(self,username,password,friends):
        self.username = username
        self.__password =password
        self._friends = friends
    def getpassword(self): # to access the password before modification
        return self.__password
    def setpassword(self,new_password):
        self.__password = new_password


    @property
    def oprFriends(self):# it is not a method
        return self._friends #accessing proctected data
    
    @oprFriends.setter
    def oprFriends(self,newfriend):
       self._friends.append(newfriend)#to modify the protected data
    
saaketh = Snapchat("saaketh","12345",["praveen","nikhil"])#object creation

print(f"Name before modification: {saaketh.username}")
saaketh.username ="sapnil"#modifying the public username directly
print(f"Name after modification: {saaketh.username}")

#print(f"Password before modification: {saaketh.__password}") you shouldn't do this.

print(f"Password before modification: {saaketh.getpassword()}")
saaketh.setpassword("S@123")#changing the password
print(f"Password after modification: {saaketh.getpassword()}")
print(f"Friends before modification: {saaketh.oprFriends}")#accessing proctected data
saaketh.oprFriends = "srindhi"#changing the protected data of friends by adding new name
print(f"Friends after modification: {saaketh.oprFriends}")#to modify the protected data


#we can't directly asscess the private data(password), so we have to create separate function to access it
#we can able to access the protected data, but we should not do that,it is not suggested,we can do other process like property.
#oprFriends is not a method ,it is the variable (we use @ for decorer)
