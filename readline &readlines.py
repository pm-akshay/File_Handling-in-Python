#readline-Reads one line from the file at a time.
#readlines-Reads all lines from the file at once and returns them as a list of strings.

file=open("star.txt",)
f=file.readline(2)
print(f)     #This prints the first 2 characters in the file
f=file.readline()
print(f)     #This prints the from the file pointer till end
file.close()

with open("star.txt") as f:
    data=f.readline(15)
    print(data)
    data=f.readline(10)
    print(data)  #when we write anything outside "with" clause,it closes the file automatically

file=open("star.txt")
data=file.readlines()
print(data)   #This prints all the lines in a list of stringswith a \n character at end of each string in the list.
file.close()

file=open("star.txt")
data=file.readlines(5)  #However, readlines() typically reads entire lines, so the 5 will influence how many bytes are read,
print(data)             #but the method will still return entire lines that total around 5 bytes or more.
data=file.readlines(6)
print(data)             #This prints the second line beacause the file pointer already reached the EOF of first line.

with open("star.txt") as f:
    data=f.readlines()
    for line in data:
        word=line.split()
        print("\n",word)

with open("star.txt") as f:
    data=file.readlines()
    for line in data:
        word=line.splitlines()
        print(word)









    
