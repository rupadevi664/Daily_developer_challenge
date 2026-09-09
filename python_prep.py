#largest number:
from sys import int_info
num=[1,2,3,4,5]
largest=num[0]
for n in num:
    if n>largest:
        largest=n

print(largest)

#second
n=[1,2,3,4,5,6,7,8,9]
largest=n[0]
second=n[0]
for num in n:
    if num>largest:
        second=largest
        largest=num
    elif second>num and num!=largest:
        second=num
print(largest)
print(second)

n=[1,2,3,4,5]
smallest=n[0]
for num in n:
    if num<smallest:
        smallest=num
print(smallest)

#reverse string
a="rupa"
reverse=""
for char in a:
    reverse=char+reverse
print(reverse)

#palindrome
n="madam"
original=n
reverse=""
for char in n:
    reverse=char+reverse
if original==reverse:
    print("palindrome")
else:
    print("not palindrome")

#even odd
n=[3,7,9,2,6]
even=0
odd=0
for num in n:
    if num%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)

#sum
n=123334
total=0
while n>0:
    digit=n%10
    total=total+digit
    n=n//10
print(total)

#count
n=12
count=0

while n>0:
    count=count+1
    n=n//10
print(count)

#count prime num
n=7
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")

#vowels
a="stringaeiou"
vowels=0
for char in a:
    if char in "aeiouAEIOU":
       vowels+=1
print(vowels)
#remove duplicates
a="aaeerupa"
unique=[]
for char in a:
    if char not in unique:
        unique.append(char)
print(unique)


#linear search
n=[10,20,23,43,46]
search=20
for num in range(len(n)):
    if n[num]==search:
        print("search found",i)
        break
else:
    print("not found")

#frequency of elements
num=[1,1,1,2,3,4,56,67654,12,33,55]
target=1
count=0
for n in num:
    if n==target:
       count+=1
print(count)


#factorial
n=5
fact=1
for num in range(1,n+1):
    fact*=num
print(fact)

#fabonocci
n=9
a=0
b=1
for i in range(n):
    print(a,end=",")
    c=a+b
    a=b
    b=c
print()

num1=[12,34,54,762,344,72,90]
max=num1[0]
min=num1[0]
for n in num1:
    if n>max:
        max=n
    elif n<min:
        min=n
print(max)
print(min)

#