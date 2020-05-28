import pprint as pr
import collections
from functools import reduce

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

''' map() function takes 2 parameters that maps first argument over a list of data 
    defined in the sceond argument.'''
scientists_names_and_ages = tuple(map(
	lambda x: {'name': x.name, 'age': 2020 - x.dob},
	scientists))

pr.pprint(scientists_names_and_ages)

'''We can use reduce() function that takes a function as a paramater to reduce a 
   set of data tiems passed as another argument in reduce() and also an initial
   value to start from'''

total_scientists_ages = reduce(
	lambda acc, val: acc + val['age'],
        scientists_names_and_ages,
	0)

print('scientists total age:', total_scientists_ages)


''' reduce() can also be used to group data into multiple categories'''
def reducer(acc, val):
	acc[val.field].append(val.name)
	return acc

categorized_scientists = reduce(
	reducer,
	scientists,
	{'math':[],'chemistry': [],'physics': []}
	)
print('\n')
print('Scientists categorized in their respective fields:')
pr.pprint(categorized_scientists)

''' But the above program needs the categories to be predfined which will not be feasible with large data.
    So we can use defaultdict function of collections module which automatically gets the categories for the data'''
categorized_scientists = reduce(
	reducer,
	scientists,
	collections.defaultdict(list)
	)

print('\n')
print('Categorized using default dict:')
pr.pprint(categorized_scientists)



