"""
A process of wrapping code and data together into single unit.
"""

# Encapsulation

class Emp:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal
    
    def com(self):
        print(self.name,'Salary is',self.sal)


class Address(Emp):

    def print(self):
        print('New colony')

# Objects
em1 = Address('Rutu',5000)

# Call function using Objects
em1.com()
em1.print()