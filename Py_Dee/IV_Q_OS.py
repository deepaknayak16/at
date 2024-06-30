'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Print IP ADDRESS DETAILS IN WINDOWS
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
print(os.system('ipconfig'))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Print IP ADDRESS AND HOST-NAME IN WINDOWS
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
 
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Write A Program To IP is pingable or not
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import string
hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

# #and then check the response...
# if response == 0:
#   print (hostname, 'is up!')
# else:
#   print (hostname, 'is down!')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import sys, os

print('sys.argv[0] =', sys.argv[0])             
pathname = os.path.dirname(sys.argv[0])        
print('path =', pathname)
print('full path =', os.path.abspath("Download/deep.txt")) 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
print(os.system("ls"))

import sys
print(sys.version)
print(sys.version_info)

import os
env_var = os.environ

with open("we.txt", "w") as fl:
    for k, v in env_var.items():
        fl.write(f"{k}:{v}\n")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: Write A Program Rename a file in python
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#  os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
import os
old_name = "we.txt"
new_name = "wee.txt"

# Renaming the file
#os.rename(old_name, new_name)

if os.path.isfile(new_name):
    print("The file already exists")
else:
    # Rename the file
    os.rename(old_name, new_name)

#  os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: Write A Program Remove/Delete a file in python
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os

# removing a file with relative path
#os.remove("we.txt")
# remove file with absolute path
#os.remove(r'C:\Users\159625\Documents\Py_Dee\wee.txt')

file_path = r'C:\Users\159625\Documents\Py_Dee\wee.txt'
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("The system cannot find the file specified")


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: Copy and move a File in Python
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import shutil

src_path = r"E:\demos\files\report\profit.txt"
dst_path = r"E:\demos\files\account\profit.txt"
shutil.copy(src_path, dst_path)
print('Copied')

shutil.move(src_path, dst_path)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: Copy All Files From A Directory
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import shutil

source_folder = r"E:\demos\files\reports\\"
destination_folder = r"E:\demos\files\account\\"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''




'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
