import pprint as pr
import collections
import os
import time
import multiprocessing
import concurrent.futures

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

print('scienitsts data:')
pr.pprint(scientists)
print()
def convert(x):
	print(f'Runnning process {os.getpid()} with name {x.name}')
	time.sleep(1)
	result = {'name':x.name,'age':2020 - x.dob}
	print(f'Completed process {os.getpid()} with name {x.name}')
	return result

start = time.time()

scientists_name_and_age = tuple(map(convert,scientists))
end = time.time()

print()
print(f'Total time without using multiprocessing module: {end - start:.2f}')
pr.pprint(scientists_name_and_age)

'''The above execution took approx. 7 seconds to complete and it took a serial approach to complete each task.
   Now we will usw the Pool() method of multiprocessing module to use all the cores of cpu to execute the processes 
   parallelly. '''
print()
print('Total cpu core count of device', multiprocessing.cpu_count())
print()

''' multiproccessing.Pool() helps executes map function in a parallel way by creating a Pool() object'''

start = time.time()

pool = multiprocessing.Pool()
scientists_name_and_age = pool.map(convert, scientists)
end = time.time()

print(f'Total time after using multiprocessing module: {end - start:.2f}')
pr.pprint(scientists_name_and_age)
print()

''' Another module known as concurrent.futures module that contains classes known as  executors that
    executes process parallely and asynchronously.'''

print('Using concurrent.futures module.....For multiple process')
start = time.time()

'''Here we are using process pool executor which executes the map function on multiple process '''
with concurrent.futures.ProcessPoolExecutor() as executor: 
	result = executor.map(convert, scientists)

end = time.time()
print()
pr.pprint(result)
print(f'Total time after using concurrent.futures for multiple processes: {end-start:.2f}')
print()
pr.pprint(tuple(result)) #Since the result returned was in the form of an iterator converting it to immutable tuples

print()
print('Using concurrent.futures module.....For multiple threads in a single process')
start = time.time()
'''Here we are using thread pool executor which executes the map function on multiple threads in a single process '''
with concurrent.futures.ThreadPoolExecutor() as executor: 
	result = executor.map(convert, scientists)

end = time.time()
print()
pr.pprint(result)
print(f'Total time after using concurrent.futures for multiple threads: {end-start:.2f}')


