import sys
import cProfile

""" This function can generate an infinite sequence of numbers but using generator as opposed to conventional method
    because the latter can create issue with machines limited memory. """
def infinite_sequence(): #Creating generator using generator functions
  num = 0
  while True:
    yield num
    num += 1
# We can use the above function using a for loop or using next() to iterate over the generator object

#We can also use infinite sequence function to build palindrome detectors
def palindrome_checker(num):
  if (num // 10 == 0):  #Checking single digits which are not palindrome
    return False

  temp = num
  reversed_number = 0

  while temp != 0:
    reversed_number = (reversed_number * 10) + (temp % 10)
    temp = temp // 10
  
  if reversed_number == num:
     return num
  else:
     return False

for i in infinite_sequence():
  if i == 100:
    break
  else:
    pal = palindrome_checker(i)
    if pal:
      print(pal, end = " ")
print()
print()

num_squared_list = [num ** 2 for num in range(10)]
num_squared_generator = (num ** 2 for num in range(10)) #Creating genertors using generator expression

print('Squared list will create a list of squares:')
print(num_squared_list)
print()

print('Squared list using generators will create a genarator object:')
print(num_squared_generator)
print()

""" If memory is an issue then generators are effective to use, whereas if speed matters list comprehensions are faster"""

print('squared list size:', sys.getsizeof(num_squared_list))
print()
print('squared generator size:', sys.getsizeof(num_squared_generator))
print()

print('Time taken to sum the squared list:')
print(cProfile.run('sum([num ** 2 for num in range(10000)])'))
print()

print('Time taken to sum the squared generator:')
print(cProfile.run('sum((num ** 2 for num in range(10000)))'))
   
  

    
    

