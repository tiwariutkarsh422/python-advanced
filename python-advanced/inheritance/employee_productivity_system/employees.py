from payroll_policy import (
  SalaryPolicy,
  HourlyPolicy,
  CommissionPolicy
)

from productivity import(
  ManagerRole,
  LabourRole,
  DeveloperRole,
  SalesRole
)

class Employee:
  # A parent class or an abstract class used to define a generic employee.
  # An abstract class is the class used for inheriting the attributes but not instantiating it.
  def __init__(self, id, name):
    self.name = name
    self.id = id

class Manager(Employee, ManagerRole, SalaryPolicy):
  def __init__(self, id, name, monthly_salary):
    SalaryPolicy.__init__(self, monthly_salary)
    super().__init__(id, name)

class Developer(Employee, DeveloperRole, SalaryPolicy):
  def __init__(self, id, name, monthly_salary):
    SalaryPolicy.__init__(self, monthly_salary)
    super().__init__(id, name)

class SalesPerson(Employee, SalesRole, CommissionPolicy):
  def __init__(self, id, name, monthly_salary, commission_amount):
    CommissionPolicy.__init__(self, monthly_salary, commission_amount)
    super().__init__(id, name)

class LabourPerson(Employee, LabourRole, HourlyPolicy):
  def __init__(self, id, name, total_hours_worked, hourly_rate):
    HourlyPolicy.__init__(self, total_hours_worked, hourly_rate)
    super().__init__(id, name)

class TemporaryDeveloper(Employee, DeveloperRole, HourlyPolicy):
  def __init__(self, id, name, total_hours_worked, hourly_rate):
    HourlyPolicy.__init__(self, total_hours_worked, hourly_rate)
    super().__init__(id, name)
  

