a = "d"
print(type(a))


students_list = ["Bob", 9, "Rahim"]

print(type(students_list[0])) # <class 'str'>
print(type(students_list[1])) # <class 'int'>
str = str(students_list[1])  # int -> str
print(type(str))   # <class 'str'>



students_list.append("Amena")
print(students_list)  # ['Bob', 9, 'Rahim', 'Amena']

students_list = list(("BOB", "BOBI" )) # evabe o list likha jay 
print(students_list[0]) # BOB 

students_list.insert(2, "sakib")
print(students_list) # ['BOB', 'BOBI', 'sakib']

# students_list.pop() # ['BOB', 'BOBI'] - last item ❌
students_list.pop(1) # i th index ❌
students_list[1:2] # slice index wise (start - end)  -- ['BOBI']
print(students_list)

ex_list = ['Aminul', 'Mostafa', 'Rafi', 'Tanzim']
students_list.extend(ex_list)
print(students_list)


for x in students_list:
    print(x)
    
    
# list comprehension 
[print(x) for x in students_list]

length = len(students_list)
print(length)


st_list = ["Bob", "Amena", "Rahim", "Alice", "Sakib"]
for i in range(length):       # length - 2 ; desirable value
    if (st_list[i] == "Amena"):
        break
    if (st_list[i] == "Sakib"):
        continue
    print(st_list[i])
