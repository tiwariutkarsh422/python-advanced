class PayrollSystem:
  def salary_calculator(self, employees):
    print('Salary of every category employee')
    print('----------------------------------')
    print()
    for employee in employees:
      print(f'Payroll for Employee id: {employee.id} , Employee name: {employee.name}')
      print(f'Total amount: {employee.calculate_salary()}')
      print()

class Employee:
  def __init__(self, id, name):
    self.name = name
    self.id = id

class SalaryEmployee(Employee):
  def __init__(self, id, name, weekly_salary):
    super().__init__(id, name)
    self.weekly_salary = weekly_salary

  def calculate_salary(self):
    return self.weekly_salary

class HourlyEmployee(Employee):
  def __init__(self, id, name, total_hours_worked, hourly_rate):
    super().__init__(id, name)
    self.total_hours_worked = total_hours_worked
    self.hourly_rate = hourly_rate

  def calculate_salary(self):
   return self.total_hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
  def __init__(self, id, name, weekly_salary, commission_amount):
    super().__init__(id, name, weekly_salary)
    self.commission_amount = commission_amount

  def calulate_salary(self):
    fixed_salary = super().calculate_salary()
    return fixed_salary + self.commission_amount


  
