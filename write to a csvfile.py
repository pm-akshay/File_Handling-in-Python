#Prog to write to a csvfile
import csv
with open("names.csv","w",newline='') as file:
    writer=csv.writer(file)
    fields=[["Name","Age","Class","Gender","Mark"],
          ["Akshay",17,"XII","M",100],
          ["Alvin",10,"XII","M",40],
          ["Allen",11,"XII","M",67],
          ["Anuvind",12,"XII","M",50]]
    writer.writerows(fields)
