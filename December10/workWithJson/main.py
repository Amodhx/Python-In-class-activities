import json

# json_file_path = "example_1.json"
# # Convert json data values to dict
# with open(json_file_path,'r') as json_file:
#     data = json.load(json_file)
#     print(data)
#     print(type(data))


# dict_1 = {
#     "name" : "aaaa",
#     "age": 19
# }

# with open('json_file_path.json','a') as json_file:
#     json_file.write(json.dumps(dict_1,indent=4))

# with open('json_file_path.json','r') as json_file:
#     data = json.loads(json_file.read())
#     print(data)



# Exercise 03
# You are give the json file name student.json which contain information about student and their grades 
# You task is to
    # Read the json file 
    # Display the name of all student who scored above 75
    # add the new student record to the file 
    # Save the updated data back to the json file 

students = []
def read_json_file():
    with open('students.json','r') as students_json:
        data = json.loads(students_json.read())
        for i in range(len(data)):
            students.append(data[i])


def check_score():
    for i in range(len(students)):
        if students[i]["score"] > 75 : 
            print(students[i]["name"])

def add_new_student():
    students.append({
        "name" : "Eranga",
        "score" : 86
    })
def save_data():
    with open('students.json','w') as student_json:
        json.dump(students,student_json,indent=4)
            



read_json_file()
check_score()
add_new_student()
save_data()