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
unique=""
for char in a:
    if char not in unique:
        unique=unique+char
print(unique)
#output aerup
#contain duplicate
a=["a","t","y","r","t"]
freq={}
for char in a:
 
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1
for char in freq:
    if freq[char]>1:
        print(char)
   
  
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

#count
n=1234
count=0
while n>0:
    count=count+1
    n=n//10
print(count)

#sum
num=12334
total=0
while num>0:
    digit=num%10
    total =total+digit
    num=num//10
print(total)

#uppercase & lowercase
n="rupadevi"
uppercase=0
lowercase=0
for char in n:
    if char>="A" and char<="Z":
        uppercase+=1
    elif char>="a" and char<="z":
        lowercase+=1
print(uppercase)
print(lowercase)

#anagram
s1="listentt"
s2="silenttt"
if len(s1)!=len(s2):
    print("Not anagram")
    
for char in s1:
    if char not in s2:
        print("Not Anagram")
        break
else:
    print("Anagram")

#non-repeating character
a="rupadevi"
freq={}
for char in a:
    if char in " ":
        continue
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1

    if freq[char]==1:
        print(freq)
        break
else:
    print("not repeating")

 #repeating first char 
a="rupadeviiii"
freq={}
for char in a:
    if char in " ":
        continue
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1
for char in freq:
    if freq[char]>=1:
        print(char)
        break
  
#frequency count
a="bannaana"
frequency={}
for char in a:
    if char in " ":
        continue
    if char in frequency:
        frequency[char]=frequency[char]+1
    else:
        frequency[char]=1
print(frequency)

#armstrong 1^3 *5^3 3^3
n=153
original=n
total=0
while n>0:
    digit=n%10
    total=total+digit*digit*digit
    n=n//10
if original==total:
    print("Armstrong")
else:
    print("Not Armstrong")
#reverse
n=123
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
print(reverse)

#palindrome
n=12321
original=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10 + digit
    n=n//10
if original==reverse:
    print("palindrome")
else:
    print("Not palindrome")

#prime
n=30
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")

#count
n=12345
count=0
while n>0:
    count+=1
    n=n//10
print(count)

#sum
n=1234
sum=0
while n>0:
    digit=n%10
    sum= sum+digit
    n=n//10
print(sum)

#fact
a=5
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)

#fibonnce
n=5
a=0
b=1
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c
print()
#moves zero
a=[10,203,334,23,0,0,2,0,2,0,2]
result=[]
for i in a:
    if i!=0:
        result=result+[i]
for i in a:
    if i==0:
        result=result+[i]
print(result)

#missing

