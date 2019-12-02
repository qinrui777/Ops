#python Object-oriented Programming
#lesson 5: Special(Magic/Dunder) method
#Special method list:  https://docs.python.org/3/reference/datamodel.html#special-method-names
# 类似__xxx__的属性和方法在Python中都是有特殊用途的

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

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.firstname, self.lastname, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.showFullname(),self.email)


emp_1 = Employee('Corey','Schafer',1000)
emp_2 = Employee('Test','Employee',1400)

# print(len('test'))
# print('test'.__len__())

print(1+2) # 实际上运行的 print(int.__add__(1,2))
print('a' + 'b') # 实际上运行的 print(str.__add__('a','b'))

print(emp_1.__repr__()) # 等价于 print(repr(emp_1))
print(emp_1.__str__()) # 等价于 print(str(emp_1))
