import productivity
import employees
import payroll_policy

manager = employees.Manager(1, 'Ramesh tripathi', 80000)
developer = employees.Developer(2, 'Utkarsh Tiwari', 40000)
sales_guy = employees.SalesPerson(3,'Abhinav sinha', 40000, 10000)
cleaner_guy = employees.LabourPerson(4, 'Mahesh', 40, 200)
freelancer = employees.TemporaryDeveloper(5, 'Tanmay sharma', 40, 1000)

employees = [
  manager,
  developer,
  sales_guy,
  cleaner_guy,
  freelancer
]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)

print()
payroll_system = payroll_policy.PayrollSystem()
payroll_system.salary_calculator(employees)


