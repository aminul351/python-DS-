def function(a,b):
    return  a + b;
print(function(4,5))


# x = [5,6,7]
# x = list(5,6,7)

points = [(1,2), (4,1), (3,3), (2,4)]
sorted_point = sorted(points, key=lambda point : point[1])
print(sorted_point)