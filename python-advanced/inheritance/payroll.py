class PayrollSystem:
  ''' This method takes a list of employees and calculates there salaries using caluclate_salary()
      method.'''
  def salary_calculator(self, employees):
    print('Salary of every category employee')
    print('----------------------------------')
    print()
    for employee in employees:
      print(f'Payroll for Employee id: {employee.id} , Employee name: {employee.name}')
      print(f'Total amount: {employee.calculate_salary()}')
      print()

class Employee:
  # A parent class or an abstract class used to define a generic employee.
  # An abstract class is the class used for inheriting the attributes but not instantiating it.
  def __init__(self, id, name):
    self.name = name
    self.id = id

class SalaryEmployee(Employee):
  # A child class which inherits name and id attributes from base class Employee.
  def __init__(self, id, name, monthly_salary):
    super().__init__(id, name) # super() method used to access base class attributes
    self.monthly_salary = monthly_salary

  def calculate_salary(self):
    # calculates the monthly salary
    return self.monthly_salary

class HourlyEmployee(Employee):
  # Child class for special hourly employee category inherited from base class Employee
  def __init__(self, id, name, total_hours_worked, hourly_rate):
    super().__init__(id, name)
    self.total_hours_worked = total_hours_worked
    self.hourly_rate = hourly_rate

  def calculate_salary(self):
   return self.total_hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
  ''' Special commision employee category inherited from class SalaryEmployee which inturn
      inherits from class Employee''' 
  def __init__(self, id, name, monthly_salary, commission_amount):
    super().__init__(id, name, monthly_salary)
    self.commission_amount = commission_amount

  def calulate_salary(self):
    ''' NOTE: We can use the monthly_salary which has been accessed from its parent class
        SalaryEmployee to get monthly salary but by doing so, any change in calculating salary
        would result in changing it twice in SalaryEmployee and ComissionEmployee'''
    fixed_salary = super().calculate_salary()
    return fixed_salary + self.commission_amount


  
