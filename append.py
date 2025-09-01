#append mode - used to write data to a textfile.
#file pointer will always be at the end of the file

with open("1.txt","a") as f:
    x="\nEarth"
    f.write(x)

with open("1.txt","a") as f:
    y='\nVenus'
    f.write(y)
    
