class Employee():
    def __init__(self, emp__id, salary):
        self.emp__id = emp__id
        self.salary = salary

    def give_raise(self):
        self.salary = self.salary*1.05

    def give_cut(self):
        self.salary = self.salary/1.05

    def __repr__(self):
        return f'<Employee ID: {self.emp__id} Employee Salary: {self.salary}>'

class Manager(Employee):

    def give_raise(self):
        self.salary = self.salary*1.10

    def give_cut(self):
        self.salary = self.salary - 10000

    def __repr__(self):
        return f'<Manager ID: {self.emp__id} Manager Salary: {self.salary}>'

emp1 = Employee(101, 100000)
#
# print(type(emp1))
#
# print(emp1.emp__id)
#
# print(emp1.salary)
#
# emp1.give_raise()
#
# print(emp1.salary)
#
# emp1.give_raise()
#
# print(emp1.salary)
#
# emp1.give_cut()
#
# print(emp1.salary)
#
# print(emp1)

mgr1 = Manager(202, 150000)

# print(type(mgr1))
# print(mgr1)
#
# print(mgr1.salary)
# mgr1.give_cut()
# print(mgr1.salary)

class Director(Employee):

    def give_raise(self):
        self.salary = self.salary*1.20

    def __repr__(self):
        return f'<Director ID: {self.emp__id} Director Salary: {self.salary}>'

drctr1 = Director(303, 300000)

# print(type(drctr1))
# print(drctr1)
#
# print(drctr1.salary)
# drctr1.give_raise()
# print(drctr1.salary)

emp1 = Employee(101, 100000)
mgr1 = Manager(202, 150000)
drctr1 = Director(303, 300000)

Staff = [emp1, mgr1, drctr1]

for emp in Staff:
    print(emp)

for emp in Staff:
    emp.give_raise()
    print(emp.salary)

