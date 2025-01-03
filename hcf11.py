a=int(input("enter first number : "))
b=int(input("enter second number : "))
hcf=0
for i in range (1,min(a+1,b+1)):
    if a%i==0 and b%i==0:
        hcf=i
        
print("the hcf of",a,"and",b,"is",hcf)
