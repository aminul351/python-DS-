# string 

s = input("Enter a string : ")
reverse = s[::-1]

if(s == reverse):
    print("✅")
else:
    print("❌")
    
    
    
    
# _____ string using function _____ 
def is_palindrome(n):
    return str(n) == str(n)[::-1]
# Test
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
    
  
    
    
    
# numbers 
def is_palindrome(n):
    return str(n) == str(n)[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
    
    
    
# We use str() here to convert the number into a string because:

# Palindrome checking involves comparing the sequence of digits from left to right and right to left.

# Strings in Python can be easily reversed using slicing syntax: [::-1].

# Numbers (integers) don’t support slicing or reversing directly.