# Impllement the contact management system .

#  create a program that store and manage contacts in a file nae contacts.txt 
# Each contact entry should be name number and email 
# implement this featurs 
        # Add the new contact ( append the contact to the file )
        # View all contact ( read and display all contact of the file)
        # Exit the program 

# with open('contacts.txt','w') as contacts:
    # contacts.write("Amodh, 078917393, amxdh@gmail.com")

def add_contact (value):
    with open('contacts.txt','a') as contacts:
        contacts.writelines("\n"+value)

def view_contact():
    with open('contacts.txt','r') as contacts:
        content = contacts.readlines()
        for i in range(len(content)):
            each_value = content[i]
            values = each_value.split(",")
            print("Name :  "+ values[0])
            print("Contact Number :  "+ values[1])
            print("Email :  "+ values[2])
    call_functions()




def get_values_to_add():
    name = input("1 . Enter a Name:  ")
    contact = input("1 . Enter a Contact:  ")
    email = input("1 . Enter a Email :  ")
    add_contact(name+", "+contact+", "+email)
    print("\n")
    call_functions()

def call_functions():
    print("1 . Enter (1) for add contact ")
    print("2 . Enter (2) for View contact ")
    print("3 . Enter (3) for Exit ")
    value = input("Enter a number :")
    print("\n")
    if value == "1" : 
        get_values_to_add()
    elif value == "2" :
        view_contact()
    elif value == "3" :
        return
    else:
        call_functions()

call_functions()