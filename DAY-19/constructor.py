class Instagram:
   def __init__(self,username,password):
       self.username = username
       self.password = password
       print(f"Hey {self.username}, Welcome to the Instagram!!!")

sapnil = Instagram("sapnil","s@123")#while creating the object only we have to pass the parameter
neha = Instagram("neha","n@123")


# constructor is the special methods which is initiatize at the movement when you create it, it means that the  method will automatically run without calling it.             
#self is the pointer ,which points to the object(user).
