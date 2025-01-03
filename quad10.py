from math import sqrt as sq
a=int(input("enter the coefficient of x² (a)"))
b=int(input("enter the coefficient of x (b)"))
c=int(input("enter the constant (c)"))
det=((b*b)-(4*a*c))

if det==0:
    print("one real root whic is :" ,(-b+sq(det))/(2*a))
elif det>0:
    print("two real root whic is :" ,(-b+sq(det))/(2*a),"and :" ,(-b-sq(det))/(2*a))
else:
    print("no real roots")
    
