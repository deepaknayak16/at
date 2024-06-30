'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 1 :: Factorial of a number using recursion
               Using the Iterative technique, calculate factorial in Python.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' 
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

def fact(x):
    if x == 0:
        return 1
    return x*fact(x-1)
x = 6
print(fact(x))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 2 :: Identify whether the number is Even or Odd
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a = int(input('Enter number: '))
rem = a % 2

print('A:', a)
print('Remainder:', rem)

if rem == 0:
    print(a, 'is an even number')
else:
    print(a, 'is an odd number')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 3 :: Fibonacce series 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def fibo(n):
   if n <= 1:
      return n
   else:
      return (fibo(n-1)+fibo(n-2))
nterm = 8
if nterm <= 0:
   print("_ve Number")
else:
   for i in range(nterm):
      print(fibo(i))
      
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 4 :: Prime Number
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
number = 3
if number > 1:
   for i in range(2, number) :
      if (number % i) == 0:
         print ("not a prime numbr")
         break
   else:
      print ("prime number")
else:
   print("2 not a prime number")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 5 :: Check the string is Palindrom or not ?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# palindrome is a word, number, phrase, or another sequence of characters which read the same backward as forward
def is_pallindrom(string):
   #return string == string [::-1]
   return string.lower() == string[::-1].lower()
print(is_pallindrom('Deepak'))
print(is_pallindrom('rotator'))
#-----------------------------------------------------------------------------
def reverse(data):
   return data[::-1]
def pallindrom(data):
   rev_data = reverse(data)
   if (data == rev_data):
      return True
   return False
data = 'Date'
ans = pallindrom(data)
if ans == 1:
   print('Yes')
else:
   print('no')
#-----------------------------------------------------------------------------------
n = 1221
temp = n
rev_n = 0
while (n > 0):
   digi = n % 10
   rev_n = rev_n*10 +digi
   n = n//10
   if temp == rev_n:
      print('Pallnidrom') 
   else:
      ('Not a Palindrom')

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: Push or move all the zeor at end of the arrary
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def pushzerotoend(arr, nz):
   count = 0
   for i in range(nz):
      if arr[i] != 0:
         arr[count] = arr[i]
         count+=1
   while count < nz:
      arr[count] = 0
      count += 1
arr =[1,9,4,0,7,8,0,3,0,4,0,5]
nz = len(arr)
pushzerotoend(arr,nz)
print("Array after pushing all zeros to end of array:")
print(arr)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Questions 6 :: Push or move all the zeor at end of the arrary
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''