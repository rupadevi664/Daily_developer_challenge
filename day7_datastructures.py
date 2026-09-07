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
