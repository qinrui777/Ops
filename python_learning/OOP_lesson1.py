#python Object-oriented Programming
#lesson 1: class ,instance

class Employee:

    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@company.com'

    def showFullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

# emp_1 = Employee()
# emp_2 = Employee()

# emp_1.firstname = 'Corey'

emp_1 = Employee('Corey','Schafer',1000)

# print(emp_1.email)
print(emp_1.showFullname())
print(Employee.showFullname(emp_1))

print(isinstance(emp_1,Employee))
