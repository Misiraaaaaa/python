num=input("enter the list of numbers").split()
noneven=[]
for _ in num:
    if (int(_)%2!=0):
        noneven.append(_)
print(noneven)