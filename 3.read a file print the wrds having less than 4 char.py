#READ A TEXTFILE AND PRINT THE WORDS HAVING LESS THAN 4 CHARACTERS

def readfile():
    f=open("star.txt")
    x=f.read()
    for i in x.split():
        if len(i)<4:
            print(i)
    f.close()

readfile()    
