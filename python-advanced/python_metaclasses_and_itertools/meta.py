''' Python 3 uses new-style of class where when if an object is instance a class
    then type(obj) is same as obj.__class__'''

class Foo:
  pass

x = Foo() #An instance x of class Foo is created
print('x.__class__ = ', x.__class__)
print('type(x) = ', type(x))
print()

result = x.__class__ is type(x)
print('comparison between x.__class__ and type(x) is:', result) #In python 2, type(x) returns <type 'instance'>
print()

''' Here type(Foo) will return type which is defined as metaclass of which
    custom classes are instance of. Also type is an instance of itself.'''
print('Return value of type(Foo): ', type(Foo))
print('Return value of type(type):', type(type))

''' type() function can be called by passing three arguments- name, bases, dct'''

Foo = type('Foo', (), {}) #Only name argument creates a simple class without any inheritance ordictionary defined class definition

x = Foo()
print('x returns: ', x)

''' In this example the name contains a class which is inherited from base class Foo
    specified as a tuple and a predifined attribut value passed through the 3rd parameter
    as dictionary.'''
ChildFoo = type('ChildFoo', (Foo,), dict(attr=100)) 

x = ChildFoo()
print()
print('The attribute value:', x.attr)
print('The child class childfoo:', x.__class__)
print('The base class foo:', x.__class__.__bases__)

'''Custom metaclasses can be created form which new classes can be derived which will act
   as instance to the metaclass so the attributes of custom metaclasses can be used.
   But some easier ways such as inheritance, decorators are available too.'''


