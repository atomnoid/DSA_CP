#check if its a palindrome or not 

n = 1111
num = n
result = 0

while num>0:
    ld=num%10
    result = (result*10)+ld
    num = num//10
print(n==result)