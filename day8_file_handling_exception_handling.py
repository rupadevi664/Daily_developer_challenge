#create a file student.txt and write five student names into it
with open("student.txt","w") as file:
    file.write("Ravi\n")
    file.write("Rupa\n")
    file.write("mahi\n")
    file.write("sravani\n")
    file.write("durga\n")
print("students added succesfully")

with open("student.txt","r") as file:
    for students in file:
        print(students.strip())

#append
with open("student.txt","a") as file:
    file.write("vijay\n")
    file.write("hii\n")
    file.write("hello\n")
print("Student appended succesfully")

#handling file not found KeyError
try:
    with open("unknown.txt","r") as file:
        data=file.read()
        print(data)
except FileNotFoundError:
    print("file not found")

# handles errors vaild numbers,zero diviso=ion error,invalid operarion by persfoming calculation operation
try:
    num1=int(input("enter number:"))
    num2=int(input("enter number:"))
    operation=input("enter operation +,-,*,/")

    if operation=="+":
        print("result",num1+num2)
    elif operation=="-":
        print("result",num1-num2)
    elif operation=="*":
        print("result",num1*num2)
    elif operation=="/":
        print("result",num1/num2)
    else:
        raise ValueError("entered invalid operation") 
except ValueError:
        print("invalid number")
except ZeroDivisionError:
    print("can not divided by zero") 



