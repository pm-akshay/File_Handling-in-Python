#Q1.INPUT FIVE NAMES AND WRITE INTO TEXTFILE

def writefile():
    f=open("names.txt","w")
    nm=int(input("Enter the total no. of names to be entered :"))
    for i in range(nm):
        n=input("Enter Name:")
        f.write(n+"\n")
    f.close()

writefile()    
