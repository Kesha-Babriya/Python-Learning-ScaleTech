import os

# current working directory
print(os.getcwd())

#list files nd folder
print(os.listdir())     # give file or folder names from current dir
print(os.listdir('Stage-01'))
# print(os.listdir('01-python-basics'))

#check if path exist

print(os.path.exists("Stage-01"))       # if file or folder exist
print(os.path.isfile("02_input_and_output.py"))     # if file exist

#if dir exist
print(os.path.isdir("stage-01"))

#for create folder
# os.mkdir("test_folder")

# remove dir
# os.rmdir("test_folder")   