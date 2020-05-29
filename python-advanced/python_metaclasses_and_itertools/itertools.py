import itertools as it
'''Program to divide a given list of elements into length of an given
   positive integer n.
'''
example_list = [1,2,3,4]  #These lists are also called iterables as the canreturn elements one at a time.
example_list2 = [4,5,6,7]

print('Iterator object', iter(example_list))# iter() creates an iterator object which can then use next() to iterate over list's elements

''' zip() is an iterator operator that calls iter() internally on every argument and then 
    calls next() on each returned iterator to advance and bind the elements into a tuple
'''
zip_result = zip(example_list, example_list2)
print('Result of zip operation:')
print(list(zip_result))
print()

''' map() calls iter() on second argument then calls next() to advance to each element and 
    applies the function passed on it's first argument to each element returned by next()'''
map_result = map(len, ['utkarsh', 'tiwari', 'python'])
print('Result of map operation')
print(list(map_result))
print()

'''Using the itertools we can solve the above defined problem'''
def grouping(inputs, n):
  iters = [iter(inputs)] * n #the iter() creates a list of n references to the input list
  return zip(*iters)

''' The zip() then gets the value pointing to first and second iterator in below case
    where n=2 and binds them into a tuple and moves to third iterator'''
num_list = [1,2,3,4,5,6,7,8,9,10]
print('Grouping result:')
print(list(grouping(num_list,2)))
print()

''' But the above function poses a problem as zip() will only work if n is perfectly divisible
    by length of the input list. To solve this problem we can use zip_longest() of itertools module'''

def itertools_grouping(inputs, n):
  iters = [iter(inputs)] * n
  return it.zip_longest(*iters) #zip_longest replaces the empty pairs with fillers like None

num_list = [1,2,3,4,5,6,7,8,9,10]
print('Grouping result when n=4:')
print(list(grouping(num_list,4)))
print()

num_list = [1,2,3,4,5,6,7,8,9,10]
print('Grouping result with itertools zip_longest() when n=4:')
print(list(itertools_grouping(num_list,4)))



 
