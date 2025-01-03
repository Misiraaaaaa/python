
num=int(input("enter the number whose factorial is to be found"))
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("factorial : " ,factorial(num))
    
