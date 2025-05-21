student_info = ["Bob", "Alice", "Rahim"]
i = 0
while i < len(student_info):
    if(student_info[i] == "Bob"):
        i+=1
        continue
    print(student_info[i])
    i+=1
    
    
for i in student_info:
    if(i == "Bob"):
     continue
    print(student_info)