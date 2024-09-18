# write a programme to calculate the gross salary of an employee
basic_salary = float(input("Enter Basic Salary: "))
if basic_salary < 1500:
    da = basic_salary * 0.9
    hra = basic_salary * 0.1
else:
    da = basic_salary * 0.98
    hra = 500
gross_salary = basic_salary + da + hra
print("Basic Salary: ", basic_salary)
print("DA: ", da)
print("HRA: ", hra)
print("Gross Salary: ", gross_salary)

