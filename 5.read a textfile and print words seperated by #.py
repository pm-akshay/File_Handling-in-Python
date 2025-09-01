#Q5.Read a textfile and print the words seperated by #

def readfile():
    f=open("star.txt")
    d=f.read()
    x=d.replace(' ','#')
    print(x)
    f.close()

readfile()    
        
