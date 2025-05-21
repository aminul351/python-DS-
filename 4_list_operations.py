# list - Syntax: my_list = [1, 2, 3]

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
print(bicycles.pop(0))   # trek - remove and return the i index
print(bicycles)   # ['cannondale', 'redline', 'specialized']
print(bicycles.remove('cannondale'))



cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()  # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True) # ['toyota', 'subaru', 'bmw', 'audi']

cars.reverse()  # ['subaru', 'toyota', 'audi', 'bmw']
print(cars)
