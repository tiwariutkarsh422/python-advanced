from pprint import pprint
from statistics import mean
from functools import reduce

def squared(x):
  return x ** 2


print('Squared by normal function:', squared(23))
print('Square of 25:', squared(25))

lambda_squared = lambda x: x ** 2
lambda_exponential = lambda x, y: x ** y
lambda_default = lambda x, y=2: x / y

print('Square of 25 using lambda function:', lambda_squared(25))
print('lambda function with 2 variables, exponential of 2 over 3:', lambda_exponential(2,3))
print('lambda function with default values, 24 divided by 2:', lambda_default(24))
print()

#Using different ethods such as sort(), map(), reduce(), filer() etc.

#1. Sorting a list of names

names = ['Utkarsh Tiwari', 'Tanmay Sharma', 'Zaid Ghori', 'Akhil Raghava']

lambda x: x.split()[-1]

print('List of names:')
pprint(names)
print()

print('Sorting names based on their last names:')
names.sort(key = lambda x: x.split()[-1])  #key takes a string based on which the list has to be sorted
pprint(names)
print()

names_and_age = [('Tanmay', 23), ('Zaid', 35), ('Utkarsh Tiwari', 28), ('Vijai Shanker', 53)]

print('Original list:')
pprint(names_and_age)
print()

print('Sorting names by their age:')
names_and_age.sort(key = lambda x: x[1])
pprint(names_and_age)
print() 

#sorting objects with the help of lambda functions

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __repr__(self):
    return f'{self.name}:{self.age}'

person_1 = Person('Utkarsh', 25)
person_2 = Person('Tanmay', 32)
person_3 = Person('Zaid', 34)

persons = [person_1, person_2, person_3]

print('Persons list:')
pprint(persons)
print()

print('Sorting persons by age using objects:')
persons.sort(key = lambda x: x.age)
pprint(persons)
print()

print('Sorting persons by names using objects:')
persons.sort(key = lambda x:x.name)
pprint(persons)
print()

#Applying filter() using lambda function

num = list(range(1, 11))
print('List of numbers:')
pprint(num)
print()

odd_nums = list(filter(lambda x: x % 2 == 0, num))
even_nums = list(filter(lambda x: x % 2 != 0, num))
print('List of even numbers filtered:')
print(even_nums)
print()

print('List of odd numbers filtered:')
print(odd_nums)
print()

data = list(range(1, 21))
mean_of_data = mean(data)

print('Average of data:', mean_of_data)
print()

above_mean = list(filter(lambda x: x > mean_of_data,data)) 
below_mean = list(filter(lambda x: x < mean_of_data, data))

print('list of data above mean:', above_mean)
print('list of data below mean:', below_mean)
print()

#Applying map() using lambda

nums = list(range(1, 11))
print('List of numbers:', nums)

squared = list(map(lambda x: x ** 2, nums))
print('Square of every element in list:', squared)
print()

check_even = list(map(lambda x: x % 2 == 0, nums))
print('Even cheker of every number on list:')
print(check_even)
print()

wc_teams = [('India', 2), ('Australia', 6), ('England', 1), ('South Africa', 2)]

print('World cup teams and their number of winnings:')
print(wc_teams)
print()

wc_teams_extra = list(map(lambda teams: (teams[0], teams[1]+1), wc_teams))
print('World cup teams with one extra winnings:')
print(wc_teams_extra)
print()

#Applying reduce() using lambda

nums = list(range(1, 11))

print('list of numbers:')
print(nums)
print()

total = reduce(lambda x, y: x+y, nums)
product = reduce(lambda x, y: x*y, nums)
print('Total of numbers using lambda functions:', total)
print('Product of all the numbers:', product)
print()

names = ['utkarsh', 'tanmay', 'zaid', 'akhil', 'vamshi']
print('Names:', names)

first_two_chars = reduce(lambda x, y: x + y[:2], names, '')
print('Concatenation of first two characters:')
print(first_two_chars)




