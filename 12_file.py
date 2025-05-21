# class code 
# f = open("c:\\practice\\employeee.txt", "r")
# f1 = open("c:\\practice\\employeeCTG.txt", "w")

# firstline = f.readline()
# f1.write(firstline)

# lines = f.readlines()

# for i in lines:
#     list_emp = i.split(' ')
#     print(list_emp)
#     if list_emp[2].strip() == 'CTG':  # Use strip() here
#         f1.write(i)

# f.close()
# f1.close()















f = open("text.txt", "r")
# text = f.readline()  # first line
text = f.readlines()  # ['line1\n', 'line2\n', 'line3\n']
print(text)


f1 = open("text2.txt", "w")
# f1.write("hello hello!")
# print(f1)

for i in text:
    list_emp = i.split(' ')
    print(list_emp)
    
    if list_emp[2] == 'b\n': 
        f1.write(i) 
        
f.close()  
f1.close()  