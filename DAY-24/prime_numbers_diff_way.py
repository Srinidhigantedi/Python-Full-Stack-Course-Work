def isprime(n):
    for i in range (2,n//2+1):
        if n%i == 0:
            return "Not a Prime Number"
    return "Prime Number"       
def main():
    n = int(input("Enter the number: "))
    print(isprime(n))        
main()
