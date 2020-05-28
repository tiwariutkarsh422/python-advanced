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

''' map() function takes 2 parameters that maps first argument over a list of data 
    defined in the sceond argument.'''
scientists_names_and_ages = tuple(map(
	lambda x: {'name': x.name, 'age': 2020 - x.dob},
	scientists))
''' It creates a copy of the original data items based on the condition specified
    in the map funtions first argument.  '''
print('\n')
print('scientists mapped with their names and ages:')
pr.pprint(scientists_names_and_ages)

'''Alternate ways to use list comprehensions or the generator expressions'''
name_and_age_list = [{'name': x.name, 'dob': 2020 - x.dob} for x in scientists]
print('\n')
print('scientists mapped with their names and ages using list comprehensions:')
pr.pprint(name_and_age_list)

name_and_age_tuple = tuple({'name': x.name, 'age': 2020 - x.dob} for x in scientists)
print('\n')
print('scientists mapped with their names and ages using generator expresis:')
pr.pprint(scientists_names_and_ages)




