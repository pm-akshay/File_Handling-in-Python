import csv

# Open the CSV file in write mode
with open("data1.csv", "w", newline='') as file:
    writer = csv.writer(file)
    
    fields = ["Name", "Age", "Class", "Gender", "Mark"]
    writer.writerow(fields)
    
    n = int(input("Enter the number of data entries to be added: "))
    
    for i in range(1,n+1):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        Class = input("Enter class: ")
        gender = input("Enter gender: ")
        mark = int(input("Enter mark: "))
        print(i,"row inserted")
        
        writer.writerow([name,age,Class,gender,mark])

print("Data successfully written to data1.csv.")


