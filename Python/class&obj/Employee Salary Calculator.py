class Employee:
    def __init__(self, name, salary, department):  
        self.name = name
        self.salary = salary
        self.department = department

    def give_bonus(self):
        bonus = self.salary * 0.10
        new_salary = self.salary + bonus
        return new_salary


name = input("Enter employee name: ")
salary = int(input("Enter employee salary: "))
department = input("Enter employee department: ")


emp = Employee(name, salary, department)

new_salary = emp.give_bonus()
print("New salary after bonus will be:", new_salary)
