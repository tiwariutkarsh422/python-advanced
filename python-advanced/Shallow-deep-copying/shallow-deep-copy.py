import copy

original_list = [2, 4 ,['ada lovelace'], 1965, [7,8,9], [11, 12, 13]]

''' Shallow copies can be created using factory function such as list(), dict() etc.
    However shallow copies only create references to the child object present in the original lists.'''

shallow_copy_list = list(original_list)

print('original list before append:', original_list)
print('shallow copied list before append', shallow_copy_list)
print()

original_list.append(['new_append'])

print('original list after append:', original_list)
print('shallow copied list after append', shallow_copy_list)# appending value sin original copy does not affect shallow copy
print()

original_list[2][0] = 'Ed'

print('original list after specified change', original_list)
print('shallow copied list after specofied change:', shallow_copy_list)
print()
 
''' As we can see above that since shallow copy is a one level deep copy, it
    is not truly independent of the original list and it changes the shallow
    copied list as well when original list is modified as it is only a reference
    to the child objects of original_list before the append.'''

original_list = [2, 4 ,['ada lovelace'], 1965, [7,8,9], [11, 12, 13]]

''' Deep copy can be created usinfg deepcopy() function of copy module.'''
deep_copy_list = copy.deepcopy(original_list)

print('original list before change:', original_list)
print('deep copied list before change', deep_copy_list)
print()

original_list[2][0] = 'Ed'
print('original list after specified change', original_list)
print('deep copied list after specified change:', deep_copy_list)



