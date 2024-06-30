'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: FIND and COUNT THE LETTER/ "E" IN THE WORD.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

test_str = "GeeksforGeeks"
# using naive method to get count  
# counting e  
count = 0
  
for i in test_str: 
    if i == 'e': 
        count = count + 1
print (count)

### METHOD -2 USING LAMBDA FUNCTION '''

count1 = sum(map(lambda x : 1 if 'e' in x else 0, test_str)) 
print("Q1||METHOD-2", count1)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: FIND THE NOT REPEATED COUNT THE SENTENCE AND REPEATED THE SENTENCE 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
### METHOD -1  USING LOOP FUNCTION '''
text = "mango mango peach apple apple banana"
words = text.split()

for word in words:
    if text.count(word) == 1:
        print(word)
        
    else:
        pass

### METHOD -2 USING LAMBDA FUNCTION '''
d = {x:words.count(x)for x in words}
print ("Q-2||METHOD -2", d)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: COUNT THE TOTAL ODD NUMBER IN THE LIST 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
numbers = [3, 2, 5, 7, 4, 9, 6, 9, 5, 8, 3]
### METHOD -1 USING LIST COMPREHESION METHOD '''

odd_nums = [num for num in numbers if num % 2 != 0]
print("Q-3||METHOD -1, odd numbers ", odd_nums )
print(f"Q-3||METHOD -1, odd numbers , {odd_nums}")
print("Q-3||METHOD -1, Total odd numbers ", len(odd_nums) )

### METHOD -2 USING NORMAL FOR LOOP '''
odd_count = 0
for num in numbers:
    if num % 2 != 0:
        odd_count += 1
print("Q-3||METHOD -2, Total odd numbers", odd_count )

### METHOD -3 USING LAMBDA EXPRESSION '''
odd_counts = len(list(filter(lambda x: x % 2 !=0, numbers)))
print(f"Q-3||METHOD -3, Total odd numbers  {odd_count}")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: COUNT THE REPATED ELEMENT LIKE THIS (1:3 , 2:2, 3:4) 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
E_List = [1,1,1,1,2,2,2,2,3,3,4,5,5]
Rept_count = {x:E_List.count(x) for x in E_List}
print("Q-4||METHOD -1", Rept_count)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: COUNT THE  ELEMENT WHO REPATED MORE THAN 2 TIMES
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
mylist = [1,7,3,7,3,9,3,9,7,9,10,0] 
print ("Q-5||METHOD -1", sorted(set([i for i in mylist if mylist.count(i)>2])))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: COUNT THE NUMBER OF CHARACTER (CHARACTER FREQUENCY) IN A STRING
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print("Q-6||METHOD -1", char_frequency('google.com'))

# s = "asldaksldkalskdlan"
# dict = {}
# for letter in s:
#  if letter not in dict.keys():
#   dict[letter] = 1
#  else:
#   dict[letter] += 1

# print (dict)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 7 :: FIND DUPLICATE ELEMENT IN THE LIST AND COUNT THE ELEMENT. 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

list = ['1', '2', '3', '1', 'c', '3', 'c']
temp=set(list)
result={}
newlist=[]
for i in temp:
    result[i]=list.count(i)
    newlist+=i
print ("Q-7||METHOD -1", result)
print ("Q-7||METHOD -1", newlist)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 8 :: Count repeated characters in a string
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import collections
str1 = '123456789764323566543643245'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1
for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print("Q-8||METHOD -1  "'%s %d' % (c, d[c]))
      
### METHOD -2 USING NORMAL FOR LOOP '''
count = {}
for i in range(len(str1)):
	if(str1[i] in count):
		count[str1[i]] += 1
	else:
		count[str1[i]] = 1
		#increase the count of characters by 1
for it,it2 in count.items(): #iterating through the unordered map
	if (it2 > 1): #if the count of characters is greater than 1 then duplicate found
		print("Q-8||METHOD -2  ", str(it) + ", count = "+str(it2))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 9 :: Count repeated element in the list
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# n = int(input())
# print(n)
# arr = list(map(int, input().split()))
# print(arr)
arr = [23, 12, 5, 24, 23, 76, 86, 24, 86, 24, 75]
dup = []
print(dup)
for i in arr:
    if i not in dup:
        dup.append(i)
        print("Q-9||""{} occurs {} times".format(i, arr.count(i)))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 10 ::How to count that how many dot character are using in-text string.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import re
text = 'Hello ............?'
n = 0
dot = [i for i in text if re.match('\.',i) ]
print("Q-10||" "Dot Counting ", len(dot))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions11 :: return true or false if string contains more than one repeated character
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
infi1 = "Deepak"
infi2 = "Kumar"
def has_repeats(str):
  for i in range(len(str)):
    for j in range(i + 1, len(str)):
      if str[i] == str[j]:
        return True
  return False
print("Q - 11 ||", has_repeats(infi1))
print("Q - 11 ||", has_repeats(infi2))