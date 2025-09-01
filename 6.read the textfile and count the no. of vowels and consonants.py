#Q6.Read a textfile and count the no. of vowels and consonants

def readfile():
    f=open("star.txt")
    x=f.read()
    f.close()
    vowels="AEIOUaeiou"
    vw=0
    cs=0
    for i in x:
        if i in vowels:
            vw+=1
        elif i.isalpha():
            cs+=1
    print("No. of vowels=",vw)
    print('No. of consonants=',cs)
readfile()



