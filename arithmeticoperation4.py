a=int(input("enter 1st number "))
b=int(input("enter 2nd number "))
print("1:ADD0 \n2:SUB \n3:MUL \n4:DIV " )
op=int(input(" select ur option"))
if op==1:
    print("SUM =", a+b)
elif op==2:
    print("DIFFERENCE =", a-b)
elif op==3:
    print("PRODUCT =", a*b)
elif op==4:
    print("QUOTIENT =", a/b)
else:
    print(" INVALID CHOICE")
