a=5
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
for i in range(a+1,0,-1):
    for j in range(i+1,1,-1):
        print("*",end=" ")
    print("\n")