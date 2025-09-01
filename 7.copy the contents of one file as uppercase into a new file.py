#Q7.Read a textfile and copy the contents as uppercase into a new file

def readfile(star,cloud):
   with open(star,'r') as f:
       old=f.read()
       nf=old.upper()

   with open(cloud,'w') as new:
       new.write(nf)
   
    
readfile('star.txt','cloud.txt')
