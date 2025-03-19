# Main file
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, emp_name, emp_dept):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._emp_dept = emp_dept

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("--- Employee Details ---")
        print(f"Employee ID: {self._emp_id}")
        print(f"Name: {self._emp_name}")
        print(f"Department: {self._emp_dept}")

class PermanentEmployee(Employee):
    def __init__(self, emp_id, emp_name, emp_dept, base_salary, bonus):
        super().__init__(emp_id, emp_name, emp_dept)
        self._base_salary = base_salary
        self._bonus = bonus

    def calculate_salary(self):
        return self._base_salary + self._bonus

    def display_details(self):
        super().display_details()
        print(f"Base Salary: ${self._base_salary:.2f}")
        print(f"Bonus: ${self._bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class ContractEmployee(Employee):
    def __init__(self, emp_id, emp_name, emp_dept, hourly_rate, hours_worked):
        super().__init__(emp_id, emp_name, emp_dept)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def calculate_salary(self):
        return self._hourly_rate * self._hours_worked

    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self._hourly_rate:.2f}")
        print(f"Hours Worked: {self._hours_worked}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

class Intern(Employee):
    def __init__(self, emp_id, emp_name, emp_dept, stipend):
        super().__init__(emp_id, emp_name, emp_dept)
        self._stipend = stipend

    def calculate_salary(self):
        return self._stipend

    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self._stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}\n")

if __name__ == "__main__":
    employees = [
        PermanentEmployee("P001", "Alice Johnson", "IT", 60000, 5000),
        ContractEmployee("C002", "Bob Smith", "HR", 50, 160),
        Intern("I003", "Charlie Brown", "Finance", 1500)
    ]
    
    for emp in employees:
        emp.display_details()
