file=open("sample.csv")
lines=file.readlines()
i=int(input("enter column index : "))
for line in lines:
    print(line.split(",")[i])