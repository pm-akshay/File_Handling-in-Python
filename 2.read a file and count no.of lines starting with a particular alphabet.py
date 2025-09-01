#READ A TEXTFILE & COUNT THE NO. OF LINES STARTING WITH I OR i

def readfile():
    f=open("star.txt")  #opens the file in read mode by default
    x=f.readlines()
    c=0
    for i in x:
        if i.startswith("I") or i.startswith("i"):
            c+=1
    print("No. of lines starting with I or i:",c)
    f.close()
readfile()    
