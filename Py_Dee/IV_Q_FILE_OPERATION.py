'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Find Palindrome from a file
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
with open(r'C:\Users\159625\Documents\Py_Dee\ex.txt') as text:
    data = text.readlines()
    for line in data:
        line = line.strip()
        line2 = line[::-1]
        if line == line2:
            print ('Palindrome!')
        else:
            print ('Not Palindrome!')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Finds all errors and warnings in a file.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import sys 
import os 
def find_error_warning(filename):
    filename = r'C:\Users\159625\Documents\Py_Dee\ex.txt'
    error_and_warning =[]
    with open(filename, "r") as fp:
        data = fp.readlines()
        i=0
        j=0
        for line in data:
            line = line.strip()
            if line.startswith("Error:"):
                i = i +1
                error_and_warning.append((i, line, "error"))
            elif line.startswith("WARNING:"):
                j=j+1
                error_and_warning.append((j, line, "warning"))
    return(error_and_warning)
print("Q2 | OUTPUT find_error_warning ", find_error_warning(filename=''))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Diffence Between write(), writelines(), read(), readline(), readlines()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#The write() method:
#This function inserts the string into the text file on a single line.
#the below line of code will insert the string into the created text file, 
filename = r'C:\Users\159625\Documents\Py_Dee\read.txt'
fp = open(filename, "w")
fp.write("Hello There \n")
fp.close()

#The writelines() method:
#This function inserts multiple strings at the same time. A list of string elements is created, and each string is then added to the text file.
filename = r'C:\Users\159625\Documents\Py_Dee\read.txt'
L = ["This is Lagos \n","This is Python \n","This is Fcc \n"]
fp = open(filename, "w")
fp.writelines(L)
fp.close()
## The read() method:
#This function returns the bytes read as a string. If no n is specified, it then reads the entire file.
filename = r'C:\Users\159625\Documents\Py_Dee\read.txt'
f = open(filename, "r")
print("Only read", f.read())
## The readline() method:
# This function reads a line from a file and returns it as a string. It reads at most n bytes for the specified n.
# But even if n is greater than the length of the line, it does not read more than one line.
filename = r'C:\Users\159625\Documents\Py_Dee\read.txt'
fp = open(filename, "r")
print("Readline", fp.readline(2))
#The readlines() method:
#This function reads all of the lines and returns them as string elements in a list, one for each line.
filename = r'C:\Users\159625\Documents\Py_Dee\read.txt'
fp1 = open(filename, "r")
print("Last read lines", fp1.readlines())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: how to copy or write coontet of of file1 to file2
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
file1 = r'C:\Users\159625\Documents\Py_Dee\read.txt'
file2 = r'C:\Users\159625\Documents\Py_Dee\ex.txt'
with open(file1, 'r', encoding='utf-8') as infile, open(file2, 'w') as outfile:
    # read sample.txt an and write its content into sample2.txt
    for line in infile:
        outfile.write(line)

# Opening the file to read the contents
f = open(file2, "r")
print(f.read())
f.close()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: Differnece between seek() method and tell()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# The seek() function sets the position of a file pointer and the tell() function returns the current position of a file pointer.
'''
f.seek(0)	    Move file pointer to the beginning of a File
f.seek(5)	    Move file pointer five characters ahead from the beginning of a file.
f.seek(0, 2)	Move file pointer to the end of a File
f.seek(5, 1)	Move file pointer five characters ahead from the current position.
f.seek(-5, 1)	Move file pointer five characters behind from the current position.
f.seek(-5, 2)	Move file pointer in the reverse direction. Move it to the 5th character from the end of the file 
'''

with open(r'C:\Users\159625\Documents\Py_Dee\ex.txt', "r") as fp:
    # Moving the file handle to 6th character 
    fp.seek(6)
    # read file
    print(fp.read())

with open(r'C:\Users\159625\Documents\Py_Dee\ex.txt', "w+") as fsw:
    fsw.write('My First Line\n')
    fsw.write('My Second Line')
    # move pointer to the beginning
    fsw.seek(0)
    # read file
    print(fsw.read())
with open(r'C:\Users\159625\Documents\Py_Dee\ex.txt', "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2)
    # Inserting new content to the end of the file
    fp.write("\nThis content is added to the end the file")
    # moving to the beginning 
    # again read the whole file
    fp.seek(0)
    print(fp.read())
############################# tell() tel() method ############################
with open(r'C:\Users\159625\Documents\Py_Dee\ex.txt', "r+") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2)

    # getting the file handle position
    print('file handle at:', fp.tell())

    # writing new content
    fp.write("\nDemonstrating tell")

    # getting the file handle position
    print('file handle at:', fp.tell())

    # move to the beginning
    fp.seek(0)
    # getting the file handle position
    print('file handle at:', fp.tell())

    # read entire file
    print('***Printing File Content***')
    print(fp.read())
    print('***Done***')

    # getting the file handle position
    print('file handle at:', fp.tell())

