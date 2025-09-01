'''
CREATE A CSV FILE WITH EMPNO, NME AND SALARY OF N
EMPLOYEES DISPLAY THE FILE. ALSO DISPLAY THE EMPLOYEES
EARNING SALARY>15000.
'''
import csv
def createemp():#write rows 
    
    n=int(input("Enter no: of employees"))
    record=[]
    with open('employee.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Empno", "Name", "Salary"])
            for i in range(n):
                 empno=int(input("enter empno" ))
                 name= input("enter name" )
                 salary= int(input("enter salary"))
                 record.append([empno,name,salary])
            writer.writerows(record)     
def reademp():
    with open('employee.CSV', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
def search():
    
    f=open("employee.csv",'r')
    csvr=csv.reader(f)
    x=next(csvr)
    
    for row in csvr:
                eno,ename,salary = row[0], row[1], int(row[2])
                if salary > 15000:
                    print(f"{eno} {ename} {salary}")
    

createemp()
reademp()
search()
