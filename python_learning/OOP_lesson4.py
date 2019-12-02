#python Object-oriented Programming
#lesson 4: Inheritance- Creating Subclassed
 
class Employee:

    raise_amount = 1.04

    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@company.com'

    def showFullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
     
    def __init__(self,firstname,lastname,pay,prog_lang):
        super().__init__(firstname,lastname,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self,firstname,lastname,pay,employees=None):
        super().__init__(firstname,lastname,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.reomve(emp)

    def print_emps(self):
        for emp in self.employees:
            print("->",emp.showFullname())
            

# print(help(Developer))

dev_1 = Developer('Corey-dev','Schafer',10000,'Python')

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.prog_lang)

# print(issubclass(Developer,Employee))


manager_1 = Manager('Kata','Willim',20000,[dev_1])

print(manager_1.email)
manager_1.print_emps()