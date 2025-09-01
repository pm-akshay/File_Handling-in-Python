#Q4.Read a textfile & count no of times the word 'twinkle' appears in the textfile.

def readfile():
    f=open("star.txt")
    x=f.read()
    c=0
    for i in x.split():
        if i=='twinkle':
            c+=1
    print("No. of times the word 'twinkle' appear in the file:",c)
    f.close()
readfile()    
            
        
        
