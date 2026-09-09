#largest number:
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