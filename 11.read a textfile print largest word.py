#Q.11 read a textfile and print largest word

def largeword():
    with open("star.txt") as f:
        words=f.read().split()
        largestword=''
        for word in words:
            if len(word)>len(largestword):
                largestword=word
        print("The largest word is:",largestword)        
            
largeword()        

