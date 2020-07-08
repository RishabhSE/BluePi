class Employee:
    # Class Variable
    raise_amt = 1250
    no_of_employees = 0

    # Initializer / Instance Attributes
    def __init__(self,f_name,l_name,pay):
        self.f_name = f_name
        self.l_name = l_name
        self.pay = pay
    # Since __init__ method will get initiated each time we add an employee
        Employee.no_of_employees += 1
    
    # instance method
    def full_name(self) :
        return "{} {}".format(self.f_name,self.l_name)

    # instance method
    def email(self) :
        return "{}.{}@gamil.com".format(self.f_name,self.l_name)
    
    def raise_amount(self) :
        return self.pay + self.raise_amt

# Printing no. of employess before initiating
print(Employee.no_of_employees)

# Instantiate the object
emp_1 = Employee("Ram","Singh",30000)
emp_2 = Employee("Kabir","Pal",90000)

# Printing no. of employess before initiating
print(Employee.no_of_employees)

# Access the instance attributes 
# print( emp_1.full_name() )
# print( Employee.email(emp_1) )

# Accessing the raised amt though class and instances
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
# print(Employee.raise_amt)

# Printing the namespace of the classes and instances
# print(emp_1.__dict__)
# print(emp_2.__dict__)
# print(Employee.__dict__)

# Changing the raise_amt through class
# Employee.raise_amt = 1999
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
# print(Employee.raise_amt)

# Changing the raise_amt through instances
# emp_1.raise_amt = 1999
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
# print(Employee.raise_amt)

# print(emp_1.raise_amount())
# print(emp_2.raise_amount())



