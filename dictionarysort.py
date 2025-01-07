dict1={2:"sdfgh",4:"xcvbn",1:"ertyui",3:"cvghu",}
mylist=list(dict1.keys())
print(mylist)
mylist.sort()
print(mylist)
print("{",end=" ")
for i in mylist:
    print(i," : ",dict1[i]," , ",end="")
print("}",end=" ")
print("{",end=" ")
for i in mylist[::-1]:
    print(i," : ",dict1[i]," , ",end="")
print("}",end=" ")
