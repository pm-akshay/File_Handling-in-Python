#Q8.Count the no. of lines in a textfile

def readfile():
    with open("star.txt") as f:
        file=f.readlines()
        print("Total no.of lines in this textfile=",len(file))
readfile()        
