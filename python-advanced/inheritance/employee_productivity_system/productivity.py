class ProductivitySystem:
  def track(self, employees, hours):
   print('Tracking all category employees productivity:')
   print('---------------------------------------------')
   for employee in employees:
     result = employee.work(hours)
     print(f'Employee {employee.name}: {result}')
     print()
    

class ManagerRole:
  def work(self, hours):
    return f'Manages multiple projects for {hours} hours per week.'

class DeveloperRole:
 def work(self, hours):
    return f'Develops code for a project {hours} hours per week.'

class LabourRole:
  def work(self, hours):
    return f'Provides cleaning support to office for {hours} hours per week.'

class SalesRole:
  def work(self, hours):
    return f'Spends {hours} hours for preparing sales reports per week.'

