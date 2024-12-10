# import csv
# csv_file_path = "Second day\December10\CSV\customers-100.csv"

# with open(csv_file_path,'r',newline='') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     #  when we using DictReader we can get values with dict 
#     for row in csv_reader:
#         print(row)




# You are task with the python program to manage the companies stored in csv file the program should read the employee details from the csv file 
# Filter the records based on the condition and write the filters record

# Input file ( Employee.csv)
# Contain the following field 
        # Employee_id
        # Name
        # Department
        # Salary

# You should create the file it should contain record of employee who salaries are above 57000 
# The field should be same 
        # Task 01 
            # Read the input file use csv.reader to read employee.csv and display all the records on the console 
            # filter the records identifiy employees with the salary > 57000
            # writer the filter records use csv.DictWriter to write the filter records to new file name High-Salary-employee.csv


import csv

employee_file_path = "Second day\December10\CSV\Employee.csv"
filterd_employee_file_path = "Second day\December10\CSV\Filterd_Employee.csv"

all_employees = []
filterd_employees = []
filed_names = []
with open(
    employee_file_path,'r',newline="") as employee_csv_file:
    employee_csv_reader = csv.reader(employee_csv_file)

    for row in employee_csv_reader:
        print(row)
        all_employees.append(
            {
                "EmployeeId" : row[0],
                "Name" : row[1],
                "Department" : row[2],
                "Salary": row[3]
            }
        )
    filed_names = all_employees.pop(0)

print("All Employees \n")
print(all_employees)

for employee in all_employees:
    if int(employee["Salary"]) > 57000:
        filterd_employees.append(employee)

print("\n\nFilterd Employees \n")
print(filterd_employees)


with open(filterd_employee_file_path,'w',newline='') as filterd_employee_file:
    csv_writer = csv.DictWriter(filterd_employee_file, fieldnames= filed_names)
    csv_writer.writeheader()
    for row in filterd_employees:
        csv_writer.writerow(row)
