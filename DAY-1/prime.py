#To check given number is prime or not
a = int(input("Enter your number: "))

if(a>1):
    b=int(a**0.5)
    print(b)

    for i in range(2, b+1):
      if a%i == 0:
         print("This is not a prime number")
         break
      else:
          print("This is a prime number")
          break
else:
    print("Number must be greater than 1")
