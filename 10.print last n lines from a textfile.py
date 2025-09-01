#Q10.wap to print last n lines from a textfile

with open("star.txt") as f:
    data=f.readlines()
    n=int(input("Enter the no.of lines to be printed from last to top:"))
    for i in data[-n:]:
        print(i,end='')
        
        
