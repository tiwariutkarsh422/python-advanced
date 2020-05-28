import pprint as pr
import collections

''' A class can be created where the fields can be predefined 
which will solve the typo errors while using mutable data structures '''
Scientist = collections.namedtuple('Scientist', ['name','field','dob','nobel'])

''' Now multiple instance can be create and stored in a single tuple'''
scientists =(
    Scientist(name='Ada Lovelace', field='math', dob=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', dob=1882, nobel=False),
    Scientist(name='Marie Curie', field='math', dob=1867, nobel=True),
    Scientist(name='Tu Youyou', field='physics', dob=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', dob=1939, nobel=True),
    Scientist(name='Vera Rubin', field='chemistry', dob=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', dob=1951, nobel=False),
)

pr.pprint(scientists)

''' filter() function hjelps to apply a function on a complete list of data and returns a filter object
    which is an iterator
'''
#The filter function returns an filter object which is an iterator based on the condition
nobel_scientists = filter(lambda x: x.nobel is True, scientists)
math_scientists = filter(lambda x: x.field is 'math', scientists)
ninetys_scientists = filter(lambda x: x.dob > 1900 and x.dob < 2000, scientists)


#filter returns an iterator
print('Type: \n',type(nobel_scientists))
print('\n')

#This object can either be iterated using next method or can be converted to tuple
print('Filtered scientists based on nobe prize:')
pr.pprint(tuple(nobel_scientists))
print('\n')

print('Filtered scientists based on mathematics:')
pr.pprint(tuple(math_scientists))
print('\n')

print('Filtered scientists based on dob:')
pr.pprint(tuple(ninetys_scientists))
print('\n')


#filter using list comprehensions as a replacement for filter fucntions
#Also the list comprehension is not necessary as the tuple function will undergo the same process to provide same result
scientist_list_comprehension = tuple([x for x in scientists if x.nobel == True])
print('Scientists tuple through list comprehension:')
pr.pprint(scientist_list_comprehension)




