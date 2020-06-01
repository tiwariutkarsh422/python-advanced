import payroll

salary_employee = payroll.SalaryEmployee(1, 'Utkarsh Tiwari', 15000)

hourly_employee = payroll.HourlyEmployee(2, 'Tanmay Dixit', 50, 1000)

commission_employee = payroll.CommissionEmployee(3, 'Zaid Ghori',12000, 5000)

payroll_system = payroll.PayrollSystem()

payroll_system.salary_calculator([
  salary_employee,
  hourly_employee,
  commission_employee,
])
