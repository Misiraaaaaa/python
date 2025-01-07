datadict=[{"rollno":"3","name":"babu"},{"rollno":"4","name":"yadhu"},]
titles=list(datadict[0].keys())
file=open("result.csv","w")
header=",".join(titles)
file.write(header+"\n")
for data in datadict:
    valuelist=list(data.values())
    row=",".join(valuelist)
    file.write(row+"\n")
file.close()