#copy from one file to another

def copyfile(copyfrom,copyto):
    file=open(copyfrom)
    file1=file.read()
    file.close()


    file2=open(copyto,"w")
    file2.write(file1)
    file2.close()

copyfile('star.txt','file.txt')
