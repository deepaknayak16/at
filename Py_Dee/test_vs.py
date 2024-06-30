 

# from math import log10
# def rev(num):
#     def rec(num, tens):
#         if num < 10:
#             return num        
#         else:
#             return num % 10 * tens + rec(num // 10, tens // 10)
#     return rec(num, 10 ** int(log10(num)))
# print(rev(9901))





# ## Find Alphabet from a List 
# import string
# list = ['h', 'e', 'l', '5', 'o']
# newlist = []
# newdigit = []
# d={"letter":0 , "digit":0}
# for c in list:
#     if c.isalpha():
#         newlist+=c
#         d["letter"]+=1
#     elif c.isdigit():
#         newdigit+=c
#         d["digit"]+=1
#     else:
#         pass
# print ("letter", d["letter"])
# print ("digit", d["digit"])
# print (newlist)
# print (newdigit)





# d={}
# d['deepak'] = 0
# d['nayak'] = 0 
# f = [ '1, deepak, 15',
# '2, nayak, 10',
#  '3, deepak, 10',
#  '4, nayak, 13',
#  '3, deepak, 11',
#  '4, nayak, 15',
#  '3, deepak, 12',
#  '4, nayak, 14']
# for lines in f:
#     print(lines)
#     ##appropriate logic to excute#
#     line = lines.split(', ')
#     d[line[1]] += int(line[-1])
# print(d)






# # object destoryer 
# class Test:
#     def __del__(self):
#         print ("deleted")
#         test = Test()
#         del test



# #Find the second most repeated word in a given string
# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     counts_x = sorted(counts.items(), key=lambda kv: kv[1])
#     print(counts_x)
#     return counts_x[-1]
 
# print(word_count("deepy dipu deepy deepy "))

# #Find the first repeated word in a given string
# def first_repeated_word(str1):
#   temp = set()
#   for word in str1.split():
#     if word in temp:
#       return word
#     else:
#       temp.add(word)
#   return 'None'
# print(first_repeated_word("ab ca bc ab "))
# print(first_repeated_word("ab ca bc ab ca ab bc"))
# print(first_repeated_word("ab ca bc ca ab bc"))
# print(first_repeated_word("ab ca bc"))



# def no_of_substring_with_equalEnds(str1): 
# 	result = 0; 
# 	n = len(str1); 
# 	for i in range(n): 
# 		for j in range(i, n): 
# 			if (str1[i] == str1[j]): 
# 				result = result + 1
# 	return result 
# str1 = input("Input a string: ")
# print(no_of_substring_with_equalEnds(str1))



# def reverse_string_words(text):
#     for line in text.split('\n'):
#         return(' '.join(line.split()[::-1]))
# print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
# print(reverse_string_words("Python Exercises."))
## Reverse a String using Recursion
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))



# x = 22
# print("\nOriginal Number: ", x)
# print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
# print("Right aligned (width 10)  :"+"{:10d}".format(x));
# print("Center aligned (width 10) :"+"{:^10d}".format(x));
# print()


# with open("C:/Users/DIPPU/Documents/test.txt") as f:
#     with open("C:/Users/DIPPU/Documents/out.txt", "w") as f1:
#         for line in f:
#             f1.write(line)



# with open('C:/Users/DIPPU/Documents/test.txt') as fh1, open('C:/Users/DIPPU/Documents/out.txt') as fh2:
#     for line1, line2 in zip(fh1, fh2):
#         # line1 from abc.txt, line2 from test.txtg
#         print(line1)
#         print(line2)
#         print(line1+line2)


# def file_lengthy(fname):
#     with open(fname) as fh1:
#         for i, l in enumerate(fh1):
#             pass
#         return i + 1
# print("Number of lines in the file: ",file_lengthy("C:/Users/DIPPU/Documents/test.txt"))



# def longest_word(filename):
#     with open(filename, 'r') as infile:
#               words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]

# print(longest_word('C:/Users/DIPPU/Documents/test.txt'))



# #match ip adress in python 

# import re
# input_ip = '192.123.8.256'
# flag=0
# match = re.match("^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$", input_ip)
# if match:
#     field = input_ip.split(".")
#     for i in range(0, len(field)):
#         if (int(field[i]) >= 0 and int(field[i]) <= 255):
#             flag += 1
#         else:
#             flag = 0
# if flag == 4:
#     print ("Acceptable ip address")
# else:
#     print ("Unacceptable ip address")

# my_dict = dict.fromkeys(['a', 'b', 'c'], 10)
# my_dict.update(dict.fromkeys(['d', 'e'], 20))
# print (my_dict)
# #my_dict = {('a', 'c', 'd'): 10, ('b', 'e'): 20}
# next(v for k, v in my_dict.items() if 'b' in k)

# #How to print 'neduitn' using a single line of code from Days ?
days = "Mon Tue Wed Thu Fri Sat Sun"
re = days.split()
temp = ""
for day in re:
    temp = temp + (day[-1])
print (temp)
print (len(days))
import re
print(''.join(re.findall("(?i)[a-z](?!\\S)", days)))

# 1.	Write a program to find the length of the string "refrigerator" without using len function.
lene = sum(map(lambda x:1, "refrigerator"))
print(lene)

#2.	Write a program to find the first and the last occurrence of the letter 'o' and character ',' in "Hello, World".

def findLastIndex(str, x): 
    index = -1
    for i in range(0, len(str)): 
        if str[i] == x: 
            index = i 
    return index 
  # String in which char is to be found 
str = "geeksforgeeks"
# char whose index is to be found 
x = 'e' 
index = findLastIndex(str, x) 
if index == -1: 
    print("Character not found") 
else: 
    print('Last index is', index)

#Write a program to print every character of a string entered by user in a new line using loop.
a = 'googleindia'
for i in a:
  print (i)

#Write a program to check if the letter 'e' is present in the word 'Umbrella'.
print ('e' in 'Umbrella')

a = "This is orange juice"
print('orange' in a.split())
#the output should be R.B.Roser.
a = "Robert Brett Roser"
a = a.split()
b = a[0][0]+". "+a[1][0]+". "+a[2]
print (b)