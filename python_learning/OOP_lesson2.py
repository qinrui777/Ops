#python Object-oriented Programming
#lesson 2: class variables
#instance variables VS calss variable

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@company.com'
        Employee.num_of_emps += 1

    def showFullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey','Schafer',1000)
emp_2 = Employee('Corey2','Schafer',1000)

emp_1.raise_amount =1.06

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# print(emp_1.__dict__)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)



# class Employee:

#     def __init__(self,firstname,lastname,pay):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.pay = pay
#         self.email = firstname + '.' + lastname + '@company.com'

#     def showFullname(self):
#         return '{} {}'.format(self.firstname,self.lastname)

#     def apply_raise(self):
#         self.pay = int(self.pay * 1.04)

# emp_1 = Employee('Corey','Schafer',1000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)