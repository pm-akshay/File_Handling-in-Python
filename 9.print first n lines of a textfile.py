#Q9.print first n lines of a textfile

def readfile():
    n=int(input("Enter the no.of lines to print:"))
    lines=open('star.txt').readlines()

    for i in range(n):
        print(lines[i],end='')

readfile()
