# ___sir___
def fact(n):
    fact = 1;
    while(n>0):
        fact *= n;
        n = n-1;
    return fact;
    
print(fact(5))
   
    
# ___YT___
num = 5
fact = 1
a = 1
while a <= num:
    fact = fact * a
    a = a +1
print(fact)
   
   
# 😁
import math
print(math.factorial(5))


# ___loop___
num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print(fact)


# ____user defined function_____ 
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(5))