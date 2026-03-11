class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        
    def calculate_bonus():
        pass
    
class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        
    def calculate_bonus(self):
        salary_with_bonus = self.salary + (self.salary * 0.20)
        print(salary_with_bonus)
    
class Developer(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        
    def calculate_bonus(self):
        salary_with_bonus = self.salary + (self.salary * 0.10)
        print(salary_with_bonus)
    
    
manager1 = Manager("Sample Manager", "000001", 50000)
developer1 = Developer("Sample Developer", "000002", 30000)

manager1.calculate_bonus()
developer1.calculate_bonus()