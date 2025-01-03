#strr=input("enter a string ")
#count=0
#for char in strr:  
#    for _ in strr:
#        if _==char:
#            count=count+1
#    print(" the frequency of ",char," is ",count)
#    count=0 

strr=input("enter a string ")
newstr=set(strr.lower())
for j in newstr:
    count=0

    for i in strr:
        if i==j:
            count+=1
    print(f"frequency of {j} is {count}")
