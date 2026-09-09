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

# #append
with open("student.txt","a") as file:
     file.write("vijay\n")
     file.write("hii\n")
     file.write("hello\n")
print("Student appended succesfully")

 #handling file not found KeyError
'''try:
    with open("unknown.txt","r") as file:
        data=file.read()
        print(data)
except FileNotFoundError:
     print("file not found")

# # handles errors vaild numbers,zero diviso=ion error,invalid operarion by persfoming calculation operation
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

#validate age and raise error

def validate_age(age):
    if age<18:
        print("invalid age")
    else:
        print("valid age")
try:
    num=int(input("enter number"))
    validate_age(num)
except ValueError as e:
    print("error",e)'''

#virtual enviroment:it is a seperate python environment used to manage diffent python packages and versions without effecting with other projects

# module:it is a python file contain reusable code such as functions,classes,variables.class

#packages:a folder containing mulitple modules such as .py files

#requirements.txt: pip freeze > requirements.txt 
#if others want to install our file: pip install -r requirements.txt

with open("student.txt","r") as file:
    line=file.readline()
    print(line)

with open("student.txt","r") as file:
    line=file.readlines()
    print(line)
# output is in list format

with open("student.txt","w") as file:
    lines=["hii\n","hell\n","hoo\n"]
    file.writelines(lines)
    print(lines)
#exception handling: exception handling means it is a mechanisms handling exceptions so that it will terminate gracefully instead of crashing the prg
# try: it contains code that may cause errror
# except: it handles the except
# raise: we manually write the errrors
# finally: it runs if contains errror or not
# keyerror,indexerror,typeerror-when we add to different strings,valueerror,attributeerrror
# import error,zero division error,file not found errror 

#writelines:writes mulitlple strings as list
#write :writes in single line
#read:read entire lines as a string
#readline: read one line once
#readlines:read multilple lines as a list

