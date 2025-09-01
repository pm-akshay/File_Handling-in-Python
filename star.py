#read()- Reads the entire file or a specified number of characters from the file
#readline()- Reads a single line from the file.

file=open("star.txt")
x=file.read()
print(x)        #here the file pointer reaches the end of the file.

z=file.read(10)
print(z)        #the file pointer has aldready reached the end of the file,no output
file.close()    #closes the file

file=open("star.txt")   #Reopen the file to reset the file pointer to the beginning
y=file.read(5)  
print(y)        #This prints the first 5 characters of the file.

z=file.read(5)
print(z)        #this prints  the next 5 characters.

z=file.readline()
print(z)        #This prints from the file pointer till the end of the line.

m=file.readline(3)
print(m)        #This prints the first 3 characters of the second line. 
