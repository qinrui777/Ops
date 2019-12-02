#python Object-oriented Programming
#lesson 6: Property Decorators-Getters,Setters, Deleters


class Employee:

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        # self.email = firstname + '.' + lastname + '@company.com'

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split(' ')
        self.firstname = firstname
        self.lastname =  lastname

    @fullname.deleter
    def fullname(self):
        print("Delete Name !!!")
        self.firstname = None
        self.lastname =  None


emp_1 = Employee('John', 'Smith')
emp_1.firstname = 'Kate'

emp_1.fullname = 'Corey Schafer' # 设置fullname，需要用到 @fullname.setter

print(emp_1.firstname)
print(emp_1.email)     # 加上 @property 后可以改写 emp_1.email() -> emp_1.email
print(emp_1.fullname)

del emp_1.fullname