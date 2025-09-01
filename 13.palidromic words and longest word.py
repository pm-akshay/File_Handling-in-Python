#A menu driven program to accept a line of text and to
#Print the palindromic words ,Display the longest word

def palword(n):
    print("Palindromic Words are:")
    for word in n.split():
        if word==word[::-1]:
            print(word)

def longword(n):
    s=''
    for word in n.split():
        if len(word)>len(s):
            s=word
    print("The Longest word is",s)

while True:
    n=input("Enter a line of text: ")
    print("1.Palindromic Words: ")
    print("2.Longest Word: ")
    choice=int(input("Enter your choice:"))
    
    if choice==1:
        palword(n)
    elif choice==2:
        longword(n)
    else:
        print("Invalid Choice.Exiting")
        break
    c=input("Do you want to continue(Y/N):")
    if c.upper()!="Y":
        break
         
        
        
    
