'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: HOW TO reverse a string without affecting special characters
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def reverse_string(string):
    tolist = list(string)
    rightpointer = len(tolist) -1
    leftpointer = 0
    while leftpointer < rightpointer:
        if not tolist[leftpointer].isalpha():
            leftpointer +=1
        elif not tolist[rightpointer].isalpha():
            rightpointer -=1
        else:
            tolist[leftpointer], tolist[rightpointer] = tolist[rightpointer], tolist[leftpointer]
            leftpointer +=1
            rightpointer -=1
    return ''.join(tolist)
string = "l@@me!be*your@@hero%"
print(reverse_string(string))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Get Dict keys as form of List
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def getlist(dict):
    list = []
    for keys in dict.keys():
        list.append(keys)
    return(list)
dict = {1:'a', 2:'b', 3:'c'}
print(getlist(dict))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Convert a list to multiple intger into a single integer
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
List = [12, 15, 17]
for i in List:
    print(i , end="")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: How to itrate- through two list in simontensoly/ Parallaly
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import itertools
foo = [1, 2, 3]
bar = ['red', 'while', 'black']
val = [255, 256]
for (f , b, V) in zip(foo, bar, val):
    print ("\n",f,b,V)
for (f , b, V) in itertools.zip_longest(foo, bar, val):
    print ("\n",f,b,V)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: Multiple Key and multiple value are support in dictnary 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#dict = {['a','b','c']:3, ['e','f']:5}
d1 =['aa', 'bb' ]
d2 = [1,2]
my_dict = dict.fromkeys(d1,d2)
print(my_dict)
#my_dict2 = dict.update(['e','f']:20)
#print(my_dict2)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: Search a charcter from a string 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def search(char, str):
    L=len(str)
    print(L)
    i = 0
    while i < L:
        if str[i] == char:
            i = i+1
            return i
print("search char", search("p", 'pallap'))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: Print a string on one line using for loop
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#
animals = "Sting"
for animal in animals:
  print(animal, end=' '"\n")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: Print dictionary Value square of key value ex({1: 1, 2: 4, 3: 9}) with range of 8
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
number=8
numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)
# Method 2 Using Lis Comperheshion
root = {x**2:x for x in range(8, 0, -1)}
print ("Method 2 Using Lis Comperheshion", root)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 9 :: Find all the alphabet from the list
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
l_data = [8, 'a', 5, 6, 8, 0,'e','d']
new_l_data =[]
for c in l_data:
    if str(c).isalpha():
        new_l_data += c 
print(new_l_data)
### Methos-2 List Cpmprehesion method 
finalls = [x for x in l_data if isinstance(x, str) and x.isalpha()]
print(finalls)
#Method -3 Lamnda Expression
finalls = list(filter(lambda e: isinstance(e, str) and e.isalpha(), l_data))
print(finalls)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 :: Write a Python code to reverse a given list using for loop 
`'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
array = [23, 12, 5, 24, 23, 76, 86, 24, 86, 24, 75] 
reversedList = []
 
#reverse list using for loop
for i in range(len(array)) :
    reversedList.append(array[len(array) - i - 1])
#print lists
print(f'Original List : {array}')
print(f'Reversed List : {reversedList}')