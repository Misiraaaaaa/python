keys=input("enter the keys of dict 1 : ").split()
dict1={}
for k in keys:
    value=int(input(f"enter the value for key {k} : "))
    dict1[k]=value 
keys=input("enter the keys of dict 2 : ").split()
dict2={}
for k in keys:
    value=int(input(f"enter the value for key {k} : "))
    dict2[k]=value
dict3=dict1
dict3.update(dict2)
print(dict3)