a=int(input("enter 1st number "))
b=int(input("enter 2nd number "))
c=int(input("enter 3rd number "))
if(a>b & a>c):
    print(f"{a} is the greatest")
elif(b>c):
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")
