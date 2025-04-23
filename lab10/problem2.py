import csv

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    result = {}
    for row in reader:
        rollno = row['Roll No']
        total = int(row['English']) + int(row['Maths']) + int(row['PC'])
        result[rollno] = {
            'name': row['Name'],
            'marks': [int(row['English']), int(row['Maths']), int(row['PC'])],
            'total': total
        }

print(result)
