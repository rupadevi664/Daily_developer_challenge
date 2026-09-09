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
if count==1:
    print(1)
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

a="aaeerupa"
unique=[]
for char in a:
    if char not in unique:
        unique.append(char)
print(unique)