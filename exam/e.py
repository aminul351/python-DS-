thislist = ["apple", "banana", "cherry"]

for list in thislist:
    print(list)
 
 
 #list comprehension   
[print(x) for x in thislist]

# while 
i = 0
while i<len(thislist):
    print(thislist[i])
    i= i +1