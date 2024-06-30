# a = "Deepak"
# print(a)




# from pathlib import Path

# fpath = Path('Download/deep.txt').absolute()

# print(fpath)



# #which one largest number.

# n1 = 4
# n2 = 7
# n3 = 6
# print(max(n1,n2,n3))

# #how to get range argument from list?

lst = [1,9]
for i in range (*lst):
  print(i)




# #How to Convert decimal to binary?

#inp = int(input())
#print('{:x}' .format(inp))


# #**kwargs manuplation 

# my_dict = {'Name' : 'Deepak', 'city' : 'Chennai'}

# def fn(**kwargs):
#   for i in kwargs:
#     print('key:',i)
#     print('value:' ,kwargs[i])
# fn(**my_dict)
# #print(fn(**my_dict))


# #Generate password using String module

from string import printable
import re
import string 
fc = re.sub(r'\t\n\r\x0b\x0c','', string.printable)
print(fc)


class human:
    name=None
    age=None
    def get_name(self):
        n1=self.name=input()
        print("Name Entered", n1)
    def get_age(self):
        a1=self.age=input()
        print("Name Entered", a1)
    def put_name(self):
        print("your name is", self.name)
    def put_age(self):
        print("your age is", self.age)
person1=human()
person1.get_name()
person1.get_age()
person1.put_name(), person1.put_age()

class Std:
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
    def print_std(self):
        print("name", self.name)
        print("age", self.age)
        print("branch", self.branch)
std1 = Std("Dee",34,"CSE")
std1.print_std()

class fruit:
    def __init__(self):
        print("I fruit")
class citrus(fruit):
    def __init__(self):
        super().__init__()
        print("I Citrus")
lemon = citrus()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
list1 = [10, 20, 4, 45, 99]

# printing the last element
print("Largest element is:", list1[-2:][::-1])

#$$$$$$$$$$$$$$$$$$$$$$

x = lambda a : a +10
print (x(5))

x = lambda a,b : a * b
print (x(6,5))


my_list = [2, 23, 4, 6, 11, 45]

new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

my_list = [1, 5, 4, 7, 8, 11, 3]

new_list= list(map(lambda x: x*2 , my_list))
print(new_list)

# samsung = {1:{2:[6]}}
# samsung.values(1[1])
# print(samsung)



#Find Equilibrium index of an array. Equilibrium index of an array is an index such that the sum of elements 
# at lower indexes is equal to the sum of elements at higher indexes.
#Ex: Input: arr[] = {-7, 1, 5, 2, -4, 3, 0}

      #Output: 3

      #3 is an equilibrium index, because: arr[0] + arr[1] + arr[2] = arr[4] + arr[5] + arr[6]
	  

# Python program to find equilibrium 
# index of an array

# function to find the equilibrium index
def equilibrium(arr):
    leftsum = 0
    rightsum = 0
    n = len(arr)

    # Check for indexes one by one 
    # until an equilibrium index is found
    for i in range(n):
        leftsum = 0
        rightsum = 0
    
        # get left sum
        for j in range(i):
            leftsum += arr[j]
        
        # get right sum
        for j in range(i + 1, n):
            rightsum += arr[j]
        
        # if leftsum and rightsum are same,
        # then we are done
        if leftsum == rightsum:
            return i
    
    # return -1 if no equilibrium index is found
    return -1
            
# driver code
arr = [-7, 1, 5, 2, -4, 3, 0]
print (equilibrium(arr))

#Find the maximum no. of consecutive one’s in a binary array
#Ex:  Input :   arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1}

# Python 3 program to count
# maximum consecutive 1's
# in a binary array.

# Returns count of maximum
# consecutive 1's in binary
# array arr[0..n-1]
def getMaxLength(arr, n):

	# initialize count
	count = 0
	
	# initialize max
	result = 0

	for i in range(0, n):
	
		# Reset count when 0 is found
		if (arr[i] == 0):
			count = 0

		# If 1 is found, increment count
		# and update result if count
		# becomes more.
		else:
			
			# increase count
			count+= 1
			result = max(result, count)
		
	return result

# Driver code
arr = [1, 1, 0, 0, 1, 0, 1,
			0, 1, 1, 1, 1, 1]
n = len(arr)

print(getMaxLength(arr, n))

# This code is contributed by Smitha Dinesh Semwal