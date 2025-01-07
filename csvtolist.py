file=open("sample.csv","r")
lines=file.readlines()
file.close()
listt=[]
for line in lines:
    listt.append(line)
print(listt)