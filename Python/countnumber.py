from math import *

n = 5438
num = n
count = 0
while num > 0:
    count+=1
    num = num//10
print(count)

k = int(input("enter any number to count digit"))
num1 = n
def countDigits(num1):
    return int(log10(num1)+1)
print(countDigits)