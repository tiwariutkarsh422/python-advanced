class PayrollSystem:
  ''' This method takes a list of employees and calculates there salaries using caluclate_salary()
      method.'''
  def salary_calculator(self, employees):
    print('Salary of every category employee')
    print('----------------------------------')
    print()
    for employee in employees:
      print(f'Payroll for Employee id: {employee.id} , Employee name: {employee.name}')
      print(f'Total amount: {employee.calculate_payroll()}')
      print()

class SalaryPolicy:
  def __init__(self, monthly_salary):
    self.monthly_salary = monthly_salary

  def calculate_payroll(self):
    return self.monthly_salary

class HourlyPolicy:
  def __init__(self, total_hours_worked, hourly_rate):
    self.total_hours_worked = total_hours_worked
    self.hourly_rate = hourly_rate

  def calculate_payroll(self):
   return self.total_hours_worked * self.hourly_rate

class CommissionPolicy(SalaryPolicy):
  def __init__(self, monthly_salary, commission_amount):
    super().__init__(monthly_salary)
    self.commission_amount = commission_amount

  def calculate_payroll(self):
    fixed_salary = super().calculate_payroll()
    return fixed_salary + self.commission_amount

