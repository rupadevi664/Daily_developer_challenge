#data sturcture: it is a way of orgaining the code so that we access it efficently.
#index
students=["rupa","mahesh","sravani"]
students.insert(1,"mani")
print(students)

#append
students=["rupa","mahesh","sravani"]
students.append(["durgarao","append"])
print(students)

#extend
students=["rupadevi","mahesh"]
students.extend(["hi","hello"])
print(students)

#remove by value
students=["rupa","mahesh","sravani"]
students.remove("rupa")
print(students)

#pop
students=["r","m","s"]
students.pop()
print(students)

#delete
students=["r","m","s"]
del students[1]
print(students)

#clear
students=["r","m","s"]
students.clear()
print(students)
#reverse
students=["r","m","s"]
students.reverse()
print(students)

#copy
students=["r","m","s"]
student=students.copy()
print(student)

#sort
students=[4,1,2,3]
students.sort()
print(students)

#set
a={1,2,3,5,4,55,99}
# a.add(123)
# print(a)
# a.pop()
#print(a)
# a.remove(1)
# print(a)
a.update({53,23,54,6887})
print(a)
