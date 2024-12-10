# We use CSV files to store structured data 
# CSV  - comma separated values 

import csv
# we have to import csv libryry first 

csv_file_path = "Second day\December10\CSV\customers-100.csv"

with open(csv_file_path,'r',newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    for  row in csv_reader:
        print(row)

data = [
    {"Name":"John Doe","Age":34,"City":"London"},
    {"Name":"John Wick","Age":38,"City":"California"},
    {"Name":"Jack reacher","Age":26,"City":"Miami"},
]

field_names = ["Name","Age","City"]

# Open CSV file
with open(csv_file_path,'w',newline='') as csv_file:
    
    # Create a CSV writer object
    csv_writer = csv.DictWriter(csv_file,fieldnames=field_names)

    # Write the header (column names) to the CSV file
    csv_writer.writeheader()
    
    #Write the data rows to the CSV file
    for row in data:
        csv_writer.writerow(row)
