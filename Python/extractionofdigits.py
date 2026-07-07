# extracting digits 

n = 5873
num = n
while num > 0:
    last_digit = n//10%10
    num = num//10
print(last_digit)
