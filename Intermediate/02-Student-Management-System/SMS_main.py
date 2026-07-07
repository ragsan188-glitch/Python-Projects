
students={}

def f1():
    stu={}
    roll_number=int(input("Enter roll number: "))
    name=input("Enter name: ").lower()
    age=int(input("Enter age: "))
    department=input("Enter department: ").lower()
    marks=int(input("Enter marks: "))
    stu["name"]=name
    stu["age"]=age
    stu["department"]=department
    stu["marks"]=marks
    students[f'{roll_number}']=stu

def f2():
    l1=list(students.values())
    n=len(students)
    for i in range(n):
        print(f'+++++student no{i}+++++')
        print("name:",l1[i]['name'])
        print("age:", l1[i]['age'])
        print("department:", l1[i]['department'])
        print("marks:", l1[i]['marks'])

def f3():
    n=int(input("1.SEARCH WITH ROLL NUMBER\n2.SEARCH WITH NAME"))
    if n==1:
        roll=int(input("Enter roll number: "))
        if f'{roll}' in students.keys():
            print(students[f'{roll}'])
        else:
            print("roll does not exist")
    elif n==2:
        name=input("Enter name: ").lower()
        found=False
        for roll, details in students.items():
            if details["name"] == name:
                print("Roll Number:", roll)
                print(details)
                found = True
                break
        if not found:
            print("student does not exist")

def f4():
    roll=input("Enter roll number: ")
    if roll in students:
        students[roll]['marks']=int(input("Enter updated marks: "))
        print("Marks updated successfully.")
    else:
        print("Roll does not exist.")

def f5():
    roll=input("Enter roll number: ")
    if roll in students:
        del students[roll]
        print("student deleted successfully.")
    else:
        print("roll does not exist.")

def f6():
    if len(students)==0:
        print("No students found.")
        return
    else:
        sum=0
        n=0
        for i in students:
            sum=sum+students[i]["marks"]
            n=n+1
        print("Class Average:",sum/n)

        topper= None
        highest=-1
        for i,j in students.items():
            if j["marks"]>highest:
                highest=j["marks"]
                topper=i
        print("Topper:",topper)
        print(students[topper]["name"])

        k=0
        for i in students:
            k+=1
        print("Total number of students:",k)

def f7():
    a=int(input("sort by\n1.Roll number\n2.Name"))
    if a==1:
        x=dict(sorted(students.items()))
        print(x)
    elif a==2:
        x=dict(sorted(students.items(),key=lambda item:item[1]['name']))
        print(x)
    else:
        print("wrong input")

def f8():
    print("exited Successfully")







def menu():
    while True:
        print("+++++Welcome to the Student Management System+++++")
        print("1.ADD STUDENT")
        print("2.VIEW STUDENTS")
        print("3.SEARCH STUDENT")
        print("4.UPDATE MARKS")
        print("5.DELETE STUDENT")
        print("6.CLASS STATISTICS")
        print("7.SORT STUDENTS")
        print("8.EXIT")


        l=int(input("Enter your choice: "))
        if l==1:
            f1()
        elif l==2:
            f2()
        elif l==3:
            f3()
        elif l==4:
            f4()
        elif l==5:
            f5()
        elif l==6:
            f6()
        elif l==7:
            f7()
        elif l==8:
            f8()
            break
        else:
            print("wrong input")
menu()

