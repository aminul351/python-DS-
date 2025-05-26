# person -- class
# we are object 

class Dog:
 
#   class variable 
    
    # method 
    def getName(self):
      return self.name 
  
#   isinstance or object varibale 
  
#   initialization 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
       return f"{self.name} is {self.age} years old"
        
        
dog2 = Dog("Hulu", 45)
print(dog2)
       
  
  
# dog1 = Dog()  # constructor - to help create a obj
# dog1.name = "bubli"
# x= dog1.getName()
# print(x)