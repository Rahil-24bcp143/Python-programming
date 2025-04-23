
import pickle

class Employee:
    def __init__(self, empcode, empname, dateofjoining, salary):
        self.empcode = empcode
        self.empname = empname
        self.dateofjoining = dateofjoining
        self.salary = salary

    def __repr__(self):
        return f"{self.empcode}, {self.empname}, {self.dateofjoining}, {self.salary}"

emp = Employee(101, 'Rahil','12/4/2025', 50000)

with open('employee.dat', 'wb') as f:
    pickle.dump(emp, f)

with open('employee.dat', 'rb') as f:
    emp_loaded = pickle.load(f)

print(emp_loaded)
