#python Object-oriented Programming
#lesson 3: classmethods and staticmethods
 
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
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        firstname, lastname, pay = emp_str.split('-')
        return  cls(firstname, lastname, pay)   

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday ==6:
            return False
        return True

emp_1 = Employee('Corey','Schafer',1000)
emp_2 = Employee('Corey2','Schafer',1000)

emp_str_1 = 'John-Doe-12000'
emp_str_2 = 'Steve-Smith-15000'

# firstname, lastname, pay = emp_str_1.split('-')
# new_emp_1 = Employee(firstname, lastname, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)


import datetime
my_date = datetime.date(2016,7,10)

print(Employee.is_workday(my_date))