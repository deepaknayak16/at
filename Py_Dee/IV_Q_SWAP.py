'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: SWAP THE TWO NUMBER
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
x = 3 #int(input("Enter the value of x?" ))  
y = 5 #int(input("Enter the value of y?" ))  
print("before swapping numbers: %d   %d\n" %(x,y))  
#swapping#  
x = x + y     
y = x - y    
x = x - y     
print("After swapping: %d   %d\n"%(x,y)) 

a = 5
b = 4

a,b = b,a
print(a)
print(b)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Swap the list by position 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
list = [65, 54, 45, 23,63,47,89,35]
pos1, pos2 = 3,5
def swaplist(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
print(list)
print(swaplist(list, pos1-1, pos2-1))


