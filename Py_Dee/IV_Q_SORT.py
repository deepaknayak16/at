## Sort the list 
L1 = ["9", "1", "5", "2", "0", "3"]
L1.sort()
print("Ouve", L1)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Sorting a list/array odd numbers first, then even numbers in Python
L = [5,6,4,7,11,14,12,1,3]

l_even = sorted(L, key = lambda x:(x%2, x))
print(l_even)

## odd numbers followed by even numbers , each in ascending order
l_o_e_a = sorted(L, key = lambda x:(not x%2, x))
print(l_o_e_a)

## even numbers followed by odd numbers , each in descending order
l_e_o_d = sorted(L, key = lambda x:(not x%2, x), reverse=True)
print(l_e_o_d)
## odd numbers followed by even numbers , each in descending order
l_o_e_d = sorted(L, key = lambda x:(x%2, x), reverse=True)
print(l_o_e_d)

###### OTHRT WAY TO SOLVE ############################################ 
L2 = [34, 45, 67, 84, 55, 24]
def sort_list(my_list):
  even_list = []
  print (even_list)
  odd_list = []
  print (odd_list)
  for i in my_list:
      if i % 2 == 0:
          even_list.append(i)
      else:
          odd_list.append(i)
  even_list.sort(),odd_list.sort()

  even_list.extend(odd_list)
  return even_list
    

print(sort_list(L2))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#How to sort mixed data type.

str_num =[5, "1", 100, 2.3,"34"]
s1 = [i for i in str_num if isinstance(i,int) or isinstance(i,float)]
s2 =[j for j in str_num if isinstance(j,str)]
str_num = sorted(s1) + sorted(s2)
print (str_num)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

## Sort the list without using any inbuilt method 
my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print( "Sort the list without using any inbuilt method" , new_list)
##### OTHER WAY Around ############
my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
for i in range(len(my_list) - 1):
  for j in range(i + 1, len(my_list)):
    if my_list[i] > my_list[j]:
      my_list[i], my_list[j] = my_list[j], my_list[i]

print(" OTHER WAY Around", my_list)


# Python Program
# Sorted vs sort

li = (3, 1, 2, 4)

print("using Sorted function :", sorted(li))

print("Tuple remains same :", li)

# sort using sort method
li.sort()
print("List is changed and sorted :", li)