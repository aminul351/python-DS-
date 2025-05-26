class Employee:
    def __init__(self, id, name,  salary):
        self.id = id
        self.name = name
        self.salary = salary
        
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
    def __str__(self):
        return f"{self.name} salary is {self.salary}"
    
    
    
student1 = Employee(22, "Aminul", 30000)
print(student1.getName(), "salary is " ,student1.getSalary())
print(student1)

        
        
        
        