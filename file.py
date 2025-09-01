import csv
file=open('file.csv')
reader=csv.reader(file,delimiter='#')
print(reader)

for row in reader:
    print(row)
