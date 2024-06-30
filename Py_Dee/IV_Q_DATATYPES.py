'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: HOW TO CONVERT TWO LIST INTO A DICTONARY 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
keys = ["name", "age", "city"]
values = ["Dipu", 32, "Blore" ]

my_dict = {keys[i]: values[i] for i in range(len(keys))}

my_dict2 = dict.fromkeys(keys,values)

print(my_dict)
print(my_dict2)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a = [1, 2, 3, 4, 5, 6]
b = a[1:3]
b[0] = 0
print (a)
print (b)