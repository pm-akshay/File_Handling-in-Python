'''
Consider a binary file, items.dat, containing records stored in the given format:
{item_id: [item_name,amount]}
Write a function, Copy_new(), that copies all records whose amount is greater than
1000 from items.dat to new_items.dat.
'''
import pickle

def write_new():
    with open("items.dat","wb") as f:
        n=int(input("Enter no. of items to be entered:"))
        d={}
        for i in range(n):
            l=[]
            item_id=int(input("Enter item id:"))
            item_name=input("Enter the name of item:")
            amt=int(input("Enter the amount:"))
            l.append(item_name)
            l.append(amt)
            d[item_id]=l
        print(d)


def copy_new():
    f1=open("items.dat","rb")
    f2=open("new_items.dat","wb")
    while True:
        try:
            data=pickle.load(f1)
            for k,v in data.items():
                if v[1]>1000:
                    newdict={k:v}
                    pickle.dump(newdict,f2)
        except EOFError:
            pass
            
write_new()            
copy_new()            
            













            
