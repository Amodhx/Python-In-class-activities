# import os
# file_path = os.getcwd() + "\\Second day\\December10" 
# file_1 = open (file_path,'r') #'r' - read 
# # 'w' - write ( when we writing if file is not exists its auto create it  )


# print(file_1.read())

# file_2 = open(file_path+"\\main_file.txt",'a')
# print(file_2.read())
# file_1.close() # we have to close file end of the operation 


# # Second way 
# # This is the best practice for file handling 
# with open(file_path,'r') as file:
#     content = file.read()
#     print(content)# when we using this way the opend file is auto close when after operation .



# # Exercise 01 
# with open("my_file1.txt",'w') as my_file:
#     my_file.write("Hello world \nMy man \n")
#     my_file.write("Hey man \n")
#     value = ["Amodh \n","amodh \n","amodh \n"]
#     my_file.writelines(value)

# with open("my_file1.txt",'a') as my_file:
#     value = ["Amodh \n","amodh \n","amodh"]
#     my_file.writelines(value)

# with open("my_file1.txt",'r') as my_file:
#     print(my_file.read())





# JSON is a langauge independentant obk
# Java script Object notation

