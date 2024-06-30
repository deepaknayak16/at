# name = "clement"
# #name = input('please enter you name\n')
# if name == "clement":
#     print('No')
    
# else:
#     print(f"Hello,{name}")
    
# def reverse(s): 
#   str = "DSER" 
#   for i in s: 
#     str = i + str
#   return str


#a = lambda x,y : x+y
#print(a(5, 6))
# import calendar
# year = int(input("Enter Year: "))
# print(calendar.calendar(year, 1, 2, 5, 4))
from logging import exception


def validate_input(value):
    try:
        value = float(value)
        return value
    except exception as e:
        print(e)
        
fahranite = 3 #input("Farhanite value: ")
fahranite = validate_input(fahranite)

if fahranite:
    celsius = (fahranite - 32) *5/9
    print(f"Celcious value of {fahranite} Faharanite is celsius {celsius:2f}.")
else:
    print("Enter Valid input")
    
#Python Qui 
# A See you soon, Till then Keep Improving!!! 
#Python Quick Codes: Two Methods to Reverse a Given sequence.'" 
sentence = "ows" #input("Enter words: ") 
# I Method-1: Using Reversed it returns a reverse itarator over the value of the given sequence. 
reverse_sentence = "".join(reversed(sentence)) 
print( reverse_sentence) 
#Method-2: Using slicing
reverse_sentence = sentence[::-1] 
print( reverse_sentence) 

#Python Code Basics: Filter positive numbers from a list  
# Suppose you are getting a list of positive and negative numbers. 
# We can use : numbers = [-10, 4, 6, 8, -12] also for sample # But here we use, 
# random module to generate a list of # 10 random numbers between -8 to 8 
import random 
numbers = [random.randint(-8, 8) for i in range(10)] 
print(f"Numbers: {numbers}") 
# List comprehension to filter positive numbers only 
positive_numbers = [n for n in numbers if n > 0] 
print(f"Posttive numbers: {positive_numbers}") 

#Why in nested list a and b print out the same result, whereas in simple list the output is different???"' 
import copy 
# nested list # If we print the ids of all the lists involved, 
a = [7, 8, ['kkk', 77777]] # id(a) = 2426335414656 
b = copy.copy(a) # id(b) = 2426335442752 
# Clearly id(a) != id(b), But 
b[2].append(888) # id(b[2]) = 2426336524480 
print(id(a)) # id(a[2]) = 2426336524480 
# Here id(b[2]) == id(a[2]) 
# It means, Python does not have '2-dimensional arrays', # it just has lists, which can contain other lists. 
# Here we define 'a' with: a = [7, 8, ['kkk', 77777]]. # Then we create a copy of a. b = copy.copy(a) 
# # So, a and b are different lists, but they contains the same # 'sub-lists' ['kkk', 77777]. 
# Therefore changing b, for example, # b.append(888) will the 'sub-list' of a, as both are referencing # to the same item. 
# Therefore, we can use deepcopy here. 
#Why in nested list a and b print out the same result, whereas in simple list the output is different???"' 
import copy 
#nested list 
a = [7, 8, ['kkk', 77777]] 
b = copy.copy(a) 
b[2].append(888) 
print("a is:", a) # Output: a is: [7, 8, ['kkk', 77777, 888]]
print("b is:", b) # Output: b is: [7, 8, ['kkk', 77777, 888]]
# Both are same, But 
# Simple list 
x = [1, 2] 
y = copy.copy(x) 
y.append(9) 
print("x is:", x) # Output: x is: [1, 2]
print("y is:", y) # Output: y is: [1, 2, 9] 


#The famous FizzBuzz Problem With 3 different Methods.,
'''What is fizzbuzz Problem??
For a number 'n', display the string representations of all the numbers from 1 to n, where: - If the number is divisible by 3, the
output is 'Fizz'. If the number is divisible by 5, the output is 'Buzz'. - If the number is divisible by both 3 and 5, the output is 
'FizzBuzz'. - And display the number if the number cannot be divided by 3 or 5. '''
# • Method-1: Using normal function 
def fizzbuzz(n): 
    for number in range(1, 9): 
        if (number % 3 == 0) and (number % 5 == 0): 
            print("FizzBuzz", end='') 
        elif (number % 3 == 0): 
            print("Fizz", end='') 
        elif (number % 5 == 0): 
            print("Buzz", end='') 
        else: 
            print(number, end='') 
print(fizzbuzz(101)) 
# ■ Using Lambda Function 
print(list(map(lambda i: 'Fizz'*(not i % 3)+'Buzz' * (not i % 5) or i, range(1, 9))), sep='') 
# Using List-Comprehension 
print(['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 9)]) 


# import getpass
# database = {"dee": "45", "pyth": "245"}
# username = input("Enter username: ")
# password = getpass.getpass("Enter Your Password : ")
# for i in database.keys():
#     if username == i :
#         while password != database.get(i):
#             password = getpass.getpass("Enter Password Again! :")
#         break
# print("Verified")

#Why the diffrent variable storing equal values have same memory allocation 
a = 10
b = 8+2
c = 12-2
d = 5*2

print(id(a) == id(b) == id(c) == id(d))
print(a == b == c == d)
print(a is b is c is d)
print(id(a), id(b), id(c), id(d))

for i in range(1, 6):
    print("*" * i)

pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
for p in pat:
   pass
   if (p == 0):
       current = p
       break
   elif (p % 2 == 0):
       continue
   print(p)    # output => 1 3 1 3 1
print(current)    # output => 0


a = set([1,1,2,3])
print(a)