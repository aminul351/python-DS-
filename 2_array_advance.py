arr = [2,3,4]
for i in arr:
    sqr = i*i
    print(f"The square of {i} is ", sqr)
    



    
# list comprehension
arr = [2,3,4]
square = [i*i*i for i in arr]
print(square)
    


# use append (i*i)
sqr_list = []
for i in arr:
    square = sqr_list.append(i * i)
print("this is it",sqr_list)
 




# use numpy
import numpy as np;
arr = [2,3,4]
sqr = np.square(arr)
print(sqr)
    


# with range 
sq = []
for value in range(1,11):
    sq.append(value ** 2)
print(sq)



my_arr = range(5,26,5)
print(my_arr)

