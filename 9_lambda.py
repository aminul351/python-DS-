add = lambda x,y : x + y;
print(add(5,3))


# map(function, iterable)
# list ❌   -->  <map object at 0x0000012D5E574910>
numbers = [1,2,3,4]
squared_numbers = list(map(lambda x : x**2, numbers))
print(squared_numbers) # [1, 4, 9, 16]


even_numbers = list(filter( lambda x : x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]