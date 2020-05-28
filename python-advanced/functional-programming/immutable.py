import collections

''' A class can be created where the fields can be predefined 
which will solve the typo errors while using mutable data structures '''
Scientist = collections.namedtuple('Scientist', ['name','field','dob','nobel'])

'''The instance of scientist can be created and the keyword arguments
   can be passed'''
ada = Scientist(name='ada lovelace',field='mathematics',dob=1815,nobel=False)
print('name=',ada.name,'field=', ada.field)

''' Now multiple instance can be create and stored in a single list'''
scientists = [
    Scientist(name='Ada Lovelace', field='math', dob=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', dob=1882, nobel=False),
    Scientist(name='Marie Curie', field='math', dob=1867, nobel=True),
    Scientist(name='Tu Youyou', field='physics', dob=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', dob=1939, nobel=True),
    Scientist(name='Vera Rubin', field='chemistry', dob=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', dob=1951, nobel=False),
]

''' Using mutable and immutable data structures can cause issues with functional programming
    approach as in above example the list items can still be deleted even though its elements are a tuple'''
print("Before deletion:", scientists)
del scientists[0]
print("After deletion:", scientists)

try:
	scientists[0].name = 'ed lovelace'

except AttributeError:
	print('Cannot modify. tuples are immutable data structures')

'''Solution is to use a tuple to combine all other tuples'''
tuple_scientists = (
    Scientist(name='Ada Lovelace', field='math', dob=1815, nobel=False),
    Scientist(name='Emmy Noether', field='math', dob=1882, nobel=False),
    Scientist(name='Marie Curie', field='math', dob=1867, nobel=True),
    Scientist(name='Tu Youyou', field='physics', dob=1930, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', dob=1939, nobel=True),
    Scientist(name='Vera Rubin', field='chemistry', dob=1928, nobel=False),
    Scientist(name='Sally Ride', field='physics', dob=1951, nobel=False),
)

try:
	del tuple_scientists[0]
except TypeError:
	print("tuple items cannot be deleted!")



