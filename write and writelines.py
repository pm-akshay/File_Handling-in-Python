#write()-write() method takes a string as an argument and writes it to the text file
#writelines()- This method is used to write multiple strings to a file.

file=open("Johny.txt","w")
data=file.write("Johny johny yes pappa\neating sugar no pappa\ntelling lies no pappa\n")
print(data)  #this print statement returns no. of charactes in the string
file.close() #the close method is necessary while using write method.
#NOTE- \n is treated as a single character

'''
with open("Johny.txt","w") as w:
    data=w.write("open your mouth\nhaa haa haa\n")#if we run this line then the old string is emptied
    print(data)                                   #and this is written into the file.
'''


'''
      IMPORTANT NOTE:-We need to pass an iterable object like lists,tuple,etc
                      containing strings to writelines()method.
'''

with open("pledge.txt","w") as w:
    lines=["India is my country\n","All indians are my brothers abd my sisters\n","I love my country"]
    data=w.writelines(lines)
    print(data) #this print statement returns None always in writelines() method.


