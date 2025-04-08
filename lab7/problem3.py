employees = {
    'dept_no': [10, 20, 10, 30, 20, 10],
    'emp_roll_no': [101, 102, 103, 104, 105, 106],
    'salary': [50000, 60000, 45000, 80000, 75000, 55000]
}

dept_salaries = {}
for dept, sal in zip(employees['dept_no'], employees['salary']):
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(sal)
for dept, salaries in dept_salaries.items():
    print(f"Department {dept}: Min Salary = {min(salaries)}, Max Salary = {max(salaries)}")