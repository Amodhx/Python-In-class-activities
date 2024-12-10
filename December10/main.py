import os
file_path = os.getcwd() + "\\Second day\\December10" 
# file_1 = open (file_path,'r') #'r' - read 
# 'w' - write ( when we writing if file is not exists its auto create it  )


# print(file_1.read())

# file_2 = open(file_path+"\\main_file.txt",'a')
# print(file_2.read())
# file_1.close() # we have to close file end of the operation 


# # Second way 
# # This is the best practice for file handling 
# with open(file_path,'r') as file:
#     content = file.read()
#     print(content)# when we using this way the opend file is auto close when after operation .


with open("my_file1.txt",'w') as my_file:
    my_file.write("Hello world \nMy man \n")
    my_file.write("Hey man \n")

with open("my_file1.txt",'a') as my_file:
    my_file.write("Hey hey hey you")

with open("my_file1.txt",'r') as my_file:
    print(my_file.read())