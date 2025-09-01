#display all the palandrome in the textfile

with open("star.txt") as f:
    f=f.read()
    s=f.lower().split()
for word in s:
    if word==word[::-1]:
        print(word)
        
