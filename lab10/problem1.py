import csv

data = [
    ['Roll No', 'Name', 'English', 'Maths', 'PC'],
    [1, 'Rahil', 85, 90, 88],
    [2, 'Het', 78, 82, 89],
    [3, 'Aaryan', 92, 88, 91]
]

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
