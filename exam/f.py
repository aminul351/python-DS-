def read_file(read, write, max_lines=10):
    read_file = open("f.txt", 'r')
    write_file = open("f_write.txt", 'w')
    
    count = 0
    for line in read_file:
        if count >= max_lines:
            break
        print(line.strip())
        write_file.write("hello")
        count = count + 1
        
    read_file.close()
read_file("f.txt", "f_write.txt")