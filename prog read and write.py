#read and write

f=open('cloud.txt',"r+")
f.seek(1)
data=f.write("e")

f.seek(0)
data1=f.read()
print(data1)    
