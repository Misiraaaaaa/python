strr=input("enter a string ")
if strr[-3:]=="ing":
    strr=strr+"ly"
else:
    strr=strr+"ing"
print (strr)