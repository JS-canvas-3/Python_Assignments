class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

from employee import Employee
emp = Employee("Siva Shankar", 50000)

print("Employee Name:", emp.get_name())
print("Employee Salary:", emp.get_salary())