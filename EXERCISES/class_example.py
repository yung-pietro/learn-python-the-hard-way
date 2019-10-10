class Employee:
    'base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee Count is %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, " Salary: ", self.salary
        #why is there no () after print

"""
    The variable empCount is a class variable whose value is shared among all instances of a
this class. This can be accessed as Employee.empCount from inside the class or outside
the class.

    __init__ is the class constructor.  A special function used when a new instance of the class
(object) is created.

    Methods are called like usual functions, with the exception that the first argument
for each method is 'self'.  You do not, however, need to include self when calling the method.

    """

# Creating Instance objects
emp1 = Employee("Sara", 65,000)
# creates the first object of employee class
emp2 =  Employee("Jeff", 110,000)

#Accessing attributes: You can access an object's attributes using the .operator
emp1.displayEmployee()
emp2.displayEmployee()
